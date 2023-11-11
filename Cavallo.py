from Pezzo import Pezzo

class Cavallo(Pezzo):

    def __init__(self, colore, posizione=None):
        super().__init__(colore, posizione, 'Cavallo')
        self.graphic_rep = '\u2658' if self.colore == 'W' else '\u265E'

        
    # def verifica_mossa(self, destinazione):

        # if super().verifica_mossa(destinazione): # Verifico la mossa di base

