#this is a test
#this is a test



myList = []

while True:
    item = input("Enter items to add to the shopping list (enter 'done' when finished):\n")

    if item.lower() == 'done':
        break

    # Append the item to the shopping list
    myList.append(item)

# Display the contents of the shopping list
print("\nYour shopping list:")
for index, item in enumerate(myList, start=1):
    print(f"{index}. {item}")

# Ask the user to enter an item to remove
remove_item = input("\nEnter an item to remove from the list: ")

# Attempt to remove the item, handling if it's not in the list
if remove_item in myList:
    myList.remove(remove_item)
    print("\nUpdated shopping list:")
    for index, item in enumerate(myList, start=1):
        print(f"{index}. {item}")
else:
    print(f"\n'{remove_item}' is not in the shopping list.")

# Display the total number of items in the shopping list
total_items = len(myList)
print(f"\nTotal number of items in the shopping list: {total_items}")
