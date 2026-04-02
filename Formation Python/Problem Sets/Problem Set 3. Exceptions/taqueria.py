# L'utilisateur fait sa demande jusqu'à taper Ctrl-d.
# A chaque étape le programme renvoie la somme dépensée
# L'exercice demande d'arrêter la commande avec Ctrl-d sur Linux et Ctrl-z sur Windows
# On arrête la commande en tapant End

def main():
    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    order(menu)

# L'utilisateur commande son menu
def order(menu):
    total = 0
    while True:
        try:
            item = input("Item: ").title()
        # Fin de la commande (ctrl-d sur Linux et ctrl-z sur Windows)
        except EOFError:
            print(f"Total: ${total}")
            break
        else:
            # Ajout l'objet à la commande
            if item in menu:
                total += menu[item]
                print(f"Total: ${total:.2f}")
main()