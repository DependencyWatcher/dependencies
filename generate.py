#!/usr/bin/env python2.7

import sys, json, os, re
sys.dont_write_bytecode = True

def instantiate(root, node=None, parent_desc=None, answers=[]):
	""" Traverses the given JSON schema tree, and generates a JSON object for it """
	if node is None:
		node = root
	try:
		desc = node["description"]
	except:
		pass

	try:
		for p in node["$ref"].split("/"):
			if p == "#":
				definition = root
			else:
				definition = definition[p]
		return instantiate(root, definition, desc, answers)
	except KeyError:
		pass

	try:
		try:
			node["enum"]
			type = "enum"
		except KeyError:
			type = node["type"]

		if type == "object":
			obj = {}
			for p, n in node["properties"].iteritems():
				v = instantiate(root, n, parent_desc, answers)
				if not v is None and not v == "" and not v == {}:
					obj[p] = v
			return obj

		if type == "boolean" or type == "integer" or type == "number" or type == "string" or type == "enum":
			if not parent_desc is None:
				desc = "%s / %s" % (parent_desc, desc)
			if type == "enum":
				info = "constant: %s" % ",".join(node["enum"])
			else:
				info = type
			v = raw_input("Enter '%s' (%s) []: " % (desc, info)).strip()
			answers.append(v)
			return v

		if type == "array":
			arr = []
			while True:
				v = instantiate(root, node["items"], parent_desc, answers)
				if not v is None and not v == "" and not v == {}:
					arr.append(v)
				else:
					break
			return arr

	except KeyError:
		pass
	return None


if __name__ == '__main__':
	with open('dependency.json') as f:
		schema = json.load(f)

	answers = []
	version = instantiate(schema, None, None, answers)

	with open("answers.txt", "w") as f:
		f.write("\n".join(answers))
	print("Stored answers to answers.txt")

	name = version["name"]
	dirname = "/".join([i for i in re.sub("[^a-zA-Z0-9]*", "", name[:4])])
	if not os.path.exists(dirname):
		os.makedirs(dirname)

	target = "%s/%s.json" % (dirname, name)
	if os.path.exists(target):
		system.exit("File '%s' already exists!")

	with open(target, "w") as f:
		f.write(json.dumps(version, indent=2))

	print("\nCreated manifest file: %s" % target)

