print("Learning AI – Day 24")

henvendelser = [
    {"navn": "Anna", "besked": "Jeg vil gerne kende prisen"},
    {"navn": "Peter", "besked": "Hvornår har I åbent i morgen?"},
    {"navn": "Sara", "besked": "Kan jeg booke en tid på fredag?"},
    {"navn": "Maja", "besked": "Har I gavekort?"},
    {"navn": "Jonas", "besked": "Hvad koster det cirka?"},
    {"navn": "Sofie", "besked": "Hvornår lukker I i dag?"},
    {"navn": "Lukas", "besked": "Kan jeg reservere en tid?"}
]


def klassificer_med_konfidens(besked):
    tekst = besked.lower()

    # Stærke keywords (meget tydelige)
    stærke = {
        "pris": ["pris"],
        "åbningstider": ["åbent", "åbning"],
        "booking": ["book", "tid"]
    }

    # Svage indikatorer (mere “tolkbare”)
    svage = {
        "pris": ["koster", "prisniveau", "dyrt", "billigt"],
        "åbningstider": ["lukker", "åbner", "åbningstid"],
        "booking": ["reservere", "reservation", "bestille tid", "aftale"]
    }

    # 1) Tjek stærke først → høj konfidens
    for kategori, ordliste in stærke.items():
        for ord in ordliste:
            if ord in tekst:
                return kategori, 0.9

    # 2) Tjek svage → middel konfidens
    for kategori, ordliste in svage.items():
        for ord in ordliste:
            if ord in tekst:
                return kategori, 0.6

    # 3) Ellers lav konfidens
    return "andet", 0.4


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
    kategori, konfidens = klassificer_med_konfidens(h["besked"])

    # Fallback-regel: hvis vi ikke er sikre nok → behandl som "andet"
    if konfidens < 0.7:
        kategori = "andet"

    svar = lav_svar(kategori, h["navn"])

    print("\n---")
    print(f"Navn: {h['navn']}")
    print(f"Besked: {h['besked']}")
    print(f"Kategori: {kategori}")
    print(f"Konfidens: {konfidens}")
    print(f"Svar: {svar}")
