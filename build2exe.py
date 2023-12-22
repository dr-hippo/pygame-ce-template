"""Script to automate PyInstaller building."""

import os

import PyInstaller.__main__

import src.config as cfg

# OPTIONS #

NOCONFIRM = True
ONEFILE = False
RESOURCE_DIRS = ["assets", "data", "src"]
ICON_PATH = None
# os.path.join("assets", "images", "sample.jpg")

# If not using a virtual environment (not recommended), set to None
VENV_DIR = ".venv"

# END OPTIONS #

arg_list = ["main.py", "--noconsole", "--log-level", "WARN", "-n", cfg.APPNAME_SIMPLE]

# Add resource folders to argument list with --add-data
for resource in RESOURCE_DIRS:
    arg_list.extend(["--add-data", f"{resource}{os.pathsep}{resource}"])

if NOCONFIRM:
    arg_list.append("-y")

if ONEFILE:
    arg_list.append("-F")

if ICON_PATH:
    arg_list.extend(["-i", ICON_PATH])

if VENV_DIR:
    arg_list.extend(["-p", os.path.join(VENV_DIR, "Lib", "site-packages")])


def make_build():
    """Run PyInstaller with the provided arguments."""
    PyInstaller.__main__.run(arg_list)


if __name__ == "__main__":
    make_build()
