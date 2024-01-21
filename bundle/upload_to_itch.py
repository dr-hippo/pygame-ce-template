"""Uses butler to upload built files to itch. Requires butler being installed and user being logged in."""

import shutil
import subprocess
import sys

import bundle.to_exe as build2exe
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

    user = cfg.AUTHOR_SIMPLE.lower()
    project = cfg.APPNAME_SIMPLE.lower()
    print(f"INFO: Pushing to {user}.itch.io/{project} channel {channel}")

    # Command is "butler push folder user/game:channel --other_args"
    arg_list = ["butler", "push", folder, user + "/" + project + ":" + channel]

    arg_list.extend(["--userversion", cfg.VERSION])

    if cfg.UPLOAD_DRY_RUN:
        arg_list.append("--dry-run")

    if cfg.UPLOAD_ONLY_IF_CHANGED:
        arg_list.append("--if-changed")

    subprocess.run(arg_list)


def main():
    """Push executable and web build."""
    push(utils.to_path(build2exe.get_exe_dir()), utils.get_platform().lower())
    push(utils.to_path(cfg.WEB_BUNDLE_DIR, "build", "web"), "web")


if __name__ == "__main__":
    main()
