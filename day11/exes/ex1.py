set1 = set()
set1.add("Cuong")
set1.update(["Ha", "Linh"])
set2 = {"Cuong", "Nam", "Dang"}

set1_set2 = set1.union(set2)
print(set1_set2)
print(set1.symmetric_difference(set2))
print(set1.intersection(set2))
