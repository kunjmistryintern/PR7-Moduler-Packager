import math

def mathematical_operations():
    
    print ("*****Mathematical operation*****\n")

    def factorial():
        num = int(input("Enter a number to calculate its factorial: "))
        result = math.factorial(num)
        print(f"The factorial of {num} is {result}\n")
        
    def compound_interest():
        P = float(input("Enter the principal amount: "))
        R = float(input("Enter the rate of interest (in %): "))
        T = float(input("Enter the time (in years): "))
        A = P * (1 + R / 100) ** T
        CI = A - P
        print(f"The compound interest after {T} years is {CI:.2f}\n")
        
    def trigonometric_calculations():
        angle = float(input("Enter the angle in degrees: "))
        rad = math.radians(angle)
        print(f"Sin({angle}) = {math.sin(rad):.4f}")
        print(f"Cos({angle}) = {math.cos(rad):.4f}")
        print(f"Tan({angle}) = {math.tan(rad):.4f}\n")
        
    def area_of_shapes():
        print("Choose Shape to calculate area:")
        print("1. Circle")
        print("2. Rectangle")
        print("3. Triangle")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            r = float(input("Enter radius of the circle: "))
            area = math.pi * r * r
            print(f"Area of Circle = {area:.2f}\n")
            
        elif choice == 2:
            l = float(input("Enter length of the rectangle: "))
            b = float(input("Enter breadth of the rectangle: "))
            area = l * b
            print(f"Area of Rectangle = {area:.2f}\n")
            
        elif choice == 3:
            base = float(input("Enter base of the triangle: "))
            height = float(input("Enter height of the triangle: "))
            area = 0.5 * base * height
            print(f"Area of Triangle = {area:.2f}\n")
            
        else:
            print("Invalid Shape Option\n")
            

    while True:

        print ("-----Please Select an Option-----")
        print ("01. Calculate Factorial")
        print ("02. Solve Compound Interest")
        print ("03. Trigonometric Calculations")
        print ("04. Area of Geometric Shapes")
        print ("05. Back to Main Menu\n")

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                factorial()

            case 2:
                compound_interest()

            case 3:
                trigonometric_calculations()

            case 4: 
                area_of_shapes()

            case 5:
                break

            case _:
                print("Invalid choice. Please try again.\n")