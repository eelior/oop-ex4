import sys

import pygame


class Pokemon:
    def __init__(self, value: float, type: int, pos: tuple):
        self.value = value
        self.type = type
        self.pos = pos
        # self.id = id
        self.is_taken = False
        try:
            self.avatar_charmander = pygame.image.load("game/sprites/charmander.png")
            self.avatar_bulbasaur = pygame.image.load("game/sprites/bulbasaur.png")
        except:
            self.avatar_charmander = pygame.image.load("../game/sprites/charmander.png")
            self.avatar_bulbasaur = pygame.image.load("../game/sprites/bulbasaur.png")

    def __str__(self):
        return f"[value={self.value},type={self.type},pos={self.pos}]"

    def __repr__(self):
        return f"[value={self.value},type={self.type},pos={self.pos}]"

    def is_equal(self,other) -> bool:
        if abs(self.pos[0]-other.pos[0]) < sys.float_info.epsilon and \
                abs(self.pos[1]-other.pos[1]) < sys.float_info.epsilon:
            return True
        return False