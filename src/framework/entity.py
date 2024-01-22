"""In-game object in a scene, inheriting from pygame's sprite class."""

from typing import Sequence, Union

import pygame
from pygame import Vector2
from pygame.sprite import Sprite, Group

from src.framework import gamestate

pygame.init()


class Entity(Sprite):
    """Base class for a visible object in a scene."""
    def __init__(self, image: pygame.Surface,
                 position: Union[Vector2, Sequence[float]],
                 pivot: Union[str, Sequence[float]] = "center",
                 rotation: float = 0.0,
                 groups: Union[Group, Sequence[Group]] = ()):
        """Instantiate an entity."""
        super().__init__(*groups)
        self.scene = gamestate.current_scene
        self.image = image
        self.rect = self.image.get_rect()
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

        # Set rect to correct position
        self.rect.topleft = Vector2(self.position.x - self.pivot.x * self.rect.w,
                                    self.position.y - self.pivot.y * self.rect.h)

    def update(self):
        """Call this function every frame update."""
        pass

    def render(self, window):
        """
        Draws this object to the window.

        :param window: Window to render to.
        """
        pass
