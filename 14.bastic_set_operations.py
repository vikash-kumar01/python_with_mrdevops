# Set
# - another built-in data type of Python
# - does NOT allow duplicate values as with Lists
# - used to store multiple items of data


months_set = {"JAN", "FEB", "MAR", "APR"}

for element in months_set:
    print(element)

#Add an item to the set

# Add an item to the set
months_set.add("MAY")
print("After adding 'MAY':", months_set)

months_set.remove("MAY")
print(months_set)