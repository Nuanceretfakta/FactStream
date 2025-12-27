# day27.py
print("Learning AI – Day 27")

from engine import behandl_henvendelse

henvendelser = [
    {"navn": "Anna", "besked": "Jeg vil gerne kende prisen"},
    {"navn": "Peter", "besked": "Hvornår lukker I i dag?"},
    {"navn": "Sara", "besked": "Hej, jeg har et spørgsmål..."},
    {"navn": "Maja", "besked": None},
]

resultater = []
for h in henvendelser:
    resultater.append(behandl_henvendelse(h))

for r in resultater:
    print("\n---")
    print(f"Navn: {r['navn']}")
    print(f"Besked: {r['besked']}")
    print(f"Kategori: {r['kategori']}")
    print(f"Konfidens: {r['konfidens']}")
    print(f"Requires human: {r['requires_human']}")
    print(f"Svar: {r['svar']}")
