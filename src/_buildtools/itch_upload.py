"""Uses butler to upload built files to itch. Requires butler being installed and user being logged in."""

import os
import sys
import subprocess
import shutil
import platform

import src._buildtools.build2web as build2web
import src.config as cfg

if not shutil.which("butler"):
    print("Cannot find butler. Make sure it is installed and included on PATH.")
    sys.exit()

# Command is "butler push directory user/game:channel"
# Push executable build
subprocess.run(["butler", "push",
                os.path.join("../../dist", cfg.APPNAME_SIMPLE),  # Directory of executable build
                f"{cfg.AUTHOR_SIMPLE.lower()}/{cfg.APPNAME_SIMPLE.lower()}:{platform.system()}",
                "--userversion", cfg.VERSION
                ])

# Push web build
subprocess.run(["butler", "push",
                os.path.join(build2web.BUNDLE_DIR, "../../build", "web"),  # Directory of web build
                f"{cfg.AUTHOR_SIMPLE.lower()}/{cfg.APPNAME_SIMPLE.lower()}:Web",
                "--userversion", cfg.VERSION
                ])
