hashmap = {}
while True:
    print("\n1. Put")
    print("2. Get")
    print("3. Remove")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        key = int(input("Enter key: "))
        value = int(input("Enter value: "))

        hashmap[key] = value
        print("Added successfully")
    elif choice == 2:
        key = int(input("Enter key: "))
        if key in hashmap:
            print("Value:", hashmap[key])
        else:
            print("Key not found")
    elif choice == 3:
        key = int(input("Enter key: "))
        if key in hashmap:
            del hashmap[key]
            print("Removed successfully")
        else:
            print("Key not found")
    elif choice == 4:
        print("HashMap:", hashmap)
    elif choice == 5:
        break
    else:
        print("Invalid choice")