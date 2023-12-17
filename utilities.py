"""Script with useful functions for loading and caching different types of assets."""

import sys
import os
from typing import Union

import pygame

import config as cfg

pygame.init()


def get_current_path() -> str:
    """Get resource path both when running normally or in PyInstaller bundle"""
    if getattr(sys, 'frozen', False):  # PyInstaller adds this attribute
        # Running in a PyInstaller bundle
        return sys._MEIPASS

    # Otherwise running in normal python environment
    return os.path.dirname(__file__)


# TODO: add caching functions
def load_image(*pathparts: str, filetype: str = "png", essential: bool = False) -> pygame.surface.Surface:
    """
    Loads surface from image file and converts its format to make blitting more efficient.

    :param pathparts: Subfolders leading to file and filename, local to config.IMAGE_PATH.
    :param filetype: Image filetype. Defaults to PNG.
    :param essential: Whether to raise error when file is not found or return placeholder surface.
    :return: Loaded surface
    """
    subfolders = os.path.join(cfg.ASSET_PATH, cfg.IMAGE_PATH, *pathparts[:-1])
    name = pathparts[-1] + os.extsep + filetype
    fullpath = os.path.join(get_current_path(), subfolders, name)

    try:
        image = pygame.image.load(fullpath)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
        return image

    except FileNotFoundError as error:
        if essential:
            raise error

        else:
            # Return placeholder magenta surface
            placeholder = pygame.surface.Surface((32, 32))
            placeholder.fill("#ff00ff")
            return placeholder


def load_sound(*pathparts: str, filetype: str = "mp3", essential: bool = False) -> Union[pygame.mixer.Sound, None]:
    """
    Loads sound from audio file.

    :param pathparts: Subfolders leading to file and filename, local to config.AUDIO_PATH.
    :param filetype: Audio filetype. Defaults to MP3.
    :param essential: Whether to raise error when file is not found or return None.
    :return: Loaded sound
    """
    subfolders = os.path.join(cfg.ASSET_PATH, cfg.AUDIO_PATH, *pathparts[:-1])
    name = pathparts[-1] + os.extsep + filetype
    fullpath = os.path.join(get_current_path(), subfolders, name)

    try:
        sound = pygame.mixer.Sound(fullpath)
        return sound

    except FileNotFoundError as error:
        if essential:
            raise error

        else:
            return None
