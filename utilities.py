"""Script with useful functions for loading and caching different types of assets."""

import sys
import os

import pygame


pygame.init()

CURRENTPATH = ""
if getattr(sys, 'frozen', False):  # PyInstaller adds this attribute
    # Running in a PyInstaller bundle
    CURRENTPATH = sys._MEIPASS
else:
    # Running in normal python environment
    CURRENTPATH = os.path.dirname(__file__)

# TODO: add loading and caching functions
