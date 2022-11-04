#!/usr/bin/env python3

# Design a dictionary with my favorite things
fav_dict = {
"Book": "Assassin`s Creed Brotherhood",
"Song": "Vance Joy - Riptide",
"Tree": "Orange tree",
"Organism": "Bacteria",
"Favorite thing": "empty"
}

# Create a list, append all keys from the dictionary to it and print the available
available_keys_lst = list()
for keys in fav_dict.keys():
        available_keys_lst.append(keys)

# Design the app
while True:
        user_input = input("\nType 'Find' to discover the value for the desired key. \nType 'Change' to modify the value of the 'Favorite thing' key. \nType 'Change any' to modify the value of any key. \nType 'QUIT' to exit the program: ")
        if user_input == "QUIT":
            break

	# "Find" option prints all the available keys from "fav_dict", asks the user to type a key e then prints its value
        elif user_input == "Find":
            print("\nAvailable keys:", *available_keys_lst) # Print all available keys from "fav_dict"
            usr_find = input("Type any of the above keys to reveal its value (type 'QUIT' to exit the program): ") # Prompt the user for an input key from "fav_dict"
            if usr_find not in available_keys_lst: # Check if the user input is valid
                print("'" + usr_find + "'", "is not one of the available keys listed above. Try again.")
                continue
            else:
                print("The value for the", "'" + usr_find + "'", "key is", fav_dict[usr_find]) # Print the value for the key requested by the user

	# "Change" option asks the user for a new value for the "Favorite thing" key from "fav_dict"
        elif user_input == "Change":
            fav_thing = input("Type a new favorite thing to be assigned as a value to the 'Favorite thing' key: ") # Prompt the user for a new value for the "Favorite thing" key
            fav_dict["Favorite thing"] = fav_thing # Update the value for the "Favorite thing" key
            print("Dictionary updated!")

	# "Change any" option allows the user to modify the values from any key from "fav_dict".
        elif user_input == "Change any":
            print("\nAvailable keys to modify:", *available_keys_lst) # Print all available jeys from "fav_dict"
            usr_change = input("Type one key to modify its value: ") # Prompt the user for a key to modify its value
            if usr_change not in available_keys_lst:
                print("'" + usr_change + "'", "is not one of the available keys listed above. Try again.") # Check if the user input is an existing key
                continue
            else:
                new_value = input("Type the new value for the selected key: ") # Prompt the user for the new value for the requested key
                fav_dict[usr_change] = new_value # Update the dictionary with the new desired value for the requested key
                print("Dictionary updated!")
	
	# In case the first user input is invalid, run this block and return to the beginning
        else:
            print("'" + user_input + "' is not an available option. Try again.") # 
            continue
