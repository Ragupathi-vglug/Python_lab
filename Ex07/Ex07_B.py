set1={1,2,3,4,5}
set2={4,5,6,7,8}
print(set1)
print(set2)

union_set=set1 | set2
print("Union of sets:",union_set)

intersection_set=set1 & set2
print("Intersection of sets:",intersection_set)

difference_set1=set1-set2
print("Difference (set1 - set2):",difference_set1)

difference_set2=set2-set1
print("Difference (set2 - set1):",difference_set2)
