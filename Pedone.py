from Pezzo import Pezzo

class Pedone(Pezzo):
    
    def __init__(self, colore, posizione=None):
        super().__init__(colore, posizione, 'Pedone')
        self.graphic_rep = '\u2659' if self.colore == 'W' else '\u265F'
        
        self.primo_passo=False

    def verifica_mossa(self, destinazione):

        mossa_valida = False
        
        row={'A':1, 
             'B':2,
             'C':3,
             'D':4,
             'E':5,
             'F':6,
             'G':7,
             'H':8}

        row_key = list(row.keys())

        if super().verifica_mossa(destinazione): # verifica base della mossa

            # il pedone puo andare solo in avanti (se è la prima mossa puo andare avanti anche di due caselle)
            # per mangiare invece puo farlo solo in daigonale
            if not self.primo_passo: 
                riga_iniziale = row[self.posizione[0]]
                riga_finale = row[destinazione[0]]

                row_diff = abs(riga_finale - riga_iniziale) # elimino il segno 

                if row_diff > 0:
                    # Gestisco lo spostamento in avanti
                    if (((row_diff == 2 and self.scacchiera.get_pezzo([row_key[row[destinazione[0]]+1], destinazione[1]])) == None) or row_diff == 1) \
                        and self.posizione[1] == destinazione[1] and self.scacchiera.get_pezzo(destinazione) == None:
                        mossa_valida = True
                        print('bravo')
                    # Gestisco lo spostamento in diagonale per mangiare
                    elif row_diff == 1 and (destinazione[1] == self.posizione[1]+1 or destinazione[1] == self.posizione[1]-1):
                        mossa_valida = True
                        print('bravo')
                    else:
                        print('che succede')

        
        return mossa_valida
                

    