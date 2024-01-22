"""Global mutable state of the game. Developer settings fixed at runtime go in src/config.py."""

import src.config as cfg
from src.framework.playerdata import PlayerData
from src.framework.playersettings import PlayerSettings

current_scene = None
player_data = PlayerData()
player_settings = PlayerSettings()


class Time:
    """Static wrapper class for time functions/variables. Time is counted in seconds (unlike in pygame-ce)."""
    unscaled_dt = 0
    timescale = 1

    @classmethod
    def get_dt(cls) -> float:
        """Time elapsed, in seconds, since last frame update."""
        return cls.unscaled_dt * cls.timescale


def init():
    """Initialises the game's internal state. Must be called after initialising Pygame."""
    global current_scene
    current_scene = cfg.STARTING_SCENE()
