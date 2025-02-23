class LinearProbing:
    def __init__(self, size=10):
        self.size = size   # Size of the hash table
        self.table = [-1] * size  # Initialize the hash table with -1

    def hash_function(self, phone):
        """Hash function to calculate the index."""
        return phone % self.size

    def insert(self, phone, name):
        """Insert (phone, name) using linear probing if needed."""
        index = self.hash_function(phone)

        if self.table[index] == -1:  # If the index is empty 
            self.table[index] = (phone, name) #insert the phone and name into the table
        else:
            print(f"Collision occurred at index {index}. Applying Linear Probing...")
            self.linear_probing(phone, name, index)  # Call linear probing function

    def linear_probing(self, phone, name, index):
        """Handle collisions using linear probing."""
        for i in range(self.size):  # Search for an empty slot
            new_index = (index + i) % self.size  # Circular probing
            if self.table[new_index] == -1: #if the index is empty
                self.table[new_index] = (phone, name) #insert the phone and name into the table
                return  
        print("Hash table is full! Cannot insert more elements.")

    def search(self, phone): 
        """Search for a phone number using linear probing."""
        index = self.hash_function(phone)

        for i in range(self.size):  # Scan using linear probing
            new_index = (index + i) % self.size
            if self.table[new_index] == -1:  # Stop if empty slot found
                break
            if self.table[new_index][0] == phone:  # Match found
                return self.table[new_index]
        
        return None  # Not found

    def display(self):
        """Display the hash table contents."""
        print("\nHash Table:")
        for i, entry in enumerate(self.table): #enumerate the table
            if entry == -1: #if the index is empty
                print(f"Index {i}: Empty") #print that the index is empty
            else:
                print(f"Index {i}: {entry[0]} - {entry[1]}") #print the phone and name

            
def main():
    hash_table = LinearProbing() #create a hash table

    while True:
        print("\nTelephone Book Database")
        print("1. Insert")
        print("2. Search")
        print("3. Display")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice: ")) #read the choice from the user
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        
        if choice == 1:
            try:
                phone = int(input("Enter the phone number: ")) #read the phone number from the user     
                name = input("Enter the name: ") #read the name from the user
                hash_table.insert(phone, name) #insert the phone and name into the table
            except ValueError:
                print("Invalid input! Phone number must be a number.") #print that the phone number must be a number
        elif choice == 2:
            try:
                phone = int(input("Enter the phone number to search: ")) #read the phone number to search from the user
                result = hash_table.search(phone) #search for the phone number in the table
                if result:
                    print(f"Phone number found: {result[0]} - {result[1]}") #print the phone and name
                else:
                    print("Phone number not found.") #print that the phone number is not found
            except ValueError:
                print("Invalid input! Phone number must be a number.") #print that the phone number must be a number
        elif choice == 3:
            hash_table.display() #display the table
        elif choice == 4:
            print("Exiting the program...") #print that the program is exiting
            break
        else:
            print("Invalid choice. Please try again.") #print that the choice is invalid

            
if __name__ == "__main__":
    main() #call the main function
