import argparse
import sys
import os

# Import from the apiport module which provides a consistent interface
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
import apiport

# Use the commands module from the apiport module
commands = apiport.commands

def main():
    parser = argparse.ArgumentParser(prog="apiport", description="CLI tool for managing API secrets")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("list")

    add_cmd = subparsers.add_parser("add", help="Add secrets to the vault", description="Add secrets to the vault")
    add_cmd_group = add_cmd.add_mutually_exclusive_group(required=True)
    add_cmd_group.add_argument("--file", "-f", dest="path_to_file", help="Path to a file containing secrets")
    add_cmd_group.add_argument("--key-value", "-k", dest="key_values", nargs="+", help="One or more KEY=VALUE pairs")
    add_cmd_group.add_argument("--name-value", "-n", nargs=2, dest="name_value", metavar=("NAME", "VALUE"), help="Secret name and value as separate arguments")

    del_cmd = subparsers.add_parser("delete", help="Delete a secret by name", description="Delete a secret by name")
    del_cmd.add_argument("name")

    upd_cmd = subparsers.add_parser("update", help="Update a secret's value", description="Update a secret's value")
    upd_cmd.add_argument("name")
    upd_cmd.add_argument("value")

    imp_cmd = subparsers.add_parser("import", help="Import secrets into .env file", description="Import secrets into a .env file")
    imp_cmd.add_argument("names", nargs="*", help="Secret names to import (if none specified, all secrets will be imported)")

    # Custom help command
    if len(sys.argv) >= 2 and sys.argv[1] == "help":
        if len(sys.argv) == 2:
            print("""
Usage:
  apiport [command] [options]

Commands:
  add       Add secrets to the vault
  delete    Delete a secret by name
  update    Update the value of an existing secret
  import    Import secrets into a .env file
  list      List all stored secrets
  help      Show help for a command

Run 'apiport help [command]' for more information on a command.
""")
            sys.exit(0)
        elif len(sys.argv) >= 3 and sys.argv[2] in subparsers.choices:
            subparsers.choices[sys.argv[2]].print_help()
            sys.exit(0)
        else:
            print(f"Unknown command '{sys.argv[2]}'. Run 'apiport help' to see available commands.")
            sys.exit(1)

    args = parser.parse_args()

    if args.command == "add":
        if args.path_to_file:
            commands.add(None, None, args.path_to_file)
        elif args.key_values:
            if len(args.key_values) == 1 and "=" in args.key_values[0]:
                commands.add(args.key_values[0])
            else:
                commands.add(args.key_values)
        elif args.name_value:
            commands.add(args.name_value[0], args.name_value[1])
    elif args.command == "delete":
        commands.delete(args.name)
    elif args.command == "update":
        commands.update(args.name, args.value)
    elif args.command == "import":
        commands.import_to_env(*args.names)
    elif args.command == "list":
        commands.list_secrets()

if __name__ == "__main__":
    main()
