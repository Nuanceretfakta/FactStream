# day28.py
print("Learning AI – Day 28 (Tests)")

from engine import klassificer_med_konfidens

tests = [
    ("Hvad koster det?", "pris"),
    ("Hvornår har I åbent?", "åbningstider"),
    ("Kan jeg booke en tid?", "booking"),
    ("Har I gavekort?", "andet"),
    (None, "andet")
]

passed = 0

for besked, forventet_kategori in tests:
    kategori, konfidens = klassificer_med_konfidens(besked)

    if kategori == forventet_kategori:
        print(f"PASS: {besked} → {kategori}")
        passed += 1
    else:
        print(f"FAIL: {besked} → {kategori} (forventet {forventet_kategori})")

print(f"\n{passed}/{len(tests)} tests passed")
