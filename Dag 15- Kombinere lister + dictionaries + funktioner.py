print("Learning AI – Day 15")

# Liste med opgaver (database)
opgaver = [
    {"id": 1, "navn": "Skriv rapport", "status": "åben"},
    {"id": 2, "navn": "Send email", "status": "i gang"},
    {"id": 3, "navn": "Lav analyse", "status": "åben"},
    {"id": 4, "navn": "Forbered møde", "status": "færdig"}
]

# Funktion 1: find åbne opgaver
def find_åbne_opgaver(opgaver):
    resultat = []
    for opg in opgaver:
        if opg["status"] == "åben":
            resultat.append(opg)
    return resultat

# Funktion 2: ændr status på en opgave via ID
def ændr_status(opgaver, id, ny_status):
    for opg in opgaver:
        if opg["id"] == id:
            opg["status"] = ny_status
            return opgaver
    return opgaver  # hvis ID ikke findes

# Test 1: print åbne opgaver
print("Åbne opgaver før:")
print(find_åbne_opgaver(opgaver))

print()

# Test 2: ændr status på opgave 1
ændr_status(opgaver, 1, "færdig")

# Test 3: print åbne opgaver efter
print("Åbne opgaver efter ændring:")
print(find_åbne_opgaver(opgaver))
