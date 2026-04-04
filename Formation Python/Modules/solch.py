# Module regroupant mes fonctions utiles 

import random
import sys

def main():
    pass

# L'utilisateur entre une valeur, le programme redemande tant que ce n'est pas un entier strictement positif
def int_strict_positive_input(prompt=""):
    while True:
        try:
            # Entre un niveau de difficulté
            n = int(input(prompt))
        # Tant que le niveau n'est pas un entier, le programme nous redemande
        except ValueError:
            continue
        else:
            # Si l'entier est négatif ou nul, le programme nous redemande
            if n < 1:
                continue
            return n

# L'utilisateur entre une valeur, le programme redemande tant que ce n'est pas un entier positif ou nul
def int_positive_input(prompt=""):
    while True:
        try:
            # Entre un niveau de difficulté
            n = int(input(prompt))
        # Tant que le niveau n'est pas un entier, le programme nous redemande
        except ValueError:
            continue
        else:
            # Si l'entier est négatif ou nul, le programme nous redemande
            if n < 0:
                continue
            return n
        
if __name__ == "__main__":
    main()