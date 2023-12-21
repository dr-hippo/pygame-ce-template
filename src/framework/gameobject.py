"""In-game object in a scene, inheriting from pygame's sprite class."""

from typing import Sequence, Union

import pygame
from pygame import Rect, Vector2
from pygame.sprite import Sprite, Group

from framework.scene import Scene

pygame.init()


class GameObject(Sprite):
    """Base class for a visible object in a scene."""
    def __init__(self, scene: Scene, groups: Union[Group, Sequence[Group]] = ()):
        super().__init__(*groups)
        self.scene = scene
        self.dt = 0

    def update(self, dt: float):
        """
        Advances this gameobject by the given deltatime.

        :param dt: Time since last update, in seconds.
        """
        self.dt = dt

    def render(self, window):
        """
        Draws this object to the window.

        :param window: Window to render to.
        """
        pass
