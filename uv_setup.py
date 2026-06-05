"""Create a Python virtual environment and install UVicorn-related packages."""

import os
import subprocess
import sys
import venv


def create_virtual_environment(venv_path: str) -> None:
    """Create a virtual environment at the given path."""
    builder = venv.EnvBuilder(with_pip=True)
    builder.create(venv_path)
    print(f"Virtual environment created at: {venv_path}")


def install_requirements(venv_path: str, requirements_file: str) -> None:
    """Install packages from requirements.txt into the virtual environment."""
    python_executable = os.path.join(venv_path, "Scripts", "python.exe")
    subprocess.check_call([python_executable, "-m", "pip", "install", "-U", "pip"])
    subprocess.check_call([python_executable, "-m", "pip", "install", "-r", requirements_file])
    print("Requirements installation completed.")


def print_activation_instructions(venv_path: str) -> None:
    """Print how to activate the virtual environment on Windows."""
    print("\nActivate the virtual environment with:")
    print(f"{venv_path}\\Scripts\\activate")
    print("Then run your Python scripts with the isolated environment.")


def main() -> None:
    venv_path = ".venv"
    requirements_file = "requirements.txt"

    if not os.path.exists(venv_path):
        create_virtual_environment(venv_path)
    else:
        print(f"Virtual environment already exists at: {venv_path}")

    if os.path.exists(requirements_file):
        install_requirements(venv_path, requirements_file)
    else:
        print(f"Requirements file not found: {requirements_file}")

    print_activation_instructions(venv_path)


if __name__ == "__main__":
    main()
