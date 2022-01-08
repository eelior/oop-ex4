import pygame


class Agent:
    def __init__(self, id1: int, value: float, src: int, dest: int, speed: float, pos: tuple):
        self.id = id1
        self.value = value
        self.src = src
        self.dest = dest
        self.lastDest = 0
        self.speed = speed
        self.pos = pos
        self.orders = []
        try:
            self.avatar = pygame.image.load('/client_python/sprites/ash_katchum.png')
        except:
            self.avatar = pygame.image.load('client_python/sprites/ash_katchum.png')

        self.nextPositions = []

    def __str__(self):
        return f'[id={self.id},value={self.value},src={self.src},dest={self.dest},speed={self.speed},pos={self.pos}]'

    def __repr__(self):
        return f'[id={self.id},value={self.value},src={self.src},dest={self.dest},speed={self.speed},pos={self.pos}]'
