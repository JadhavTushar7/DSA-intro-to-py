with open("c.txt", "w", encoding="utf-8") as f:
    f.write("Chloé, Noël")

with open("c.txt", "r", encoding="latin-1") as f:
    print(f.read())