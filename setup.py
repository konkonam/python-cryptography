import subprocess
import json
import sys

SUPPORTED_PYTHON_VERSION = "3.8.1"

def set_python_path():
        with open("./.vscode/settings.json", "r") as file:
            data = json.load(file)

        data["python.pythonPath"] = "${workspaceFolder}\\.env\\Scripts\\python.exe"

        with open("./.vscode/settings.json", "w") as file:
            json.dump(data, file)

if __name__ == "__main__":

    if not SUPPORTED_PYTHON_VERSION in sys.version:
        print("You need version " + SUPPORTED_PYTHON_VERSION)
        print("You should consider using version " + sys.version)

    subprocess.run(["pip", "install", "virtualenv"])
    subprocess.run(["virtualenv", ".env/"])

    set_python_path()

    subprocess.run([".\\.env\\Scripts\\python.exe", "-m", "pip", "install", "-r", "requirements.txt"])

    