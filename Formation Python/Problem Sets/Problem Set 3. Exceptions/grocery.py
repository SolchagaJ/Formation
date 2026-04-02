# L'utilisateur entre des objets jusqu'à Ctrl-Z
# Le programme renvoit la liste de courses en majuscule trié par ordre alphabétique avec la quantité avant chaque objet

def main():
    g = grocery()
    print_grocery(g)

# L'utilisateur entre sa liste de courses jusqu'à Ctrl-Z
def grocery():
    g = {}
    while True:
        try:
            item = input().upper()
        except EOFError:
            return g
        # Si l'objet est nouveau, l'ajoute dans le dictionnaire avec 1 en valeur
        # Si l'objet existe déjà, la valeur est incrémentée de 1 
        else:
            g[item] = g.get(item,0) + 1
    
# La liste de courses est affichée en majuscule par ordre alphabétique. La quantité est affichée devant chaque objet
def print_grocery(grocery):
    for item in sorted(grocery):
        print(f"{grocery[item]} {item}")

main()