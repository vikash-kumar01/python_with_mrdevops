# Basic list operations
# - Create a list - Access items of the list
# - Add an item to the list
# - Remove an item from the list
# - Change items in the list

# List items are indexed
# - First item has index 0

my_month = ["JAN", "FEB", "MAR"]
print(my_month[1])

my_month.append("APR")
print(my_month)

# Remove a specific item by value
my_month.remove("MAR")
print("After removing 'MAR':", my_month)

# Remove an item by index using pop()
removed_item = my_month.pop(1)  # Removes the item at index 1
print("After popping index 1:", my_month)
print("Popped item:", removed_item)

# Remove an item by index using del
del my_month[0]  # Removes the first item
print("After deleting the first item:", my_month)

# Initial list
my_month = ["JAN", "FEB", "MAR"]

# Change the value of an item
my_month[1] = "DEC"  # Changing 'FEB' to 'DEC'
print("After changing the second item:", my_month)

# Change multiple items
my_month[0:2] = ["JUL", "AUG"]  # Replace 'JAN' and 'DEC' with 'JUL' and 'AUG'
print("After changing multiple items:", my_month)
