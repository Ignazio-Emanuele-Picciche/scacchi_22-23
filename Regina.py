from Pezzo import Pezzo
from Colore import Colore

class Regina(Pezzo):

    def __init__(self, colore, posizione=None):
        super().__init__(colore, posizione, 'Regina')
        self.graphic_rep = '\u2655' if self.colore == Colore.BIANCHI else '\u265B'