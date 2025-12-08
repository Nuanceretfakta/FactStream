print("Learning AI – Day 12")

# Original liste
tal = [3, 7, 12, 20, 1]

# Funktion 1: gang alle tal med 2
def gange_med_to(lst):
    ny_liste = []
    for nummer in lst:
        ny_liste.append(nummer * 2)
    return ny_liste

# Funktion 2: filtrer alle tal større end 10
def filtrer_store_tal(lst):
    resultat = []
    for nummer in lst:
        if nummer > 10:
            resultat.append(nummer)
    return resultat

# Test funktionerne
dobbelt = gange_med_to(tal)
store_tal = filtrer_store_tal(tal)

print("Original liste:", tal)
print("Dobbelt liste:", dobbelt)
print("Store tal (>10):", store_tal)
