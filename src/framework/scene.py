"""Script containing scene base class and some subclasses."""

import time

import pygame

pygame.init()


class Scene:
    """Superclass for in-game screens/locations."""
    def __init__(self):
        self.INIT_TIME = time.time()

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

    @property
    def time(self) -> float:
        """Time elapsed, in seconds, since this scene was loaded."""
        return time.time() - self.INIT_TIME
