#L'utilisateur entre une expression sous la forme x y z
# x et z sont des entiers
# y est le symbole +, -, * ou /
x,y,z = input("Expression: ").split()
#Convertir x et z en entier
x,z = int(x),int(z)
#Affiche le résultat en float avec un chiffre après la virgule
if y == "+":
    print(float(round((x+z),1)))
elif y == "-":
    print(float(round((x-z),1)))
elif y == "*":
    print(float(round((x*z),1)))
else:
    print(float(round((x/z),1)))