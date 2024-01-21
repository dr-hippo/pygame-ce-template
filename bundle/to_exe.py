"""Script to automate PyInstaller building."""

import os
import struct
import subprocess

import PyInstaller.__main__

import src.config as cfg
import src.utilities as utils

fileexts = {
    "Win": ".exe",
    "MacOS": ".app",
    "Linux": ""
}


def get_exe_name() -> str:
    """Generate unique file/folder name for the executable, including system and word size info."""
    return "{}_{}_{}{}bit".format(
        cfg.APPNAME_SIMPLE,  # Base game name
        cfg.VERSION,
        utils.get_platform(),  # OS name
        struct.calcsize('P') * 8  # Bit count of system
    )


def get_exe_path() -> str:
    """Get the path of the built executable local to utilities.rootdir()."""
    if cfg.EXE_ONEFILE:
        return os.path.join("dist", get_exe_name() + fileexts[utils.get_platform()])

    else:
        return os.path.join("dist", get_exe_name(), get_exe_name() + fileexts[utils.get_platform()])


def get_exe_dir() -> str:
    """Get the parent directory of the built executable,
    or the executable itself for one-file builds, local to utilities.rootdir()."""

    if cfg.EXE_ONEFILE:
        return os.path.join("dist", get_exe_name() + fileexts[utils.get_platform()])

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

    # Apparently only onefile builds work on MacOS
    if cfg.EXE_ONEFILE or utils.get_platform() == "MacOS":
        arg_list.append("-F")

        # Enabling splash screen in directory mode makes window start unfocused, so only enable it in onefile mode
        # Splash screen doesn't work on MacOS
        if cfg.EXE_SPLASH_FILENAME and utils.get_platform() != "MacOS":
            arg_list.extend(["--splash", utils.to_path(cfg.ASSET_PATH, cfg.IMAGE_PATH, cfg.EXE_SPLASH_FILENAME)])

    if cfg.ICON_FILENAME:
        arg_list.extend(["-i", utils.to_path(cfg.ASSET_PATH, cfg.IMAGE_PATH, cfg.ICON_FILENAME)])

    if cfg.VENV_DIR:
        arg_list.extend(["-p", utils.to_path(cfg.VENV_DIR, "Lib", "site-packages")])

    arg_list.extend([
        "--distpath", utils.to_path("dist"),
        "--workpath", utils.to_path("build"),
        "--specpath", utils.rootdir(),
        "-n", get_exe_name()
    ])

    print(f"INFO: Running command:\n\tpyinstaller {' '.join(arg_list)}")
    PyInstaller.__main__.run(arg_list)
    print(f"INFO: Build complete. Running built executable at {get_exe_path()}")

    subprocess.run(utils.to_path(get_exe_path()))


if __name__ == "__main__":
    make_build()
