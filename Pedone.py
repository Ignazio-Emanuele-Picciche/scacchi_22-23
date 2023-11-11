from Pezzo import Pezzo

class Pedone(Pezzo):

    def __init__(self, colore, posizione=None):
        super().__init__(colore, posizione, 'Pedone')
        self.graphic_rep = '\u2659' if self.colore == 'W' else '\u265F'