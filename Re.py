from Pezzo import Pezzo

class Re(Pezzo):

    def __init__(self, colore, posizione=None):
        super().__init__(colore, posizione, 'Re')
        self.graphic_rep = '\u2654' if self.colore == 'W' else '\u265A'