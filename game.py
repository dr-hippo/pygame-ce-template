"""Main game."""

import pygame

# Some code won't work if old pygame is used instead of pygame-ce
if not hasattr(pygame, "IS_CE"):
    raise ImportError("Pygame Community Edition (pygame-ce) is required to run this game.")

import sys
import ctypes

import config as cfg


def main():
    """Main game function."""
    # Try to prevent display stretching if on Windows, if it doesn't work no big deal
    try:
        ctypes.windll.user32.SetProcessDPIAware()

    except OSError:
        pass

    # Initialisation
    pygame.init()

    pygame.display.set_caption(cfg.TITLE)
    window = pygame.display.set_mode(cfg.RESOLUTION, pygame.SCALED | pygame.FULLSCREEN)
    clock = pygame.time.Clock()

    font = pygame.font.SysFont("consolas", 40, italic=True)
    font.align = pygame.FONT_RIGHT

    # Event/update/render loop
    while True:
        for event in pygame.event.get(pygame.QUIT):
            pygame.quit()
            sys.exit()

        pygame.event.get()

        window.fill("white")
        window.blit(
            font.render("Hello world\nThis is a\nPygame Template", True, "black"),
            (10, 25)
        )
        pygame.display.update()
        clock.tick(cfg.TARGET_FPS)


if __name__ == "__main__":
    main()
