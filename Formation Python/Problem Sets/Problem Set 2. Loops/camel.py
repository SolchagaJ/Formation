# Transformer un nom sous la forme camel case en forme snake case (i.e firstName devient first_name)
name = input("camelCase: " )
for letter in name:
    if letter.islower():
        print(letter,end="")
    else:
        print("_" + letter.lower(),end="")