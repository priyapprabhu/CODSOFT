''' Design a simple calculator with basic arithmetic operations. Prompt the user to input 2 numbers
and an operation choice. Perform the calculation and display the result.'''

def calculator():
    num1= int(input("Enter the 1st number:"))
    num2= int(input("Enter the 2nd number:"))

    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice= int(input("Enter your choice:"))

    if choice == 1:
        result = num1 + num2
    elif choice == 2:
        result = num1 - num2
    elif choice == 3:
        result = num1 * num2
    elif choice == 4:
        if num2!=0:
            result = num1 / num2
        else:
            print("Error")

    else:
        print("Invalid choice")
        return
    
    print("The result is:", result)

calculator()