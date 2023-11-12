from Pezzo import Pezzo
from Colore import Colore

class Re(Pezzo):

    def __init__(self, colore, posizione=None):
        super().__init__(colore, posizione, 'Re')
        self.graphic_rep = '\u2654' if self.colore == Colore.BIANCHI else '\u265A'