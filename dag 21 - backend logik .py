henvendelser = [
    {"navn": "Anna", "besked": "Jeg vil gerne kende prisen", "prioritet": "høj"},
    {"navn": "Peter", "besked": "Hvornår har I åbent?", "prioritet": "lav"},
    {"navn": "Sara", "besked": "Kan jeg booke en tid?", "prioritet": "middel"}
]

def filtrer_høj_prioritet(data):
    return [h for h in data if h["prioritet"] == "høj"]

def lav_opsummering(data):
    return f"Der er {len(data)} højprioritets-henvendelse(r) i dag."

høj_prioritet = filtrer_høj_prioritet(henvendelser)
print(høj_prioritet)
print(lav_opsummering(høj_prioritet))
