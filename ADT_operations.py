class SetADT:
    def __init__(self): 
        """Initialize an empty list to store set elements."""
        self.set = []

    def add(self):
        """Add elements to the set while ensuring no duplicates."""
        try:
            n = int(input("How many elements do you want to enter? "))
            for i in range(n):
                data = int(input("Enter data: "))
                if data not in self.set:  # Ensure uniqueness
                    self.set.append(data)
                else:
                    print(f"{data} is already in the set. Skipping...")
        except ValueError:
            print("Invalid input! Please enter an integer.")

    def remove_data(self):
        """Remove an element from the set if it exists."""
        try:
            data = int(input("Enter data you want to remove: "))
            if data in self.set:
                self.set.remove(data)
                print(f"{data} is removed from the set.")
            else:
                print(f"{data} is not in the set.")
            self.display()
        except ValueError:
            print("Invalid input! Please enter an integer.")

    def display(self):
        """Display the elements of the set."""
        if self.set:
            print("Set elements:", self.set)
        else:
            print("The set is empty.")

    def union(self, st):
        """Perform the union of two sets and display the result."""
        result = list(set(self.set).union(set(st.set)))
        print("\nUnion of Set1 and Set2:", result)

    def intersection(self, st):
        """Perform the intersection of two sets and display the result."""
        result = list(set(self.set).intersection(set(st.set)))
        if result:
            print("\nIntersection of Set1 and Set2:", result)
        else:
            print("\nNo common elements between Set1 and Set2.")

    def difference(self, st, order):
        """Perform the difference operation (Set1 - Set2) or (Set2 - Set1)."""
        if order == 1:
            result = list(set(self.set).difference(set(st.set)))
            print("\nDifference (Set1 - Set2):", result)
        else:
            result = list(set(st.set).difference(set(self.set)))
            print("\nDifference (Set2 - Set1):", result)

    def membership(self):
        """Check if a given element is present in the set."""
        try:
            data = int(input("Enter data to check membership: "))
            if data in self.set:
                print(f"{data} is present in the set.")
            else:
                print(f"{data} is not present in the set.")
            self.display()
        except ValueError:
            print("Invalid input! Please enter an integer.")


# Main Menu
set1 = SetADT()  
set2 = SetADT()  

while True:
    print("\n********** Set Operations ************")
    print("1. Insert Elements")
    print("2. Remove Elements")
    print("3. Display Elements")
    print("4. Perform Union Operation")
    print("5. Perform Intersection Operation")
    print("6. Perform Difference Operation")
    print("7. Check Membership")
    print("8. Exit")

    try:
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            set_choice = int(input("Enter elements in Set 1 or Set 2? (1/2): "))
            if set_choice in [1, 2]:
                (set1 if set_choice == 1 else set2).add()
            else:
                print("Invalid set choice! Enter 1 or 2.")

        elif choice == 2:
            set_choice = int(input("Remove element from Set 1 or Set 2? (1/2): "))
            if set_choice in [1, 2]:
                (set1 if set_choice == 1 else set2).remove_data()
            else:
                print("Invalid set choice! Enter 1 or 2.")

        elif choice == 3:
            set_choice = int(input("Display elements of Set 1 or Set 2? (1/2): "))
            if set_choice in [1, 2]:
                (set1 if set_choice == 1 else set2).display()
            else:
                print("Invalid set choice! Enter 1 or 2.")

        elif choice == 4:
            set1.union(set2)

        elif choice == 5:
            set1.intersection(set2)

        elif choice == 6:
            order = int(input("Choose difference operation:\n1. Set1 - Set2\n2. Set2 - Set1\nEnter choice (1/2): "))
            if order in [1, 2]:
                set1.difference(set2, order)
            else:
                print("Invalid choice! Enter 1 or 2.")

        elif choice == 7:
            set_choice = int(input("Check membership in Set 1 or Set 2? (1/2): "))
            if set_choice in [1, 2]:
                (set1 if set_choice == 1 else set2).membership()
            else:
                print("Invalid set choice! Enter 1 or 2.")

        elif choice == 8:
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please enter a valid option.")

    except ValueError:
        print("Invalid input! Please enter a number.")

