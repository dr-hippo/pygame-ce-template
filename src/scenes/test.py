"""Test scene."""

from typing import Optional

import pygame

import src.utilities as utils
from src.framework import Scene, gamestate, Entity

pygame.init()


class TestScene(Scene):
    def __init__(self):
        super().__init__()
        self.smallfont = utils.load_font("m6x11", size=16)
        self.font = utils.load_font("m6x11", size=48, align=pygame.FONT_LEFT, underline=True)
        self.img = utils.load_image("sample", filetype="jpg")
        self.sound = utils.load_sound("sample")
        self.last_click_pos: Optional[pygame.Vector2] = None
        self.test_ent = Entity(utils.load_image("testent"), (50, 50))
        self.debug_info = ""

    def update(self):
        self.debug_info = "Click position: {}\nDeltatime: {}s\nTotal time: {:.1f}s".format(
            self.last_click_pos,
            gamestate.Time.get_dt(),
            self.time
        )

    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.sound.play()
            self.last_click_pos = event.pos

    def render(self, window):
        window.fill("aliceblue")
        window.blit(self.img, pygame.Vector2(0, 0))
        utils.render_text(self.debug_info, self.smallfont, "black", window, bottomleft=(5, window.get_rect().bottom))
        utils.render_text("Hello world. This is a Pygame template by Dr.Hippo. Click to play a sound.",
                          self.font, "#666666", window, midleft=(220, window.get_rect().centery))
