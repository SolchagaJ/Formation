# L'utilisateur ouvre le fichier via le terminal avec 0 ou 2 commandes supplémentaires
# L'utilisateur entre un message
# Si 0 commandes, le programme renvoit le message avec un font aléatoire
# Si 2 mauvaises commandes, le programme exit avec message d'erreur
# Si 2 bonnes commandes, le programme renvoit le message avec le font indiqué


from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
# Renvoit une erreur si le nombre de commandes n'est pas bon
if len(sys.argv) == 2 or len(sys.argv) > 3:
    sys.exit("Invalid usage")

#Renvoit une erreur si on entre 2 mauvaises commandes
elif len(sys.argv) == 3 and ((sys.argv[1] != "-f" and sys.argv[1] != "--font") or sys.argv[2] not in figlet.getFonts()):
    sys.exit("Invalid usage")

# Il n'y a plus d'erreur, je peux taper mon message
else:
    message = input("Input: ")
    # Si je n'entre aucune commande, le font est aléatoire
    if len(sys.argv) == 1:
        font = random.choice(figlet.getFonts())
    # Si j'entre 2 commandes, le font est spécifié
    else:
        font = sys.argv[2]

    figlet.setFont(font = font)
    print("Output: " + figlet.renderText(message))