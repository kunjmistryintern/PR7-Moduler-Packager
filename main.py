import date_time as d_t
import math_op as m_o
import random_data as r_d  
import file_op as f_o
import uuid   

def generate_uuid():
    unique_id = uuid.uuid4()   
    print("\nGenerated UUID:", unique_id,"\n")
    
def explore_module_attributes():
    print("\n*** Explore Module Attributes ***\n")
    module_name = input("Enter module name to explore: ").strip()
    if not module_name:
        print("No module name provided.\n")
        return
    try:
        module = __import__(module_name)
    except ModuleNotFoundError:
        print(f"Module '{module_name}' not found.\n")
        return
    print(f"\nAvailable Attributes in {module_name} module:\n")
    print(dir(module))  


print("\n*-*-* Welcome to the Multi-Utility Toolkit! *-*-*\n")
    
while True:

    print ("\n-----Please Select an Option-----\n")
    print ("01. Datetime and Time Operations")
    print ("02. Mathematical Operations")
    print ("03. Random Data Generation")
    print ("04. Generate Unique Identifier (UUID)")
    print ("05. File Operations")
    print ("06. Explor Module Attributes (dir())")
    print ("07. Exit\n")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            d_t.datetime_operations()
            
        case 2:
            m_o.mathematical_operations()

        case 3:
            r_d.random_data_generation()

        case 4:
            generate_uuid()

        case 5:
            f_o.file_operations()

        case 6:
            explore_module_attributes()

        case 7:
            print("Exiting the Multi-Utility Toolkit. Goodbye!")
            break

        case _:
            print("Invalid choice. Please try again.\n")

