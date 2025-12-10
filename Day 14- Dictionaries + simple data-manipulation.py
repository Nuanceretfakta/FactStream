print("Learning AI – Day 14")

# Liste med produkter
produkter = [
    {"navn": "Laptop", "pris": 8500, "kategori": "Elektronik"},
    {"navn": "Høretelefoner", "pris": 1200, "kategori": "Lyd"},
    {"navn": "Mus", "pris": 300, "kategori": "Elektronik"}
]

# Funktion 1 – find dyre produkter
def find_dyre_produkter(produkter, grænse):
    resultat = []
    for p in produkter:
        if p["pris"] > grænse:
            resultat.append(p)
    return resultat

# Funktion 2 – gennemsnitspris
def beregn_gennemsnitspris(produkter):
    total = 0
    for p in produkter:
        total += p["pris"]
    return total / len(produkter)

# Kør funktionerne
dyre = find_dyre_produkter(produkter, 1000)
gennemsnit = beregn_gennemsnitspris(produkter)

# Print resultater
print("Dyre produkter (>1000):", dyre)
print("Gennemsnitspris:", gennemsnit)
