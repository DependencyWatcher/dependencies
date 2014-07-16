manifests
=========

This project contains dependency manifests in JSON format defined by the [schema](https://github.com/DependencyWatcher/manifests/blob/master/dependency.json) file.

### What can be a dependency? ###

Dependency, as its name says, is something that a project depends on. Examples are:

 * Library
 * Framework
 * Application
 * Binary component

### Uniqueness ###

Dependency name along with the its homepage URL must define it in a unique manner.
There may be aliases used in different frameworks/toolkits as well. For instance,
the name `apache-kafka` and the URL "https://kafka.apache.org/" can be used for defining
Apache Kafka, and one of its aliases would be `org.apache.kafka:kafka_2.10` (Maven alias).

### Contribution ###

Dependency manifests are stored in the directory tree under the directory called `_m`,
where each level is defined by the first four letters of the dependency name.
For example, for the given name "cassandra" the directory tree would be:

    ├── _m
    │   └── c
    │       └── a
    │           └── s
    │               └── s
    │                   ├── cassandra.json


Templates are stored in the same way under the `_t` directory.

To add a new manifest, find the relevant directory in the tree (create one if it doesn't exist),
then add a new file named `<dependency name>.json`, which conforms to the dependency JSON schema.

### Manifest Generator ###

To make generating of manifest file easier, use script `./generate.py`. This script asks user for needed
values based on schema file, then generates a JSON file containing the answers user provided.


