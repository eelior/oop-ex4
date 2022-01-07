class Agent:
    def __init__(self, id1: int, value: float, src: int, dest: int, speed: float, pos: tuple):
        self.id = id1
        self.value = value
        self.src = src
        self.dest = dest
        self.speed = speed
        self.pos = pos

        self.nextPositions = []

    def __str__(self):
        return f'[id={self.id},value={self.value},src={self.src},dest={self.dest},speed={self.speed},pos={self.pos}]'

    def __repr__(self):
        return f'[id={self.id},value={self.value},src={self.src},dest={self.dest},speed={self.speed},pos={self.pos}]'
