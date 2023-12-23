"""Script to automate PyInstaller building."""

import os

import PyInstaller.__main__

import src.config as cfg

# OPTIONS #

NOCONFIRM = True
ONEFILE = False
DIRS_TO_BUNDLE = ["assets", "data", "src"]
ICON_PATH = None
# os.path.join("assets", "images", "sample.jpg")

# If not using a virtual environment (not recommended), set to None
VENV_DIR = ".venv"

ADDITIONAL_ARGS = ["--noconsole", "--log-level", "WARN", "-n", cfg.APPNAME_SIMPLE]

# END OPTIONS #


def make_build():
    """Build to standalone executable using PyInstaller."""
    arg_list = ["main.py"] + ADDITIONAL_ARGS

    # Add resource folders to argument list with --add-data
    for resource in DIRS_TO_BUNDLE:
        arg_list.extend(["--add-data", f"{resource}{os.pathsep}{resource}"])

    if NOCONFIRM:
        arg_list.append("-y")

    if ONEFILE:
        arg_list.append("-F")

    if ICON_PATH:
        arg_list.extend(["-i", ICON_PATH])

    if VENV_DIR:
        arg_list.extend(["-p", os.path.join(VENV_DIR, "Lib", "site-packages")])

    print(arg_list)
    print(f"INFO: Running command:\n\tpyinstaller {' '.join(arg_list)}")
    PyInstaller.__main__.run(arg_list)


if __name__ == "__main__":
    make_build()
