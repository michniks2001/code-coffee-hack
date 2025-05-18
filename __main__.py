import argparse
import sys
import os

# Import from the apiport module which provides a consistent interface
# regardless of the folder name
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
import apiport

# Use the commands module from the apiport module
commands = apiport.commands

def main():
    parser = argparse.ArgumentParser(prog="apiport", description="CLI tool for managing API secrets")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("list")

    add_cmd = subparsers.add_parser("add", description="Add secrets to the vault")
    add_cmd_group = add_cmd.add_mutually_exclusive_group(required=True)
    add_cmd_group.add_argument("--file", "-f", dest="path_to_file", help="Path to a file containing secrets")
    add_cmd_group.add_argument("--key-value", "-k", dest="key_values", nargs="+", help="One or more KEY=VALUE pairs")
    add_cmd_group.add_argument("--name-value", "-n", nargs=2, dest="name_value", metavar=("NAME", "VALUE"), help="Secret name and value as separate arguments")

    del_cmd = subparsers.add_parser("delete")
    del_cmd.add_argument("name")

    upd_cmd = subparsers.add_parser("update")
    upd_cmd.add_argument("name")
    upd_cmd.add_argument("value")

    imp_cmd = subparsers.add_parser("import")
    imp_cmd.add_argument("name")

    args = parser.parse_args()

    if args.command == "add":
        if args.path_to_file:
            commands.add(None, None, args.path_to_file)
        elif args.key_values:
            if len(args.key_values) == 1 and "=" in args.key_values[0]:
                # Single KEY=VALUE pair
                commands.add(args.key_values[0])
            else:
                # Multiple KEY=VALUE pairs
                commands.add(args.key_values)
        elif args.name_value:
            # Name and value as separate arguments
            commands.add(args.name_value[0], args.name_value[1])
    elif args.command == "delete":
        commands.delete(args.name)
    elif args.command == "update":
        commands.update(args.name, args.value)
    elif args.command == "import":
        commands.import_to_env(args.name)
    elif args.command == "list":
        commands.list_secrets()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
