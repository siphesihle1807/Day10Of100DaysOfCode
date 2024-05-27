logo = """
 _____________________
|  _________________  |
| | Siphe's Maths  0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


# Functions of how the operations work.
def sum(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def product(num1, num2):
    return num1 * num2

def quotient(num1, num2):
    if num2 == 0:
        return "Division by zero is undefined."
    return num1/num2

#contains the operations the calculator can perform
mathematical_operands = (
    "+ : add num1 and num2 given.\n- : subtracts num2 from num1 given.\n* : multiplies num1 and num1 given.\n/ : divides num1 by num2 given."
)
def welcome():
    print(logo)
    print("Welcome to Siphe's Maths...") 
    user_help = input("Before we start, type 'help' to see the operations this calculator can do. ")
    if user_help.lower() == "help":
       print(mathematical_operands)
    else:
        print("Seems like you know just what to do ;), you cam go right ahead.")
        
def calculations():
    welcome()
    num1 = float(input("Enter the first number: "))
    continue_math = True
 
    while continue_math:
        math_operand = input("From the operands provided, which would you like to use: ")
                
        if math_operand == "+":
            num2 = float(input("Enter the second the number: "))
            result =  sum(num1, num2)
        elif math_operand == "-":
            num2 = float(input("Enter the second the number: "))
            result = subtract(num1, num2)
        elif math_operand == "*":
            num2 = float(input("Enter the second the number: "))
            result = product(num1, num2)
        elif math_operand == "/":
            num2 = float(input("Enter the second the number: "))
            result = quotient(num1,num2)
        else:
            print("Invalid operand selected")
            continue
        
        print(f"The result of {num1} {math_operand} {num2} is = {result}.")
        
        continue_math = input("Would you like to continue the calculations?: y/n ")
        if continue_math.lower() == "y":
            num1 = result
        else:
            continue_math =False
            print("Thank you for using Siphe's Maths. Goodbye!")
       
       
        

 
    
calculations()