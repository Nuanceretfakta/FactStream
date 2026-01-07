# day32.py
# Dag 32 – Identificér hvor tiden forsvinder (Pareto)

henvendelser = [
    # Dag 31 (grund-datasæt)
    {"afdeling": "HR", "sagstype": "ferie", "besked": "Spørgsmål til ferie", "tid_min": 5},
    {"afdeling": "HR", "sagstype": "sygefravær", "besked": "Lang sygefraværssag", "tid_min": 45},
    {"afdeling": "IT", "sagstype": "password", "besked": "Password virker ikke", "tid_min": 10},
    {"afdeling": "IT", "sagstype": "udstyr", "besked": "Ny pc til ny medarbejder", "tid_min": 30},

    # Udvidet datasæt (6–8 ekstra)
    {"afdeling": "IT", "sagstype": "password", "besked": "Nulstil adgang til system", "tid_min": 12},
    {"afdeling": "IT", "sagstype": "udstyr", "besked": "Opsætning af telefon", "tid_min": 20},
    {"afdeling": "HR", "sagstype": "ferie", "besked": "Restferie og overførsel", "tid_min": 15},
    {"afdeling": "HR", "sagstype": "sygefravær", "besked": "Opfølgning på sygefravær (møde + notat)", "tid_min": 35},
    {"afdeling": "HR", "sagstype": "kontrakt", "besked": "Spørgsmål til kontraktvilkår", "tid_min": 25},
    {"afdeling": "IT", "sagstype": "support", "besked": "Outlook sync-problem", "tid_min": 18},
    {"afdeling": "IT", "sagstype": "udstyr", "besked": "Bestilling af skærm + docking", "tid_min": 22},
    {"afdeling": "HR", "sagstype": "ferie", "besked": "Ferie i forbindelse med helligdage", "tid_min": 8},
]


def beregn_tid_pr_sagstype(data: list[dict]) -> dict[str, float]:
    """Returnerer dict: sagstype -> total tid (min). Robust hvis tid mangler/er forkert."""
    tid_pr_type: dict[str, float] = {}

    for sag in data:
        sagstype = sag.get("sagstype", "ukendt")
        tid = sag.get("tid_min", 0)

        if not isinstance(tid, (int, float)):
            tid = 0

        tid_pr_type[sagstype] = tid_pr_type.get(sagstype, 0) + tid

    return tid_pr_type


def pct(del_tal: float, hel_tal: float) -> float:
    if hel_tal == 0:
        return 0.0
    return (del_tal / hel_tal) * 100


def print_ledelsesrapport(tid_pr_type: dict[str, float]) -> None:
    total_tid = sum(tid_pr_type.values())

    # sorter desc efter tid
    sorteret = sorted(tid_pr_type.items(), key=lambda x: x[1], reverse=True)

    top2 = sorteret[:2]
    top2_tid = sum(t for _, t in top2)
    top2_pct = pct(top2_tid, total_tid)

    print("Dag 32 – Hvor forsvinder tiden? (Pareto-overblik)")
    print("-" * 60)
    print(f"Samlet tidsforbrug (alle sagstyper): {total_tid:.0f} min")
    print()

    print("Top 2 sagstyper med størst tidsforbrug:")
    for i, (sagstype, tid) in enumerate(top2, start=1):
        andel = pct(tid, total_tid)
        print(f"{i}) {sagstype}: {tid:.0f} min ({andel:.1f}% af totalen)")

    print()
    print(f"Konklusion: Top 2 sagstyper udgør {top2_pct:.1f}% af den samlede tid.")
    print("Anbefaling: Prioritér standardisering/automatisering i disse 2 sagstyper først.")
    print("-" * 60)

    # (valgfrit) vis resten kort for kontekst
    print("Øvrige sagstyper (til kontekst):")
    for sagstype, tid in sorteret[2:]:
        print(f"- {sagstype}: {tid:.0f} min ({pct(tid, total_tid):.1f}%)")


if __name__ == "__main__":
    tid_pr_type = beregn_tid_pr_sagstype(henvendelser)
    print_ledelsesrapport(tid_pr_type)
