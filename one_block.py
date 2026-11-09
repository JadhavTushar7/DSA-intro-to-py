total = 0 
count = 0

with open("grades.txt", encoding="utf-8") as f:
    for line in f:
        name, g = line.split()
        total += int(g)
        count += 1

if count > 0:
    print(f"Average: {total / count:.2f}")
