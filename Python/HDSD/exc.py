# Version 3
def main():
    try:
        weight = int(input("Enter the weight in kg: " ))   
        heightInCM = int(input("Enter your height in cm: "))
        bmi = calculateBMI(weight, heightInCM);
        print("BMI: {:.2f}".format(bmi))
        ...

    except:
        print("Some input is in wrong format or outside valid range!")
        print("Please try again.")

main()