# day22.py

henvendelser = [
    {"navn": "Anna", "besked": "Jeg vil gerne kende prisen"},
    {"navn": "Peter", "besked": "Hvornår har I åbent i morgen?"},
    {"navn": "Sara", "besked": "Kan jeg booke en tid på fredag?"},
    {"navn": "Maja", "besked": "Har I gavekort?"}
]

def klassificer(besked):
    b = besked.lower()

    if "pris" in b:
        return "pris"
    elif "åbent" in b or "åbning" in b:
        return "åbningstider"
    elif "book" in b or "tid" in b:
        return "booking"
    else:
        return "andet"

# Tilføj "kategori" til hver henvendelse
for h in henvendelser:
    h["kategori"] = klassificer(h["besked"])

# Print pænt
for h in henvendelser:
    print(f"Navn: {h['navn']} | Besked: {h['besked']} | Kategori: {h['kategori']}")
