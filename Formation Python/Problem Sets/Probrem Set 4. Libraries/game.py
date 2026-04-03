# L'utilisateur entre un niveau de difficulté n. Un nombre aléatoire entre 1 et n est généré. L'utilisateur doit deviner ce nombre.
import random
import sys

def main():
    n = int_positive_input("Level: ")
    if n > 0:
        game(n)

# Le programme génère un nombre aléatoire entre 1 et le niveau tapé par l'utilisateur précédemment
# On tape un nombre jusqu'à trouver la bonne valeur. Le jeu nous dit s'il est plus grand ou plus petit. Si on ne tape pas un entier, le programme nous redemande
# Le programme s'arrête dès qu'on trouve
def game(n):
    answer = random.randint(1,n)
    while True:
        guess = int_positive_input("Guess: ")
        if guess < answer:
            print("Too Small!")
        elif guess > answer:
            print("Too large!")
        else:
            print("Just right!")
            sys.exit()


# L'utilisateur entre une valeur, le programme redemande tant que ce n'est pas un entier positif
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
            if n < 1:
                continue
            return n

main()