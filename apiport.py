"""
apiport module - Provides consistent access to the apiport functionality
regardless of the folder name
"""
import os
import sys
import importlib.util
from pathlib import Path

# Get the absolute path to the directory containing this file
PACKAGE_DIR = os.path.abspath(os.path.dirname(__file__))

# Function to dynamically import a module from the package directory
def import_module(module_name):
    module_path = os.path.join(PACKAGE_DIR, f"{module_name}.py")
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

# Import the modules dynamically
commands = import_module("commands")
storage = import_module("storage")
encryption = import_module("encryption")

# Export the modules
__all__ = ['commands', 'storage', 'encryption']
