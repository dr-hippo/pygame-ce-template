"""Script to automate Pygbag building.
Modified from https://github.com/davidpendergast/dimensions/blob/main/make_web_bundle.py."""

import os
import sys
import shutil
import glob
import runpy

import src.config as cfg
import src.utilities as utils


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

    os.chdir(utils.rootdir())

    if os.path.exists(cfg.WEB_BUNDLE_DIR):
        if not skip_prompts and os.listdir(cfg.WEB_BUNDLE_DIR) \
                and not _ask_yn_question(f"Bundle destination {cfg.WEB_BUNDLE_DIR} isn't empty, overwrite?"):
            raise ValueError("Process was cancelled.")
        shutil.rmtree(cfg.WEB_BUNDLE_DIR)
        print(f"INFO: deleted {cfg.WEB_BUNDLE_DIR}")
    os.mkdir(cfg.WEB_BUNDLE_DIR)
    print(f"INFO: created {cfg.WEB_BUNDLE_DIR}")

    all_files_to_copy = set()
    for glob_code in cfg.WEB_INCLUDE_GLOBS:
        for fpath in glob.glob(glob_code, recursive=True):
            if os.path.isfile(fpath):
                all_files_to_copy.add(fpath)

    for glob_code in cfg.WEB_EXCLUDE_GLOBS:
        for fpath in glob.glob(glob_code, recursive=True):
            fpath = os.path.normpath(fpath)
            if os.path.isfile(fpath) and fpath in all_files_to_copy:
                all_files_to_copy.remove(fpath)

    print(f"\nINFO: bundle will include:")
    for fpath in sorted(all_files_to_copy):
        print(f"    {fpath}")
    if not skip_prompts and \
            not _ask_yn_question(f"Continue with these {len(all_files_to_copy)} file(s)?"):
        raise ValueError("Process was cancelled.")

    print(f"INFO: Copying the files to {cfg.WEB_BUNDLE_DIR}...")
    for fpath in all_files_to_copy:
        dest_fpath = os.path.join(cfg.WEB_BUNDLE_DIR, fpath)
        os.makedirs(os.path.dirname(dest_fpath), exist_ok=True)
        shutil.copy(fpath, dest_fpath)
    print(f"INFO: Copied {len(all_files_to_copy)} file(s).")

    arg_list = []
    if cfg.WEB_TEMPLATE is not None:
        arg_list.extend(["--template", utils.to_path(cfg.WEB_TEMPLATE)])

    if cfg.ICON_FILENAME:
        arg_list.extend(["--icon", utils.to_path(cfg.ASSET_PATH, cfg.IMAGE_PATH, cfg.ICON_FILENAME)])

    arg_list.extend(cfg.WEB_ADDITIONAL_ARGS)
    arg_list.append(cfg.WEB_BUNDLE_DIR)
    print(f"\nINFO: About to run command:\n    pygbag {' '.join(arg_list)}\n\n"
          "________________________\n")

    sys.argv = ["_"] + arg_list
    runpy.run_module("pygbag", alter_sys=True, run_name="__main__")


if __name__ == "__main__":
    make_build(skip_prompts=any(f in sys.argv for f in ("-f", "--force") or cfg.BUILD_NOPROMPTS))
