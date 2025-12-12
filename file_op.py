
def file_operations():
    
    print("\n*****File Operations*****\n")

    def create_new_file(filename):
        with open(filename, "w") as file:
            file.write("")       
        print(f"\nFile '{filename}' created successfully!\n")

    def write_to_file(filename, content):
        with open(filename, "w") as file:
            file.write(content)
        print("\nContent written successfully!\n")

    def read_from_file(filename):
        try:
            with open(filename, "r") as file:
                data = file.readlines()
            if data:
                print("\n--- File Contents ---\n")
                for line in data:
                    print(line.strip())
                print("")
            else:
                print("\nFile is empty.\n")
        except FileNotFoundError:
            print("\nFile not found!\n")

    def append_to_file(filename, content):
        try:
            with open(filename, "a") as file:
                file.write(content + "\n")
            print("\nText appended successfully!\n")
        except FileNotFoundError:
            print("\nFile not found!\n")


    while True:
        print("-----Please Select an Option-----")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")

        choice = int(input("\nEnter your choice: "))

        match choice:

            case 1:
                filename = input("Enter file name: ")
                create_new_file(filename)

            case 2:
                filename = input("Enter file name: ")
                content = input("Enter text to write: ")
                write_to_file(filename, content)

            case 3:
                filename = input("Enter file name: ")
                read_from_file(filename)

            case 4:
                filename = input("Enter file name: ")
                content = input("Enter text to append: ")
                append_to_file(filename, content)

            case 5:
                print("\nReturning to Main Menu...\n")
                break

            case _:
                print("\nInvalid choice! Try again.\n")



