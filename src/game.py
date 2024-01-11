"""Main game script with initialisation code and main loop."""

import asyncio
import ctypes
import platform
import sys

import pygame

# Some code won't work if old pygame is used instead of pygame-ce
if not hasattr(pygame, "IS_CE"):
    raise ImportError("Pygame Community Edition (pygame-ce) is required to run this game.")

import src.config as cfg
import src.utilities as utils

from src.framework import gamestate


# If in executable bundle with splash screen, close it when starting up
try:
    # noinspection PyUnresolvedReferences
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

# Some operating systems don't allow changing the window's caption/icon, so set them before calling set_mode()
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
        gamestate.current_scene.render(window)
        pygame.display.update()

        if cfg.SHOW_FPS and sys.platform != "emscripten":
            pygame.display.set_caption(f"{cfg.APPNAME} - {cfg.AUTHOR} - FPS: {round(clock.get_fps(), 1)}")

        await asyncio.sleep(0)
        gamestate.Time.unscaled_dt = clock.tick(cfg.TARGET_FPS) / 1000


if __name__ == "__main__":
    asyncio.run(main())
