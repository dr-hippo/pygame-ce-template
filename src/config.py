"""Configuration file."""

from pygame import Rect, Vector2
from src.scenes.test import TestScene
from src.framework import Scene


# GENERAL #
APPNAME = "Pygame-CE Template"
AUTHOR = "Dr.Hippo"
VERSION = "pre-alpha"

# These are used to create data directories, make sure they stay the same across versions
# They shouldn't include spaces or special characters
# If uploading to itch.io, the lowercase versions of these should be your username/project name
APPNAME_SIMPLE = "Pygame-CE-Template"
AUTHOR_SIMPLE = "DrHippo"
# E.g. this will be uploaded to https://drhippo.itch.io/pygame-ce-template


# VISUAL #
RESOLUTION = Vector2(640, 360)
TARGET_FPS = 120


# DEBUG #
SHOW_FPS = True


# SCENES #
STARTING_SCENE: type[Scene] = TestScene


# DIRECTORY NAMES #
ASSET_PATH = "assets"
AUDIO_PATH = "audio"
FONT_PATH = "fonts"
IMAGE_PATH = "images"
DATA_PATH = "data"


# BUILD #
BUILD_NOPROMPTS = True

# Filename of image to set as the window/tray icon for executable, and favicon for web
ICON_FILENAME = "default-icon.png"

# If not using a virtual environment (not recommended), set to None
VENV_DIR = ".venv"


# BUILD (EXECUTABLE) #
# Whether to build to a single executable with no dependencies.
# Set to False to build to a directory (faster start times)
EXE_ONEFILE = False

# Data to be bundled
EXE_DATA_TO_BUNDLE = [ASSET_PATH, DATA_PATH]

# TODO: Data to be copied into the build folder
# User-accessible, only available when building to a directory
EXE_DATA_TO_COPY = ["LICENSE.txt"]

# Image to show while executable unpacks itself
# Not available when building to a directory or on Mac
EXE_SPLASH_FILENAME = "default-splash.png"

EXE_ADDITIONAL_ARGS = ["--noconsole", "--log-level", "WARN"]


# BUILD (WEB) #
WEB_INCLUDE_GLOBS = [
    "main.py",
    f"{ASSET_PATH}/**/*",
    f"{DATA_PATH}/**/*",
    "src/**/*.py"
]

WEB_EXCLUDE_GLOBS = [
    "src/_buildtools/**/*"
]

# Web export template modified from https://github.com/pygame-web/archives/blob/main/0.8/default.tmpl
WEB_TEMPLATE = "src/_buildtools/web-template.tmpl"

# Note that any preexisting contents of this directory will be deleted, so be careful.
# The actual "build" will end up in BUNDLE_DIR/build/web
WEB_BUNDLE_DIR = "build/web"

WEB_ADDITIONAL_ARGS = ["--app_name", APPNAME]


# ITCH UPLOAD WITH BUTLER #
# Don't actually upload anything, just show what would happen
UPLOAD_DRY_RUN = False

# Don't actually upload if builds haven't changed
UPLOAD_ONLY_IF_CHANGED = True
