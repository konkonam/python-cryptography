import sys
import subprocess

SUPPORTED_PYTHON_VERSION = "3.8.1"


subprocess.run(["pip", "install", "virtualenv"])
subprocess.run(["virtualenv", ".env/"])

if not SUPPORTED_PYTHON_VERSION in sys.version:
    print("You need version " + SUPPORTED_PYTHON_VERSION)
    print("Your version: " + sys.version)
    exit(1)
