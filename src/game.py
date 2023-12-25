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

# Try to prevent display stretching if on Windows, if it doesn't work no big deal
if platform.system().lower() == "windows":
    try:
        ctypes.windll.user32.SetProcessDPIAware()

    except OSError:
        pass

# Initialisation
pygame.init()
pygame.display.set_caption(f"{cfg.APPNAME} - {cfg.AUTHOR}")
if cfg.ICON_FILENAME:
    pygame.display.set_icon(pygame.image.load(utils.to_path(cfg.ASSET_PATH, cfg.IMAGE_PATH, cfg.ICON_FILENAME)))
display_flags = pygame.SCALED if sys.platform == "emscripten" else pygame.RESIZABLE | pygame.SCALED
window = pygame.display.set_mode(cfg.RESOLUTION, display_flags)
clock = pygame.time.Clock()


async def main():
    """Main game function."""
    global window, clock
    smallfont = utils.load_font("m6x11", size=16)
    font = utils.load_font("m6x11", size=48, align=pygame.FONT_LEFT, underline=True)
    img = utils.load_image("sample", filetype="jpg")
    # sound = utils.load_sound("sample")
    # sound.play(loops=4)

    # Event/update/render loop
    while True:
        for event in pygame.event.get(pygame.QUIT):
            pygame.quit()
            return

        pygame.event.get()

        window.fill("aliceblue")
        window.blit(img, (0, 0))
        utils.render_text(f"FPS: {round(clock.get_fps(), 1)}",
                          smallfont, "black", window, bottomleft=(5, window.get_rect().bottom))
        utils.render_text("Hello world. This is a Pygame template made by Dr.Hippo.",
                          font, "#666666", window, midleft=(220, window.get_rect().centery))
        pygame.display.update()
        await asyncio.sleep(0)
        clock.tick(cfg.TARGET_FPS)


if __name__ == "__main__":
    asyncio.run(main())
