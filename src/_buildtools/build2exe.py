"""Script to automate PyInstaller building."""

import os

import PyInstaller.__main__
import subprocess
import platform
import struct

import src.config as cfg
import src.utilities as utils

_WIN, _MAC, _LINUX = "Windows", "Darwin", "Linux"  # platform.system return values

osnames = {
    "Windows": "Win",
    "Darwin": "MacOS",
    "Linux": "Linux"
}

fileexts = {
    "Windows": ".exe",
    "Darwin": ".app",
    "Linux": ""
}


def get_exe_name() -> str:
    """Generate unique file/folder name for the executable, including system and word size info."""
    return "{}_{}{}bit".format(
        cfg.APPNAME_SIMPLE,  # Base name of executable
        osnames[platform.system()],  # OS name
        struct.calcsize('P') * 8  # Bit count of system
    )


def get_exe_path() -> str:
    """Get the path of the built executable local to utilities.rootdir()."""
    if cfg.EXE_ONEFILE:
        return os.path.join("dist", get_exe_name() + fileexts[platform.system()])

    else:
        return os.path.join("dist", get_exe_name(), get_exe_name() + fileexts[platform.system()])


def get_exe_dir() -> str:
    """Get the parent directory of the built executable,
    or the executable itself for one-file builds, local to utilities.rootdir()."""

    if cfg.EXE_ONEFILE:
        return os.path.join("dist", get_exe_name() + fileexts[platform.system()])

    else:
        return os.path.join("dist", get_exe_name())


def make_build():
    """Build to standalone executable using PyInstaller."""

    arg_list = [utils.to_path("main.py")] + cfg.EXE_ADDITIONAL_ARGS

    # Add resource folders to argument list with --add-data
    for resource in cfg.EXE_DATA_TO_BUNDLE:
        arg_list.extend(["--add-data", f"{utils.to_path(resource)}{os.pathsep}{resource}"])

    if cfg.BUILD_NOPROMPTS:
        arg_list.append("-y")

    # Apparently only onefile builds work on Mac
    if cfg.EXE_ONEFILE or platform.system() == _MAC:
        arg_list.append("-F")

        # Enabling splash screen in directory mode makes window start unfocused, so only enable it in onefile mode
        # Splash screen doesn't work on Mac
        if cfg.EXE_SPLASH_FILENAME and platform.system() != _MAC:
            arg_list.extend(["--splash", utils.to_path(cfg.ASSET_PATH, cfg.IMAGE_PATH, cfg.EXE_SPLASH_FILENAME)])

    if cfg.ICON_FILENAME:
        arg_list.extend(["-i", utils.to_path(cfg.ASSET_PATH, cfg.IMAGE_PATH, cfg.ICON_FILENAME)])

    if cfg.VENV_DIR:
        arg_list.extend(["-p", utils.to_path(cfg.VENV_DIR, "Lib", "site-packages")])

    arg_list.extend([
        "--distpath", utils.to_path("dist"),
        "--workpath", utils.to_path("build"),
        "--specpath", utils.rootdir()
    ])

    arg_list.extend([
        "-n", get_exe_name()
    ])

    print(f"INFO: Running command:\n\tpyinstaller {' '.join(arg_list)}")
    PyInstaller.__main__.run(arg_list)
    print(f"INFO: Build complete. Running built executable at {get_exe_path()}")

    subprocess.run(utils.to_path(get_exe_path()))


if __name__ == "__main__":
    make_build()
