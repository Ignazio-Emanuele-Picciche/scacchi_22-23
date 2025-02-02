#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 10:42:39 2022

@author: iannello

"""

from Scacchiera import Scacchiera
from Pezzo import Pezzo
from Torre import Torre
from Regina import Regina
from Re import Re
from Alfiere import Alfiere
from Cavallo import Cavallo
from Pedone import Pedone


def in_board(posizione):
    """
    verifica che la posizione sia all'intgerno della scacchiera
    Parameters
    ----------
    posizione: coppia di coordinate

    Returns
    -------
    bool
        True se le coordinate corrispondono a una casella della
        scacchiera, False altrimenti
    """
    return posizione[0] in {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'} and \
           posizione[1] in range(1, 9)


def get_mossa():
    """
    acquisisce una mossa dallo standard input o termina il programma
    La mossa deve essere fornita nel formato:
        
        posizione_di_partenza posizione_di_destinazione
        
    dove una posizione è una coppia formata da una lettera
    in ['A', 'H'] e da una cifra in [1, 8]
    le due posizioni devono essere separate da un solo spazio

    se la lunghezza della stringa fornita in input è diversa
    da 5 il programma viene terminato

    Returns
    -------
    list
        posizione di partenza
    list
        posizione di destinazione

    """
    while True:
        mossa = input("Dammi la mossa: ")
        if not len(mossa) == 5:  # l'input non è una mossa
            print('La lunghezza della stringa non è valida')
            exit(0)              # termina il programma
        partenza = [mossa[0].upper(), int(mossa[1])]
        destinazione = [mossa[3].upper(), int(mossa[4])]
        if in_board(partenza) and in_board(destinazione):
            return partenza, destinazione
        else:
            print(f'La partenza e/o la destinazione della mossa {mossa} non corrispondono a caselle della scacchiera')


if __name__ == "__main__":
    # setup del gioco
    scacchiera = Scacchiera()
    
    # # posizione 4 pezzi bianchi nelle prime 4 righe della colonna A
    # for i in range(1, 5):
    #     p = Torre('W')
    #     scacchiera.metti(p, ['A', i])
    # # posizione 4 pezzi neri nelle prime 4 righe della colonna H
    # for i in range(1, 5):
    #     p = Torre('B')
    #     scacchiera.metti(p, ['H', i])


    # Metto i pedoni bianchi    
    for i in range(1,9):
        scacchiera.metti(Pedone('W'), ['B', i])

    # Metto tutti i pezzi bianchi
    scacchiera.metti(Torre('W'), ['A', 1])
    scacchiera.metti(Cavallo('W'), ['A', 2])
    scacchiera.metti(Alfiere('W'), ['A', 3])
    scacchiera.metti(Regina('W'), ['A', 4])
    scacchiera.metti(Re('W'), ['A', 5])
    scacchiera.metti(Alfiere('W'), ['A', 6])
    scacchiera.metti(Cavallo('W'), ['A', 7])
    scacchiera.metti(Torre('W'), ['A', 8])



    # Metto i pedoni neri    
    for i in range(1,9):
        scacchiera.metti(Pedone('B'), ['G', i])

    # Metto tutti i pezzi neri
    scacchiera.metti(Torre('B'), ['H', 1])
    scacchiera.metti(Cavallo('B'), ['H', 2])
    scacchiera.metti(Alfiere('B'), ['H', 3])
    scacchiera.metti(Regina('B'), ['H', 4])
    scacchiera.metti(Re('B'), ['H', 5])
    scacchiera.metti(Alfiere('B'), ['H', 6])
    scacchiera.metti(Cavallo('B'), ['H', 7])
    scacchiera.metti(Torre('B'), ['H', 8])


    scacchiera.visualizza()
    print()

    # inizia il gioco
    while True:
        while True:
            # acquisisce mossa da fare
            (partenza, destinazione) = get_mossa()
            # recupera il pezzo da muovere
            pezzo = scacchiera.get_pezzo(partenza)
            # muovi il pezzo sulla scacchiera
            if pezzo.verifica_mossa(destinazione):  # la mossa è legale
                break
        # esegui mossa sulla scacchiera
        if not scacchiera.get_pezzo(destinazione) is None:  # la casella è occupata
            scacchiera.togli(destinazione)  # "mangia" il pezzo che occupa la casella
        scacchiera.togli(partenza)
        scacchiera.metti(pezzo, destinazione)

        scacchiera.visualizza()
        print()

