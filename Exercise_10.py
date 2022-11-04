#!/usr/bin/env python3

# Create two sets in distinct ways
mySet = set("ATGTGGG")
mySet2 = {"ATGTGGG"}

# Print both sets
print(
"Set using the set() function:", mySet,
"\nSet using {}:", mySet2)

# Explain why the sets are different
print("\nDespite the fact that both sets have the same content, the 'set()' function eliminates all duplicates and returns a set of unique values without any specific order. In contrast, by using just the '{}' to create the set, printing it returns all its contents in the specified order.")


