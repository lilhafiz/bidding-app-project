while True:
    first_number = float(input("Enter the first number: "))  
    second_number = float(input("Enter the second number: ")) 
    operation = input("Enter the operation (+, -, *, /): ")  
    
    if operation == '+':
        result = first_number + second_number
    elif operation == '-':
        result = first_number - second_number
    elif operation == '*':
        result = first_number * second_number
    elif operation == '/':
        if second_number != 0:
            result = first_number / second_number
        else:
            result = "Error! Division by zero."
    else:
        result = "Invalid operator."

    print(f"The result of {first_number} {operation} {second_number} is: {result}")
    
    continue_calculation = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if continue_calculation != 'yes':
        print("Goodbye!")
        break
#Umar Ahmad Garba