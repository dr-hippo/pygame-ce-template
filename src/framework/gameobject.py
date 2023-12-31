"""In-game object in a scene, inheriting from pygame's sprite class."""

from typing import Sequence, Union

import pygame
from pygame import Rect, Vector2
from pygame.sprite import Sprite, Group

from framework.scene import Scene

pygame.init()


class GameObject(Sprite):
    """Base class for a visible object in a scene."""
    def __init__(self, image_path: str,
                 position: Union[Vector2, Sequence[float]],
                 pivot: Union[str, Sequence[float]] = "center",
                 rotation: float = 0.0,
                 scene: Scene = None, groups: Union[Group, Sequence[Group]] = ()):
        super().__init__(*groups)
        self.scene = scene
        # self.image =
        # self.rect =
        self.position = Vector2(position)

    def update(self):
        """Call this function every frame update."""
        pass

    def render(self, window):
        """
        Draws this object to the window.

        :param window: Window to render to.
        """
        pass
