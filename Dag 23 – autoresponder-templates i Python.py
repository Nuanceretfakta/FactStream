print("Learning AI – Day 23")

henvendelser = [
    {"navn": "Anna", "besked": "Jeg vil gerne kende prisen"},
    {"navn": "Peter", "besked": "Hvornår har I åbent i morgen?"},
    {"navn": "Sara", "besked": "Kan jeg booke en tid på fredag?"},
    {"navn": "Maja", "besked": "Har I gavekort?"}
]


def klassificer(besked):
    tekst = besked.lower()

    if "pris" in tekst:
        return "pris"
    elif "åbent" in tekst or "åbning" in tekst:
        return "åbningstider"
    elif "book" in tekst or "tid" in tekst:
        return "booking"
    else:
        return "andet"


def lav_svar(kategori, navn):
    if kategori == "pris":
        return f"Hej {navn}, her er vores priser: 500 kr. pr. time."
    elif kategori == "åbningstider":
        return f"Hej {navn}, vores åbningstider er kl. 9–17 på hverdage."
    elif kategori == "booking":
        return f"Hej {navn}, du kan booke en tid via vores hjemmeside."
    else:
        return f"Hej {navn}, tak for din besked – vi vender tilbage hurtigst muligt."


for h in henvendelser:
    kategori = klassificer(h["besked"])
    svar = lav_svar(kategori, h["navn"])

    h["kategori"] = kategori
    h["svar"] = svar

    print(f"\nNavn: {h['navn']}")
    print(f"Kategori: {h['kategori']}")
    print(f"Svar: {h['svar']}")
