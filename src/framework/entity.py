"""In-game object in a scene, inheriting from pygame's sprite class."""

from typing import Sequence, Union

import pygame
from pygame import Rect, Vector2
from pygame.sprite import Sprite, Group

from framework.scene import Scene
import src.utilities as utils

pygame.init()


class Entity(Sprite):
    """Base class for a visible object in a scene."""
    def __init__(self, image_path: str,
                 position: Union[Vector2, Sequence[float]],
                 pivot: Union[str, Sequence[float]] = "center",
                 rotation: float = 0.0,
                 scene: Scene = None, groups: Union[Group, Sequence[Group]] = ()):
        """Instantiate an entity. Scene only need to be set if not using Scene.spawn()."""
        super().__init__(*groups)
        self.scene = scene
        # self.image =
        # self.rect =
        self.position = Vector2(position)

        self._pivot_dict = {
            "topleft": (0, 0),
            "midtop": (0.5, 0),
            "topright": (1, 0),
            "midleft": (0, 0.5),
            "center": (0.5, 0.5),
            "midright": (1, 0.5),
            "bottomleft": (0, 1),
            "midbottom": (0.5, 1),
            "bottomright": (1, 1),
        }
        self.pivot = Vector2(self._pivot_dict[pivot] if type(pivot) == str else pivot)

    def update(self):
        """Call this function every frame update."""
        pass

    def render(self, window):
        """
        Draws this object to the window.

        :param window: Window to render to.
        """
        pass
