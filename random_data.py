import random

def random_data_generation():
    
    print("---Random Data Generation---\n")
    
    def random_number():
        lower = int(input("Enter Starting number: "))
        upper = int(input("Enter Ending number: "))
        rand_num = random.randint(lower, upper)
        print(f"Random Number between {lower} and {upper}: {rand_num}\n")
        
    def random_list():
        size = int(input("Enter size of the list: "))
        lower = int(input("Enter Starting number for list elements: "))
        upper = int(input("Enter Ending number for list elements: "))
        rand_list = [random.randint(lower, upper) for _ in range(size)]
        print(f"Random List: {rand_list}\n")
        
    def random_password():
        length = int(input("Enter desired password length: "))
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
        password = ''.join(random.choice(characters) for _ in range(length))
        print(f"Generated Password: {password}\n")
        
    def random_otp():
        length = int(input("Enter desired OTP length: "))
        otp = ''.join(str(random.randint(0, 9)) for _ in range(length))
        print(f"Generated OTP: {otp}\n")
        
    
    
    
    while True:
    
        print ("-----Please Select an Option-----")
        print ("01. Generate Random Number")
        print ("02. Generate Random List")
        print ("03. Create Random Password")
        print ("04. Generate Random OTP")
        print ("05. Back to Main Menu\n")
    
        choice = int(input("Enter your choice: "))
    
        match choice:
            case 1:
                random_number()
            
            case 2:
                random_list()
            
            case 3:
                random_password()
            
            case 4:
                random_otp()
            
            case 5:
                break
            
            case _:
                print("Invalid choice. Please try again.\n")
                
                