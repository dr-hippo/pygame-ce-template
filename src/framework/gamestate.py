import pygame

from src.framework import Scene, GameObject


class GameState:
    def __init__(self, starting_scene: Scene):
        """
        Object encapsulating global game state.

        :param starting_scene: Scene to load on game start.
        """
        self.unscaled_dt = 0
        self.timescale = 1
        self.current_scene = starting_scene
        self.player_data = None
        self.player_settings = None

        self.reload_scene()

    @property
    def dt(self):
        return self.unscaled_dt * self.timescale

    def load_scene(self, scene: Scene):
        self.current_scene = scene
        self.current_scene.game = self

    def reload_scene(self):
        self.load_scene(type(self.current_scene)())
