#!/usr/bin/env python3

# Create two sets
Set_A = {"3", "14", "15", "9", "26", "5", "35", "9"}
Set_B = {"60", "22", "14", "0", "9"}

# Find the intersection, difference, union and symetrical difference between the these sets
print("Intersection:", Set_A.intersection(Set_B))
print("Difference (A-B):", Set_A.difference(Set_B))
print("Difference (B-A):", Set_B.difference(Set_A))
print("Union", Set_A.union(Set_B))
print("Symmetric difference", Set_A.symmetric_difference(Set_B))
