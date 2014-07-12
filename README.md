manifests
=========

This project contains dependency manifests in JSON format defined by the [schema](https://github.com/DependencyWatcher/manifests/blob/master/dependency.json) file.

### What can be a dependency? ###

Dependency, as its name says, is something that a project depends on. Examples are:

 * Library
 * Framework
 * Application
 * Binary component

### Contribution ###

Dependency manifests are stored in the directory tree, where each level is defined by the
consequent two letters of the dependency name. For example, for the given name "cassandra"
the directory tree would be:

    ├── ca
    │   └── ss
    │       └── an
    │           └── dr
    │               └── cassandra.json


To add a new manifest, find the relevant directory in the tree (create one if it doesn't exist),
then add a new file named `<dependency name>.json`, which conforms to the dependency JSON schema.

