"""Script containing scene base class and some subclasses."""

import pygame
from pygame import Rect, Vector2

pygame.init()


class Scene:
    """Superclass for in-game screens/locations."""
    def __init__(self):
        pass

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
