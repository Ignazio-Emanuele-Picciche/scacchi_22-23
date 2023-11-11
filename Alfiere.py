from Pezzo import Pezzo

class Alfiere(Pezzo):
    
    def __init__(self, colore, posizione=None):
        super().__init__(colore, posizione, 'Alfiere')
        self.graphic_rep = '\u2657' if self.colore == 'W' else '\u265D'

    def verifica_mossa(self, destinazione):
        super().verifica_mossa(destinazione)
        # if super().verifica_mossa(destinazione): # se el condizioni di base sono rispettate vai avanti

        
            

                
