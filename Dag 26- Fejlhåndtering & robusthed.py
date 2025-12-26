print("Learning AI – Day 26")

henvendelser = [
    {"navn": "Anna", "besked": "Hvad koster det?"},
    {"navn": "Peter", "besked": None},
    {"navn": "Sara", "besked": "Kan jeg booke?"}
]


def klassificer_med_konfidens(besked):
    try:
        tekst = besked.lower()

        if "pris" in tekst or "koster" in tekst:
            return "pris", 0.9, "nej"
        if "book" in tekst or "tid" in tekst:
            return "booking", 0.9, "nej"

        return "andet", 0.4, "nej"

    except Exception:
        # Hvis besked er None, ikke tekst, eller noget uventet sker
        return "andet", 0.0, "ja"


for h in henvendelser:
    kategori, konfidens, fejl = klassificer_med_konfidens(h["besked"])

    print("\n---")
    print(f"Navn: {h['navn']}")
    print(f"Kategori: {kategori}")
    print(f"Konfidens: {konfidens}")
    print(f"Fejl: {fejl}")
