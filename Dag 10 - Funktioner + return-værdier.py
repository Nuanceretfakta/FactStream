print("Learning AI – Day 10")

# Funktion der lægger to tal sammen
def læg_sammen(a, b):
    return a + b

# Kald funktionen 3 gange
resultat1 = læg_sammen(3, 5)
resultat2 = læg_sammen(10, 20)
resultat3 = læg_sammen(7, 13)

print("Resultat 1:", resultat1)
print("Resultat 2:", resultat2)
print("Resultat 3:", resultat3)

print()  # tom linje

# Funktion der giver en hilsen
def hilsen(navn):
    return "Hej, " + navn + ", velkommen til min Python-journey!"

# Print hilsen
tekst = hilsen("AleGS")
print(tekst)
