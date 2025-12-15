print("Learning AI – Day 18")

tekst = "AI og automatisering er fremtiden for administrativt arbejde"

def tekst_analyse(tekst):
    ord_liste = tekst.split()
    antal_ord = len(ord_liste)
    antal_bogstaver = len(tekst.replace(" ", ""))

    return {
        "ord": antal_ord,
        "bogstaver": antal_bogstaver
    }

resultat = tekst_analyse(tekst)

print(f"Antal ord: {resultat['ord']}")
print(f"Antal bogstaver: {resultat['bogstaver']}")

# Ekstra (valgfrit)
if "AI" in tekst:
    print("Teksten indeholder ordet 'AI'")
else:
    print("Teksten indeholder ikke ordet 'AI'")
