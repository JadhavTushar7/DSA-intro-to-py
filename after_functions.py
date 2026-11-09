def read_grades(path):
    grades = {}
    with open(path, encoding="utf-8") as f:
     for line in f:
      name, g = line.split() 
      grades[name] = int(g)
    return grades

def average(values):
   return sum(values)/len(values)

grades = read_grades("grades.txt")
print(f"Average: {average(grades.values()):2f}")