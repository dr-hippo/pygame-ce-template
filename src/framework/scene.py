"""Script containing scene base class and some subclasses."""

import pygame
from pygame import Rect, Vector2

pygame.init()


class Scene:
    """A screen/location in-game. Should be inherited from."""
    def __init__(self):
        self.dt = 0

    def update(self, dt: float):
        """
        Advances this scene by the given deltatime.

        :param dt: Time since last update, in seconds.
        """
        self.dt = dt

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
