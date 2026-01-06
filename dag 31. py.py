# day31.py
# Dag 31 – Analyse af administrative henvendelser → beslutningsstøtte

henvendelser = [
    {"afdeling": "HR", "besked": "Spørgsmål til ferie", "tid_min": 5},
    {"afdeling": "HR", "besked": "Lang sygefraværssag", "tid_min": 45},
    {"afdeling": "IT", "besked": "Password virker ikke", "tid_min": 10},
    {"afdeling": "IT", "besked": "Ny pc til ny medarbejder", "tid_min": 30},
]

# --- regler / definitioner ---
# "Lavthængende frugter" = korte sager, der ofte kan standardiseres eller automatiseres
SIMPLE_THRESHOLD_MIN = 10


def er_simple_sag(sag: dict) -> bool:
    """Returnerer True hvis sagen regnes som 'simpel' (lavthængende frugt)."""
    try:
        tid = sag.get("tid_min")
        return isinstance(tid, (int, float)) and tid <= SIMPLE_THRESHOLD_MIN
    except Exception:
        return False


def beregn_statistik(henv: list[dict]) -> dict:
    """Samler statistik pr. afdeling + samlet gennemsnit."""
    statistik = {
        "afdelinger": {},  # afdeling -> {total_min, antal, simple_antal, simple_min, sager[]}
        "samlet": {"total_min": 0, "antal": 0},
    }

    for sag in henv:
        afdeling = sag.get("afdeling", "Ukendt")
        tid = sag.get("tid_min", 0)

        if afdeling not in statistik["afdelinger"]:
            statistik["afdelinger"][afdeling] = {
                "total_min": 0,
                "antal": 0,
                "simple_antal": 0,
                "simple_min": 0,
                "sager": [],
            }

        # robusthed: hvis tid ikke er tal, så behandl som 0
        if not isinstance(tid, (int, float)):
            tid = 0

        statistik["afdelinger"][afdeling]["total_min"] += tid
        statistik["afdelinger"][afdeling]["antal"] += 1
        statistik["afdelinger"][afdeling]["sager"].append(sag)

        statistik["samlet"]["total_min"] += tid
        statistik["samlet"]["antal"] += 1

        if er_simple_sag(sag):
            statistik["afdelinger"][afdeling]["simple_antal"] += 1
            statistik["afdelinger"][afdeling]["simple_min"] += tid

    return statistik


def procent(del_tal: int, hel_tal: int) -> float:
    if hel_tal == 0:
        return 0.0
    return (del_tal / hel_tal) * 100


def print_rapport(stats: dict) -> None:
    print("Dag 31 – Mini-rapport (administrative henvendelser)")
    print("-" * 55)

    # samlet gennemsnitlig sagstid
    samlet_total = stats["samlet"]["total_min"]
    samlet_antal = stats["samlet"]["antal"]
    gennemsnit = (samlet_total / samlet_antal) if samlet_antal else 0

    print(f"Samlet: {samlet_antal} henvendelser, {samlet_total} min total")
    print(f"Gennemsnitlig sagstid: {gennemsnit:.1f} min")
    print()

    # pr. afdeling
    for afdeling, data in stats["afdelinger"].items():
        total_min = data["total_min"]
        antal = data["antal"]
        simple_antal = data["simple_antal"]
        simple_min = data["simple_min"]

        simple_pct = procent(simple_antal, antal)
        simple_min_pct = procent(simple_min, total_min) if total_min else 0.0

        print(f"{afdeling} bruger {total_min} minutter pr. dag på henvendelser.")
        print(f"- {simple_pct:.0f}% er simple (≤ {SIMPLE_THRESHOLD_MIN} min).")
        print(f"- Simple sager udgør {simple_min_pct:.0f}% af tidsforbruget.")
        print("Lavthængende frugter (eksempler):")

        # list de simple sager pænt
        simple_sager = [s for s in data["sager"] if er_simple_sag(s)]
        if not simple_sager:
            print("  - (ingen)")
        else:
            for s in simple_sager:
                print(f"  - {s.get('besked')} ({s.get('tid_min')} min)")
        print("-" * 55)


if __name__ == "__main__":
    stats = beregn_statistik(henvendelser)
    print_rapport(stats)
