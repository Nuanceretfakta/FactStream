print("Learning AI – Day 17")

tal = [12, 5, 19, 3, 27, 14, 8]

def beregn_stats(tal):
    minimum = min(tal)
    maksimum = max(tal)
    gennemsnit = sum(tal) / len(tal)

    return {
        "min": minimum,
        "max": maksimum,
        "gennemsnit": gennemsnit
    }

stats = beregn_stats(tal)

print(f"Min: {stats['min']}, Max: {stats['max']}, Gennemsnit: {stats['gennemsnit']}")
