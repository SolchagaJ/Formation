# L'utilisateur entre un code et le programme renvoit l'emoji correspondant

import emoji

alias = input("Input: ")
print("Output: " + emoji.emojize(alias))