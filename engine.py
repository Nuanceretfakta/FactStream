# engine.py

def klassificer_med_konfidens(besked):
    """
    Returnerer (kategori, konfidens).
    Robust: hvis besked er None eller ikke tekst -> ("andet", 0.0)
    """
    try:
        if not isinstance(besked, str):
            return "andet", 0.0

        tekst = besked.lower()

        # Stærke keywords (0.9)
        if "pris" in tekst or "koster" in tekst:
            return "pris", 0.9
        if "åbent" in tekst or "åbning" in tekst:
            return "åbningstider", 0.9
        if "book" in tekst or "tid" in tekst:
            return "booking", 0.9

        # Svagere indikatorer (0.6)
        if "lukker" in tekst or "åbner" in tekst:
            return "åbningstider", 0.6
        if "reservere" in tekst or "reservation" in tekst or "aftale" in tekst:
            return "booking", 0.6

        return "andet", 0.4

    except Exception:
        return "andet", 0.0


def lav_svar(kategori, navn):
    if kategori == "pris":
        return f"Hej {navn}, her er vores priser: 500 kr. pr. time."
    elif kategori == "åbningstider":
        return f"Hej {navn}, vores åbningstider er kl. 9–17 på hverdage."
    elif kategori == "booking":
        return f"Hej {navn}, du kan booke en tid via vores hjemmeside."
    else:
        return f"Hej {navn}, tak for din besked – vi vender tilbage hurtigst muligt."


def behandl_henvendelse(henvendelse):
    """
    Input: {"navn": ..., "besked": ...}
    Output: ny dict med navn, besked, kategori, konfidens, svar, requires_human
    """
    navn = henvendelse.get("navn", "Ukendt")
    besked = henvendelse.get("besked")

    kategori, konfidens = klassificer_med_konfidens(besked)

    # Fallback: hvis vi ikke er sikre nok -> andet
    if konfidens < 0.7:
        kategori_final = "andet"
    else:
        kategori_final = kategori

    requires_human = (kategori_final == "andet")

    svar = lav_svar(kategori_final, navn)

    return {
        "navn": navn,
        "besked": besked,
        "kategori": kategori_final,
        "konfidens": konfidens,
        "svar": svar,
        "requires_human": requires_human
    }
