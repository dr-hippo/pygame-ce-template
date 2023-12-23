"""Uses butler to upload built files to itch. Requires butler being installed and user being logged in."""

import os
import sys
import subprocess
import shutil
import platform

import src.config as cfg

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

    # Command is "butler push folder user/game:channel"
    subprocess.run(arg_list)


def main():
    """Push executable and web build."""
    push(cfg.EXE_DIST_DIR, platform.system())
    push(cfg.WEB_BUNDLE_DIR, "web")


if __name__ == "__main__":
    main()
