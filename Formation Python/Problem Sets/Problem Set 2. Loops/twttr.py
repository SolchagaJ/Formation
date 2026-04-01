# On veut supprimer les voyelles d'un texte
def main():
    text = input("Input: ")
    for letter in text:
        # je n'affiche que les consonnes
        if not isvowel(letter):
            print(letter,end="")

# Vérifie si un caractère est une voyelle
def isvowel(letter):
    if letter.lower() in "aeiou":
        return True
    else:
        return False

main()