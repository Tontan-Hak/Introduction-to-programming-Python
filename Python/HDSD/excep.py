# 
def main():
    while True:
        print("\n---------- Menu ----------")
        print("1. Calculate a person's BMI")
        print("2. Exit")
        option = input("Please select an option: ")
        if option == "1":
            findBMI()   
        elif option == "2":
            print("Thank you!")
            break
        else:
            print("Invalid option. Please try again.")
main()
