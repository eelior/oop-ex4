import pygame


class Pokemon:
    def __init__(self, value: float, type: int, pos: tuple):
        self.value = value
        self.type = type
        self.pos = pos
        self.is_taken = False
        try:
            self.avatar_pikachu = pygame.image.load('client_python/sprites/pikachu.png')
            self.avatar_bulbasaur = pygame.image.load('client_python/sprites/bulbasaur.png')
        except:
            print("Loaded sprites")
            self.avatar_pikachu = pygame.image.load('sprites/pikachu.png')
            self.avatar_bulbasaur = pygame.image.load('sprites/bulbasaur.png')


    def __str__(self):
        return f'[value={self.value},type={self.type},pos={self.pos}]'

    def __repr__(self):
        return f'[value={self.value},type={self.type},pos={self.pos}]'
