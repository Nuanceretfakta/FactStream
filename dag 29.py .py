# day29.py
print("Learning AI – Day 29 (Demo af AI-engine)\n")

from engine import behandl_henvendelse

# 6 henvendelser (mix af klare, uklare og fejl)
henvendelser = [
    {"navn": "Anna", "besked": "Hvad koster det?"},
    {"navn": "Peter", "besked": "Kan jeg booke en tid i næste uge?"},
    {"navn": "Sara", "besked": "Hvornår lukker I i dag?"},
    {"navn": "Jonas", "besked": "Hvad med farver og muligheder?"},
    {"navn": "Maja", "besked": "Har I gavekort?"},
    {"navn": "Emil", "besked": None},
]

resultater = []

print("=== BEHANDLING AF HENVENDELSER ===\n")

for h in henvendelser:
    r = behandl_henvendelse(h)
    resultater.append(r)

    print(f"Navn: {r['navn']}")
    print(f"Besked: {r['besked']}")
    print(f"Kategori: {r['kategori']} ({r['konfidens']})")
    print(f"Requires human: {r['requires_human']}")
    print(f"Svar: {r['svar']}")
    print("-" * 40)

# Opsummering
total = len(resultater)
auto = len([r for r in resultater if not r["requires_human"]])
human = len([r for r in resultater if r["requires_human"]])

print("\n=== OPSUMMERING ===")
print(f"Total henvendelser: {total}")
print(f"Auto-svar: {auto}")
print(f"Human-in-loop: {human}")
