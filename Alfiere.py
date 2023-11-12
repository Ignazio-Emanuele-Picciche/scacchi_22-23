from Pezzo import Pezzo
from Colore import Colore

class Alfiere(Pezzo):
    
    def __init__(self, colore, posizione=None):
        super().__init__(colore, posizione, 'Alfiere')
        self.graphic_rep = '\u2657' if self.colore == Colore.BIANCHI else '\u265D'

    def verifica_mossa(self, destinazione, colore_turno):
        super().verifica_mossa(destinazione, colore_turno)
        # if super().verifica_mossa(destinazione): # se el condizioni di base sono rispettate vai avanti

        
            

                
