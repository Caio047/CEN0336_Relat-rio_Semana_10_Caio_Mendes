#!/usr/bin/env python3

# Design a dictionary with my favorite things
fav_dict = {
"Book": "Assassin`s Creed Brotherhood",
"Song": "Vance Joy - Riptide",
"Tree": "Orange tree"
}

# Print out the favorite book by using a key found in the generated dictionary
print("Favorite book:", fav_dict["Book"])

# Assign the "Book" key to a variable
fav_thing = "Book"

# Print out the favorite book (using a variable as key) and the favorite tree
print(
"Favorite book (using a variable as key):", fav_dict[fav_thing],
"\nFavorite tree:", fav_dict["Tree"])

# Assign the key "Organism" to the "fav_thing" variable and add my favorite organism as a value for this new key
fav_thing = "Organism"
fav_dict[fav_thing] = "Bacteria"
print("Favorite organism:", fav_dict[fav_thing])

