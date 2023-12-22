"""Script with useful functions for loading and caching different types of assets."""

import sys
import os
from typing import Union, Sequence

import pygame

import src.config as cfg

pygame.init()


def get_current_path() -> str:
    """Get base path when running normally, in executable or in browser."""
    if getattr(sys, 'frozen', False):  # PyInstaller adds this attribute
        # Running in a PyInstaller bundle
        return sys._MEIPASS

    elif sys.platform == "emscripten":
        # Running in a Pygbag bundle
        return ""

    # Otherwise, this is running in normal python environment, so make sure to go one level up, out of /src
    return os.path.dirname(os.path.dirname(__file__))


# TODO: add caching functions
def load_image(*pathparts: str, filetype: str = "png", essential: bool = False) -> pygame.surface.Surface:
    """
    Loads surface from image file and converts its format to make blitting more efficient.

    :param pathparts: Subfolders leading to file and filename, local to config.IMAGE_PATH.
    :param filetype: Image filetype. Defaults to PNG.
    :param essential: Whether to raise error when image is not found or return placeholder surface.
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


def load_sound(*pathparts: str, filetype: str = "mp3", essential: bool = False) -> pygame.mixer.Sound:
    """
    Loads sound from audio file.

    :param pathparts: Subfolders leading to file and filename, local to config.AUDIO_PATH.
    :param filetype: Audio filetype. Defaults to MP3.
    :param essential: Whether to raise error when sound is not found or return None.
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
            return load_sound("empty")


def load_font(*pathparts: str, filetype: str = "ttf", size: int = 16, essential: bool = False, **styleattrs) \
        -> pygame.font.Font:
    """
    Loads font from font file at specified path and sets style flags.

    :param pathparts: Subfolders leading to file and filename, local to config.FONT_PATH.
    :param filetype: Audio filetype. Defaults to TTF.
    :param size: Height of the font in pixels.
    :param essential: Whether to raise error when font is not found, or return a similar system font or the default
    pygame font.
    :param styleattrs: Sets the font's style attributes. See https://pyga.me/docs/ref/font.html#pygame.font.Font for
    details.
    :return: Loaded font
    """
    if pathparts[-1]:
        subfolders = os.path.join(cfg.ASSET_PATH, cfg.FONT_PATH, *pathparts[:-1])
        name = pathparts[-1] + os.extsep + filetype
        fullpath = os.path.join(get_current_path(), subfolders, name)

    else:
        fullpath = None

    try:
        font = pygame.Font(fullpath, size)

    except FileNotFoundError as error:
        if essential:
            raise error

        else:
            # Try finding a system font with the filename; this defaults to pygame's default if not found
            font = pygame.font.SysFont(pathparts[-1], size)

    finally:
        # Set style attributes
        for key in styleattrs:
            setattr(font, key, styleattrs[key])
        return font


def render_text(text: str, font: pygame.font.Font, color, surface: pygame.Surface,
                aa: bool = True, **positionkwargs: Union[int, Sequence[int]]) -> None:
    """
    Renders text in the specified font and color onto surface, wrapping if needed.

    :param text: Text to render.
    :param font: Font to render with.
    :param color: Color of text.
    :param surface: Surface to render to.
    :param aa: Whether to render text with anti-aliasing.
    :param positionkwargs: Keyword arguments to position text, e.g. centerx=500/topright=(300, 200)
    """
    textsurf = font.render(text, aa, color, wraplength=surface.get_rect().width)
    cliprect = surface.get_rect().clip(textsurf.get_rect(**positionkwargs))
    clippedtextsurf = font.render(text, aa, color, wraplength=cliprect.width)
    surface.blit(clippedtextsurf, clippedtextsurf.get_rect(**positionkwargs))
