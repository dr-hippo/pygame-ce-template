"""Script containing scene base class and some subclasses."""

import time

import pygame
from pygame import Rect, Vector2

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

    def spawn(self, entity_type: type['Entity'], *args, **kwargs) -> 'Entity':
        """Instantiate a new entity of entity_type with the specified positional and keyword arguments."""
        entity = entity_type(*args, **kwargs)
        entity.scene = self
        return entity
