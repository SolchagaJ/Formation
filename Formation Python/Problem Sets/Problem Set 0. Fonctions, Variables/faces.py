def main():
    texte = input()
    print(convert(texte))
# Convertisseur d'emoji
def convert(texte):
    return texte.replace(":)","🙂").replace(":(","🙁")

main()