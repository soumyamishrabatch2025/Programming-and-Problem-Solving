# Type Content here...

setA = set(map(int, input("Set A: ").split(" ")))
setB = set(map(int, input("Set B: ").split(" ")))

print("Union:", setA.union(setB))
print("Intersection:", setA.intersection(setB))
print("Difference:", setA.difference(setB))