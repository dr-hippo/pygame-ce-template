"""Script to automate Pygbag building.
Modified from https://github.com/davidpendergast/dimensions/blob/main/make_web_bundle.py.
MAKE SURE TO USE POSIX PATHS."""

import os
import sys
import shutil
import glob
import runpy

import src.config as cfg

# OPTIONS #

FILE_GLOBS_TO_INCLUDE = [
    "main.py",
    "assets/**/*",
    "data/**/*",
    "src/**/*.py"
]

TEMPLATE = None

# Note that any preexisting contents of this directory will be deleted, so be careful.
# The actual "build" will end up in BUNDLE_DIR/build/web
BUNDLE_DIR = "build/web"

ADDITIONAL_ARGS = ["--app_name", cfg.APPNAME]

# END OPTIONS #


def _ask_yn_question(question):
    print("")  # Newline to make it a little less claustrophobic
    answer = None
    while answer is None:
        txt = input("  " + question + " (y/n): ")
        if txt == "y" or txt == "Y":
            answer = True
        elif txt == "n" or txt == "N":
            answer = False
    print("")
    return answer


def make_build(skip_prompts=False):
    """Copy the included blobs to the source folder, overwriting other files.
    Then bundle these files with Pygbag."""
    if os.path.exists(BUNDLE_DIR):
        if not skip_prompts and os.listdir(BUNDLE_DIR) \
                and not _ask_yn_question(f"Bundle destination {BUNDLE_DIR} isn't empty, overwrite?"):
            raise ValueError("Process was cancelled.")
        shutil.rmtree(BUNDLE_DIR)
        print(f"INFO: deleted {BUNDLE_DIR}")
    os.mkdir(BUNDLE_DIR)
    print(f"INFO: created {BUNDLE_DIR}")

    all_files_to_copy = set()
    for glob_code in FILE_GLOBS_TO_INCLUDE:
        for fpath in glob.glob(glob_code, recursive=True):
            if os.path.isfile(fpath):
                all_files_to_copy.add(fpath)

    print(f"\nINFO: bundle will include:")
    for fpath in sorted(all_files_to_copy):
        print(f"    {fpath}")
    if not skip_prompts and \
            not _ask_yn_question(f"Continue with these {len(all_files_to_copy)} file(s)?"):
        raise ValueError("Process was cancelled.")

    print(f"INFO: Copying the files to {BUNDLE_DIR}...")
    for fpath in all_files_to_copy:
        dest_fpath = os.path.join(BUNDLE_DIR, fpath)
        os.makedirs(os.path.dirname(dest_fpath), exist_ok=True)
        shutil.copy(fpath, dest_fpath)
    print(f"INFO: Copied {len(all_files_to_copy)} file(s).")

    arg_list = []
    if TEMPLATE is not None:
        arg_list.extend(["--template", f"{TEMPLATE}"])

    arg_list.append(BUNDLE_DIR)
    print(f"\nINFO: About to run command:\n    pygbag {' '.join(arg_list)}\n\n"
          "________________________\n")

    sys.argv = ["_"] + arg_list
    runpy.run_module("pygbag", alter_sys=True, run_name="__main__")


if __name__ == "__main__":
    make_build(skip_prompts=any(f in sys.argv for f in ("-f", "--force")))
