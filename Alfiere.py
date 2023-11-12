from Pezzo import Pezzo
from Colore import Colore

class Alfiere(Pezzo):
    
    def __init__(self, colore, posizione=None):
        super().__init__(colore, posizione, 'Alfiere')
        self.graphic_rep = '\u2657' if self.colore == Colore.BIANCHI else '\u265D'

    def verifica_mossa(self, destinazione, colore_turno):
        
        if super().verifica_mossa(destinazione, colore_turno):
            # verifica che non ci siano pezzi tra la casella di partenza e quella di arrivo
           
            colonna_partenza = self.posizione[1]+1
            colonna_arrivo = destinazione[1]
            riga_partenza = ord(self.posizione[0])+1
            riga_arrivo = ord(destinazione[0])
            
            pos_possibili=[]

            if colonna_partenza-1 < colonna_arrivo and riga_partenza-1 < riga_arrivo: # Si sposta in basso a destra
                pos_possibili = list(zip(range(riga_partenza,  riga_arrivo+1), range(colonna_partenza, colonna_arrivo+1)))
            elif colonna_partenza-1 < colonna_arrivo and riga_partenza-1 > riga_arrivo: # Si sposta in alto a destra
                pos_possibili = list(zip(range(riga_partenza-2,  riga_arrivo-1, -1), range(colonna_partenza, colonna_arrivo+1)))
            elif colonna_partenza-1 > colonna_arrivo and riga_partenza-1 > riga_arrivo: # Si sposta in alto a sinistra
                pos_possibili = list(zip(range(riga_partenza-2,  riga_arrivo-1, -1), range(colonna_partenza-2, colonna_arrivo-1, -1)))
            elif colonna_partenza-1 > colonna_arrivo and riga_partenza-1 < riga_arrivo: # Si sposta in basso a sinistra
                pos_possibili = list(zip(range(riga_partenza,  riga_arrivo+1), range(colonna_partenza-2, colonna_arrivo-1, -1)))


            if (ord(destinazione[0]), destinazione[1]) in pos_possibili:
                for (row, col) in pos_possibili:
                    if not self.scacchiera.get_pezzo([chr(row), col]) == None and  not len(pos_possibili) == pos_possibili.index((row, col))+1:
                        print(f'La mossa non è legale perche è presente un pezzo {self.scacchiera.get_pezzo([chr(row), col]).nome} nella casella {chr(row)}{col}')
                        return False
            else:
                print(f'La destinazione scelta {destinazione[0]}{destinazione[1]} non rientra nelle regole per il movimento dell\'Alfiere')
                return False

            
            return True

        else:
            print(f'La mossa {self.posizione[0]}{self.posizione[1]}, {destinazione[0]}{destinazione[1]} non è legale per l\'Alfiere')
            return False

        
            

                
