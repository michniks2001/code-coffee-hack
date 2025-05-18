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

    add_cmd = subparsers.add_parser("add")
    add_cmd.add_argument("name")
    add_cmd.add_argument("value")

    del_cmd = subparsers.add_parser("delete")
    del_cmd.add_argument("name")

    upd_cmd = subparsers.add_parser("update")
    upd_cmd.add_argument("name")
    upd_cmd.add_argument("value")

    imp_cmd = subparsers.add_parser("import")
    imp_cmd.add_argument("names", nargs="*", help="Secret names to import (if none specified, all secrets will be imported)")

    args = parser.parse_args()

    if args.command == "add":
        commands.add(args.name, args.value)
    elif args.command == "delete":
        commands.delete(args.name)
    elif args.command == "update":
        commands.update(args.name, args.value)
    elif args.command == "import":
        commands.import_to_env(*args.names)
    elif args.command == "list":
        commands.list_secrets()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
