"""Uses butler to upload built files to itch. Requires butler being installed and user being logged in."""

import os
import sys
import subprocess
import shutil
import platform

import src.config as cfg
import src.utilities as utils

if not shutil.which("butler"):
    print("Cannot find butler. Make sure it is installed and included on PATH.")
    sys.exit()


def push(folder, channel: str):
    """
    Upload folder to itch.io with butler.

    :param folder: Folder containing game files.
    :param channel: Channel on game page.
    """

    arg_list = ["butler", "push", folder, cfg.AUTHOR_SIMPLE.lower() + "/" + cfg.APPNAME_SIMPLE.lower() + ":" + channel]

    arg_list.extend(["--userversion", cfg.VERSION])

    if cfg.UPLOAD_DRY_RUN:
        arg_list.extend(["--dry-run"])

    if cfg.UPLOAD_ONLY_IF_CHANGED:
        arg_list.extend(["--if-changed"])

    # Command is "butler push folder user/game:channel"
    subprocess.run(arg_list)


def main():
    """Push executable and web build."""
    push(os.path.join(utils.get_current_path(), "dist", cfg.APPNAME_SIMPLE), platform.system())
    push(os.path.join(utils.get_current_path(), cfg.WEB_BUNDLE_DIR, "build", "web"), "web")


if __name__ == "__main__":
    main()
