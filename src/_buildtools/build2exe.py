"""Script to automate PyInstaller building."""

import os

import PyInstaller.__main__
import subprocess

import src.config as cfg
import src.utilities as utils


def make_build():
    """Build to standalone executable using PyInstaller."""

    workpath = utils.to_path("build")
    distpath = utils.to_path("dist")

    arg_list = [utils.to_path("main.py")] + cfg.EXE_ADDITIONAL_ARGS

    # Add resource folders to argument list with --add-data
    for resource in cfg.EXE_DATA_TO_BUNDLE:
        arg_list.extend(["--add-data", f"{utils.to_path(resource)}{os.pathsep}{resource}"])

    if cfg.BUILD_NOPROMPTS:
        arg_list.append("-y")

    if cfg.EXE_ONEFILE:
        arg_list.append("-F")

    if cfg.ICON_FILENAME:
        arg_list.extend(["-i", utils.to_path(cfg.ASSET_PATH, cfg.IMAGE_PATH, cfg.ICON_FILENAME)])

    if cfg.VENV_DIR:
        arg_list.extend(["-p", os.path.join(cfg.VENV_DIR, "Lib", "site-packages")])

    arg_list.extend([
        "--distpath", distpath,
        "--workpath", workpath
    ])
    print(f"INFO: Running command:\n\tpyinstaller {' '.join(arg_list)}")
    PyInstaller.__main__.run(arg_list)
    print("INFO: Build complete. Running built executable.")

    subprocess.run(os.path.join(distpath, cfg.APPNAME_SIMPLE, cfg.APPNAME_SIMPLE))


if __name__ == "__main__":
    make_build()
