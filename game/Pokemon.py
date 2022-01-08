import pygame


class Pokemon:
    def __init__(self, value: float, type: int, pos: tuple):
        self.value = value
        self.type = type
        self.pos = pos
        # self.id = id
        self.is_taken = False
        try:
            self.avatar_pikachu = pygame.image.load('game/sprites/pikachu.png')
            self.avatar_bulbasaur = pygame.image.load('game/sprites/bulbasaur.png')
        except:
            self.avatar_pikachu = pygame.image.load('../game/sprites/pikachu.png')
            self.avatar_bulbasaur = pygame.image.load('../game/sprites/bulbasaur.png')

    def __str__(self):
        return f'[value={self.value},type={self.type},pos={self.pos}]'

    def __repr__(self):
        return f'[value={self.value},type={self.type},pos={self.pos}]'
