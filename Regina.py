from Pezzo import Pezzo

class Regina(Pezzo):

    def __init__(self, colore, posizione=None):
        super().__init__(colore, posizione, 'Regina')
        self.graphic_rep = '\u2655' if self.colore == 'W' else '\u265B'