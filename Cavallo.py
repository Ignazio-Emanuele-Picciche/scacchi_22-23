from Pezzo import Pezzo
from Colore import Colore

class Cavallo(Pezzo):

    def __init__(self, colore, posizione=None):
        super().__init__(colore, posizione, 'Cavallo')
        self.graphic_rep = '\u2658' if self.colore == Colore.BIANCHI else '\u265E'
        self.colore = colore

        
    def verifica_mossa(self, destinazione, colore_turno):
        if super().verifica_mossa(destinazione): # Verifico la mossa di base
            # prendo la posizione del cavallo come centro asse, e da li mi calcolo e creo un vettore
            # con le sue posizioni possibili 

            dest_poss=[]

            # mi calcolo le posizioni possibili
            print(self.scacchiera.get_pezzo(self.posizione).posizione)



            

