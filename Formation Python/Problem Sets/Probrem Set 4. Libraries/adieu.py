# L'utilisateur entre un nom par ligne jusqu'à Ctrl-Z
# Le programme affiche  "Adieu, adieu, to" et énumère tous les noms

import inflect

p = inflect.engine()
names = []

# Je continue de lister des noms tant que je ne tape pas Ctrl-Z
while True:
    try:
        names.append(input("Name: ").title())
    # J'ai tapé Ctrl-Z, j'affiche le résultat, (amélioration : je continue tant que je n'ai rentré aucun nom)
    except EOFError:
        if len(names) > 0:
            print("Adieu, adieu, to " + p.join(names))
            break