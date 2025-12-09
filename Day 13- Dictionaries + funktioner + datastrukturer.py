print("Learning AI – Day 13")

# Enkelt dictionary
person = {
    "navn": "AleGS",
    "alder": 27,
    "by": "København"
}

# Print pænt
print("Navn:", person["navn"])
print("Alder:", person["alder"])
print("By:", person["by"])

print()

# Funktion der opdaterer alder
def opdater_alder(person_dict, ny_alder):
    person_dict["alder"] = ny_alder
    return person_dict

# Test funktionen
opdateret_person = opdater_alder(person, 30)
print("Efter opdatering:", opdateret_person)

print()

# Liste af tre dictionaries
personer = [
    {"navn": "Maria", "alder": 24, "by": "Odense"},
    {"navn": "Jonas", "alder": 31, "by": "Aarhus"},
    {"navn": "Sofie", "alder": 29, "by": "København"}
]

# Loop gennem listen og print navnene
for p in personer:
    print("Person:", p["navn"])
