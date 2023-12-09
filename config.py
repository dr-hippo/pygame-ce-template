"""Reads config.toml and sets each variable in this module to the corresponding key in the TOML."""

import os

import tomlkit

import utilities as utils

with open(os.path.join(utils.CURRENTPATH, "config.toml")) as file:
    document = tomlkit.load(file)
    for key in document.keys():
        globals()[key] = document[key]
