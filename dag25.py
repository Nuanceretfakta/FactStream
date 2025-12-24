# day25.py
print("Learning AI – Day 25")

henvendelser = [
    {"navn": "Anna", "besked": "Jeg vil gerne kende prisen"},
    {"navn": "Peter", "besked": "Hvornår har I åbent i morgen?"},
    {"navn": "Sara", "besked": "Kan jeg booke en tid på fredag?"},
    {"navn": "Maja", "besked": "Har I gavekort?"},
    {"navn": "Jonas", "besked": "Hvad koster det at få lavet farve?"},
    {"navn": "Nadia", "besked": "Hvornår lukker I i dag?"},
    {"navn": "Emil", "besked": "Kan jeg reservere en tid næste uge?"},
]

def klassificer_med_konfidens(besked: str):
    b = besked.lower()

    # stærke keywords -> 0.9
    if "pris" in b or "koster" in b:
        return "pris", 0.9
    if "åbent" in b or "åbning" in b:
        return "åbningstider", 0.9
    if "book" in b or "tid" in b:
        return "booking", 0.9

    # svagere indikatorer -> 0.6
    if "lukker" in b:
        return "åbningstider", 0.6
    if "reservere" in b or "reserver" in b:
        return "booking", 0.6

    # ellers -> 0.4
    return "andet", 0.4


log_linjer = []

for h in henvendelser:
    kategori, konfidens = klassificer_med_konfidens(h["besked"])

    # fallback: hvis lav konfidens, så sæt til "andet"
    if konfidens < 0.7:
        kategori = "andet"

    kræver_menneske = "ja" if kategori == "andet" else "nej"

    # Lav en log-linje (én linje per henvendelse)
    linje = f"{h['navn']} | {h['besked']} | {kategori} | {konfidens:.1f} | kræver_menneske={kræver_menneske}"
    log_linjer.append(linje)

# Skriv log til fil
with open("log_day25.txt", "w", encoding="utf-8") as fil:
    for linje in log_linjer:
        fil.write(linje + "\n")

print("Log skrevet til log_day25.txt")
