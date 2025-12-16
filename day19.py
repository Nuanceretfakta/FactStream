print("Learning AI – Day 19")

with open("data.txt", "r") as fil:
    linjer = fil.readlines()

antal_linjer = len(linjer)

opsummering = f"Antal linjer: {antal_linjer}"

with open("output.txt", "w") as fil:
    fil.write(opsummering)

print(opsummering)
