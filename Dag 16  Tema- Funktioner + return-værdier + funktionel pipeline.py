print("Learning AI – Day 16")

def hent_brugerdata():
    navn = input("Skriv dit navn: ")
    alder = int(input("Skriv din alder: "))
    return navn, alder

def beregn_senior(alder):
    return 65 - alder

def opsummer(navn, alder, år_til_senior):
    print(f"{navn}, du er {alder} år. Der er {år_til_senior} år til du bliver 65.")

# Hovedprogram
navn, alder = hent_brugerdata()
år = beregn_senior(alder)
opsummer(navn, alder, år)
