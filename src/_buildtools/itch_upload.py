"""Uses butler to upload built files to itch. Requires butler being installed and user being logged in."""

import sys
import subprocess
import shutil
import platform

import src.config as cfg
import src.utilities as utils

import src._buildtools.build2exe as build2exe

if not shutil.which("butler"):
    print("Cannot find butler. Make sure it is installed and included on PATH.")
    sys.exit()

osnames = {
    "Windows": "windows",
    "Darwin": "mac",
    "Linux": "linux"
}


def push(folder, channel: str):
    """
    Upload folder to itch.io with butler.

    :param folder: Folder containing game files.
    :param channel: Channel on game page.
    """

    user = cfg.AUTHOR_SIMPLE.lower()
    project = cfg.APPNAME_SIMPLE.lower()
    print(f"INFO: Pushing to {user}.itch.io/{project} channel {channel}")

    arg_list = ["butler", "push", folder, user + "/" + project + ":" + channel]

    arg_list.extend(["--userversion", cfg.VERSION])

    if cfg.UPLOAD_DRY_RUN:
        arg_list.append("--dry-run")

    if cfg.UPLOAD_ONLY_IF_CHANGED:
        arg_list.append("--if-changed")

    # Command is "butler push folder user/game:channel"
    subprocess.run(arg_list)


def main():
    """Push executable and web build."""
    push(utils.to_path(build2exe.get_exe_dir()), osnames[platform.system()])
    push(utils.to_path(cfg.WEB_BUNDLE_DIR, "build", "web"), "web")


if __name__ == "__main__":
    main()
