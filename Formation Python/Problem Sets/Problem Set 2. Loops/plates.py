# Déterminer si une plaque d'immatriculation est valide ou non
# Doit commencer par 2 lettres
# Doit contenir entre 2 et 6 caractères
# Pas de chiffres au milieu, le premier chiffre ne peut pas être 0
# Pas d'espaces ou de ponctuation

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# Déterminer si une plaque d'immatriculation est valide ou non
def is_valid(s):
    if good_range(s):
        if good_beginning(s):
            if first_digit(s):
                if good_digits_placement(s):
                    if no_space_no_punct(s):
                        return True
    return False

# Doit contenir entre 2 et 6 caractères
def good_range(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False

# Doit commencer par 2 lettres
def good_beginning(s):
    for i in range(2):
        if not s[i].isalpha():
            return False
    return True

# Le premier chiffre ne peut pas être 0
def first_digit(s):
    for carac in s:
        if carac.isdigit():
            if int(carac) == 0:
                return False
            else:
                return True       
    return True # Renvoie True si aucun chiffre


# Pas de chiffres au milieu, le premier chiffre ne peut pas être 0
def good_digits_placement(s):
    # On continue tant qu'on ne tombe pas sur un chiffre
    for i in range(len(s)):
        # Dès qu'on trouve un chiffre, les autres caractères doivent être des chiffres
        if s[i].isdigit():
            for i in range(i+1,len(s)):
                if not s[i].isdigit():
                    return False
            return True
    return True # Renvoie True si aucun chiffre
                
# Pas d'espaces ou de ponctuation
def no_space_no_punct(s):
    for carac in s:
        if not carac.isalnum():
            return False
    return True

main()