counts = {
    "python": 3,
    "is": 2,
    "easy": 1,
    "i": 2,
    "like": 2,
    "data": 1
}

pairs = []

for word, n in counts.items():
    pairs.append((n, word))

pairs.sort(reverse=True)

for n, word in pairs[:3]:
    print(f"{word:<8} {n}")