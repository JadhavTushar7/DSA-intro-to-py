words = ["a", "b", "a", "c", "a"]
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) +1
print(counts)