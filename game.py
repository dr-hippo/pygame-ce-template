"""Main game."""

import pygame

# Some code won't work if old pygame is used instead of pygame-ce
if not hasattr(pygame, "IS_CE"):
    raise ImportError("Pygame Community Edition (pygame-ce) is required to run this game.")

import sys
import ctypes

import config as cfg
import utilities as utils


def main():
    """Main game function."""
    # Try to prevent display stretching if on Windows, if it doesn't work no big deal
    try:
        ctypes.windll.user32.SetProcessDPIAware()

    except OSError:
        pass

    # Initialisation
    pygame.init()

    pygame.display.set_caption(f"{cfg.APPNAME} - {cfg.AUTHOR}")
    window = pygame.display.set_mode(cfg.RESOLUTION, pygame.SCALED | pygame.RESIZABLE)
    clock = pygame.time.Clock()
    img = utils.load_image("sample", filetype="jpg")
    sound = utils.load_sound("sample")
    sound.play(loops=4)

    font = utils.load_font("m6x11", size=48, align=pygame.FONT_RIGHT, underline=True)

    # Event/update/render loop
    while True:
        for event in pygame.event.get(pygame.QUIT):
            pygame.quit()
            sys.exit()

        pygame.event.get()

        window.fill("white")
        window.blit(img, (0, 0))
        window.blit(
            font.render("Hello world\nThis is a\nPygame Template", True, "yellow"),
            (10, 25)
        )
        pygame.display.update()
        clock.tick(cfg.TARGET_FPS)


if __name__ == "__main__":
    main()
