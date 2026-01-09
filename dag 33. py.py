# day33.py
# Dag 33 – Fra analyse til Excel-klar output (CSV)

import csv

henvendelser = [
    {"sagstype": "ferie", "tid_min": 5},
    {"sagstype": "sygefravær", "tid_min": 45},
    {"sagstype": "password", "tid_min": 10},
    {"sagstype": "udstyr", "tid_min": 30},
    {"sagstype": "password", "tid_min": 12},
    {"sagstype": "udstyr", "tid_min": 20},
    {"sagstype": "ferie", "tid_min": 15},
    {"sagstype": "sygefravær", "tid_min": 35},
    {"sagstype": "kontrakt", "tid_min": 25},
    {"sagstype": "support", "tid_min": 18},
    {"sagstype": "udstyr", "tid_min": 22},
    {"sagstype": "ferie", "tid_min": 8},
]


def beregn_tid_pr_sagstype(data: list[dict]) -> dict[str, int]:
    tid_pr_type = {}
    for sag in data:
        sagstype = sag.get("sagstype", "andet")
        tid = sag.get("tid_min", 0)
        tid_pr_type[sagstype] = tid_pr_type.get(sagstype, 0) + tid
    return tid_pr_type


def beregn_andel(tid_pr_type: dict[str, int]) -> list[dict]:
    samlet_tid = sum(tid_pr_type.values())
    resultater = []

    for sagstype, tid in tid_pr_type.items():
        andel_pct = round((tid / samlet_tid) * 100, 1) if samlet_tid else 0
        resultater.append({
            "sagstype": sagstype,
            "samlet_tid": tid,
            "andel_pct": andel_pct
        })

    return resultater


def eksportér_til_csv(data: list[dict], filnavn: str):
    with open(filnavn, mode="w", newline="", encoding="utf-8") as fil:
        writer = csv.DictWriter(
            fil,
            fieldnames=["sagstype", "samlet_tid", "andel_pct"]
        )
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    tid_pr_type = beregn_tid_pr_sagstype(henvendelser)
    analyse = beregn_andel(tid_pr_type)

    # sorter så Excel får pæn rækkefølge (mest tid først)
    analyse.sort(key=lambda x: x["samlet_tid"], reverse=True)

    eksportér_til_csv(analyse, "analyse_day33.csv")

    print("Data eksporteret til analyse_day33.csv")
