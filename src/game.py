"""Main game."""

import sys
import platform
import ctypes
import asyncio

import pygame

# Some code won't work if old pygame is used instead of pygame-ce
if not hasattr(pygame, "IS_CE"):
    raise ImportError("Pygame Community Edition (pygame-ce) is required to run this game.")

import src.config as cfg
import src.utilities as utils

from framework import gamestate


# If in executable bundle with splash screen, close it when starting up
try:
    import pyi_splash
    pyi_splash.close()

except ImportError:
    pass

# Try to prevent display stretching if on Windows, if it doesn't work no big deal
if platform.system().lower() == "windows":
    try:
        ctypes.windll.user32.SetProcessDPIAware()

    except OSError:
        pass

# Initialisation
pygame.init()


# Some systems don't allow changing window title/icon after set_mode, so set these before that
pygame.display.set_caption(f"{cfg.APPNAME} - {cfg.AUTHOR}")

if cfg.ICON_FILENAME:
    icon_img = pygame.image.load(utils.to_path(cfg.ASSET_PATH, cfg.IMAGE_PATH, cfg.ICON_FILENAME))
    pygame.display.set_icon(icon_img)

display_flags = pygame.SCALED if sys.platform == "emscripten" else pygame.RESIZABLE | pygame.SCALED
window = pygame.display.set_mode(cfg.RESOLUTION, display_flags)
clock = pygame.time.Clock()


async def main():
    """Main game function."""
    global window, clock

    gamestate.init()

    # Event/update/render loop
    while True:
        for event in pygame.event.get(pygame.QUIT):
            pygame.quit()
            return

        for event in pygame.event.get():
            gamestate.current_scene.on_event(event)

        gamestate.current_scene.update()
        pygame.display.update()
        gamestate.current_scene.render(window)

        if cfg.SHOW_FPS:
            pygame.display.set_caption(f"{cfg.APPNAME} - {cfg.AUTHOR} - FPS: {round(clock.get_fps(), 1)}")

        await asyncio.sleep(0)
        gamestate.Time.unscaled_dt = clock.tick(cfg.TARGET_FPS) / 1000


if __name__ == "__main__":
    asyncio.run(main())
