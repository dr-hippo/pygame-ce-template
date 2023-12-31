"""Global mutable state of the game. Developer settings fixed at runtime go in src/config.py."""

import pygame

from src.framework import Scene, GameObject
import src.config as cfg


class Time:
    unscaled_dt = 0  # In seconds
    timescale = 1

    @classmethod
    @property
    def dt(cls) -> float:
        """Time elapsed, in seconds, since last frame update."""
        return cls.unscaled_dt * cls.timescale


current_scene: Scene = None
player_data = None
player_settings = None


def init():
    """Initialises the game's internal state."""
    global current_scene
    current_scene = cfg.STARTING_SCENE()
