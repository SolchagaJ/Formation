# Mettre des pièces dans la machine pour recevoir un Coca de 50 centimes
# La Machine n'accepte que les pièces de 25,10 et 5 centimes

amount_due = 50

while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    coin = int(input("Insert Coin: "))

    # La pièce doit être valide 
    if coin == 25 or coin == 10 or coin == 5:
        amount_due -= coin

# Affiche la monnaie rendue
print(f"Change Owed: {abs(amount_due)}")