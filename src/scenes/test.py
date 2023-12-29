"""Test scene."""

import pygame

import src.config as cfg
import src.utilities as utils
from framework import Scene


class TestScene(Scene):
    def __init__(self):
        super().__init__()
        self.smallfont = utils.load_font("m6x11", size=16)
        self.font = utils.load_font("m6x11", size=48, align=pygame.FONT_LEFT, underline=True)
        self.img = utils.load_image("sample", filetype="jpg")
        self.sound = utils.load_sound("sample")

    def update(self):
        pass

    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.sound.play()

    def render(self, window):
        window.fill("aliceblue")
        window.blit(self.img, (0, 0))
        utils.render_text(f"Deltatime: {self.game.dt}",
                          self.smallfont, "black", window, bottomleft=(5, window.get_rect().bottom))
        utils.render_text("Hello world. This is a Pygame template by Dr.Hippo. Click to play a sound.",
                          self.font, "#666666", window, midleft=(220, window.get_rect().centery))
