import pygame


class Pokemon:
    def __init__(self, value: float, type: int, pos: tuple):
        self.value = value
        self.type = type
        self.pos = pos
        self.avatar_pikachu = pygame.image.load('client_python/pikachu.png')
        self.avatar_bulbasaur = pygame.image.load('client_python/bulbasaur.png')


    def __str__(self):
        return f'[value={self.value},type={self.type},pos={self.pos}]'

    def __repr__(self):
        return f'[value={self.value},type={self.type},pos={self.pos}]'
