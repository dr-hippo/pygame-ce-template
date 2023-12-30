"""Script containing scene base class and some subclasses."""

import pygame
from pygame import Rect, Vector2

pygame.init()


class Scene:
    """A screen/location in-game. Should be inherited from.
    Parameter 'game' only needs to be set if not using GameState.load_scene()
    """
    def __init__(self, game: 'GameState' = None):
        self.game = game

    def update(self):
        """Call this function every frame update."""
        pass

    def on_event(self, event: pygame.Event):
        """
        Handles an event.

        :param event: Event to be handled.
        """
        pass

    def render(self, window: pygame.Surface):
        """
        Draws this scene to the window.

        :param window: Window to render to.
        """
        pass
