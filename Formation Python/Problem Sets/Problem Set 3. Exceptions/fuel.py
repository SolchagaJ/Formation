# L'utilisateur entre une fraction sous la forme x/y
# Le programme revoie x/y sous forme de pourcentage, E si < 1% et F si > 99%

def main():
    f = get_percent("Fraction: ")
    print(fuel_remaining(f))

# L'utilisateur entre une fonction sous la forme x/y. Le programme redemande jusqu'à une réponse valide
def get_percent(prompt=""):
    while True:
        try:
            x,y = input(prompt).split("/")
            x,y = int(x),int(y)
            value = (x/y) * 100
        # x et y doivent être des entiers et y ne doit pas être 0
        except (ValueError,ZeroDivisionError):
            pass
        else:
            # x doit êre positif et plus petit que y
            if 0 <= x <= y :
                return round(value)

                
# Affiche la quantité de fuel restante en pourcentage, E si <1% et F si >99%
def fuel_remaining(value):
    if 99 <= value:
        return "F"
    elif value <= 1:
        return "E"
    else:
        return f"{value}%"

main()