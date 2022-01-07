class Pokemon:
    def __init__(self, value: float, type: int, pos: tuple):
        self.value = value
        self.type = type
        self.pos = pos

    def __str__(self):
        return f'[value={self.value},type={self.type},pos={self.pos}]'

    def __repr__(self):
        return f'[value={self.value},type={self.type},pos={self.pos}]'
