# ooarg

Argument parser using object oriented design.

Inspired by [Oclif](https://oclif.io/). Using OOP design and folder structure to specify command-subcommand relationship.

For example, the following folder structure means: `hello` is a command, `world` and `world2` are the subcommands of `hello`.

`commands/hello/__init__.py` has the command parser. 2 world python files are parser of the subcommands.

```
.
└── commands
    └── hello
        ├── __init__.py
        ├── world.py
        └── world2.py
```

Sample Usage

```bash
cli_name hello ...            # commands/hello/__init__.py
cli_name hello world ...      # commands/hello/world.py
cli_name hello world2 ...     # commands/hello/world2.py
```
