import datetime
import time

def datetime_operations():

    print("\n***** Date and Time Operations *****\n")
    
    def display_current_datetime():
        now = datetime.datetime.now()
        print ("\nCurrent Date and Time: ", now, "\n")
        
    def calc_difference():
        print ("Enter the first date (YYYY-MM-DD): ")
        d1 = input()
        print ("Enter the second date (YYYY-MM-DD): ")
        d2 = input()
        
        date1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
        date2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
        
        difference = abs(date2 - date1)
        print ("\nDifference = ", difference.days, " days\n")
        
    def format_date():
        print ("Enter the date (YYYY-MM-DD): ")
        d = input()
        date = datetime.datetime.strptime(d, "%Y-%m-%d")
        
        print("\nChoose format:")
        print("1. DD-MM-YYYY")
        print("2. Month-DD-YYYY")
        
        choice = int(input("Enter choice: "))
        
        if choice == 1:
            print ("\nFormatted Date: ", date.strftime("%d-%m-%Y \n"))
        elif choice == 2:
            print ("\nFormatted Date: ", date.strftime("%B %d, %Y \n"))
        else:
            print ("Invalid Format Option")
            
    def stopwatch():
        print ("\nStopwatch\n")
        input("Press ENTER to start")
        start = time.time()
        
        input("Press ENTER to stop")
        end = time.time()
        
        print ("\nTotal Time: ", round(end - start, 2), " seconds\n")
        
    def countdown():
        sec = int(input("\nEnter seconds for countdown: "))
        
        while sec > 0:
            print (sec)
            time.sleep(1)
            sec -= 1
        print("Countdown finished!\n")
    
    
    
    while True:
        print ("-----Please Select an Option-----")
        print ("01. Display Current Date and Time")
        print ("02. Calculate Difference between Date/Time")
        print ("03. Formate Date into coustom format")
        print ("04. StopWatch") 
        print ("05. Countdown Timer")
        print ("06. Back to Main Menu\n")
        
        choice = int(input("Enter your choice: "))
        
        match choice:
            
            case 1:
                display_current_datetime()
                
            case 2:
                calc_difference()
                
            case 3:
                format_date()
                
            case 4: 
                stopwatch()
                
            case 5:
                countdown()
                
            case 6:
                break
                
            case _:
                print("Invalid choice. Please try again.\n")
    