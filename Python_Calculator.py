
def main():
    # stores op as a global var
    global op
    global many
    print("Welcome to a more advanced Calculator")
    print("What operator are you wanting to use?")

    # Main will call these classes in order
    operator()
    howmany()

    

def operator():
    global op
    op = float(input(" 1. Addition \
           2. Mulitplication \
           3. Division \
           4. Subtraction \n"))
    if op == 1:
        #addition
        print("Additon Selected")
    elif op == 2:
        #multiplication
        print("Multiplication Selected")
    elif op == 3:
        #division
        print("Divison Selected")
    elif op == 4:
        #subtraction
        print("Subtraction Selected")
    else:
        print("Invalid operator")
        print("Try Again")
        operator()
        
        
def howmany():
    global many
    # Takes the input of how many nunbers 
    many = int(input("How Many Numbers? 2-4\n"))
    if many == 2:
        two()
    elif many == 3:
        three()
    elif many == 4:
        four()
    else: 
        if many> 3:
         print("Invalid operator")
         print("Try Again")
        howmany()
            

def two():
    global op
    if op == 1:
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))
        add_result= num1 + num2
        print(add_result)
    elif op == 2:
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))
        add_result= num1 * num2
        print(add_result)
    elif op == 3:
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))
        add_result= num1 / num2
        print(add_result)
    elif op == 4:
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))
        add_result= num1 - num2
        print(add_result)
    else:
        print("Invalid entry")
        print("Try Again")
        two()

def three():
    global op
    if op == 1:
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))
        num3 = float(input("Enter Third Number: "))
        add_result= num1 + num2 + num3
        print(add_result)
    elif op == 2:
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))
        num3 = float(input("Enter Third Number: "))
        add_result= num1 * num2 *num3
        print(add_result)
    elif op == 3:
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))
        num3 = float(input("Enter Third Number: "))
        add_result= num1 / num2 / num3
    elif op == 4:
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))
        num3 = float(input("Enter Third Number: "))
        add_result= num1 - num2 - num3 
        print(add_result)
    else:
        print("Invalid entry")
        print("Try Again")
        three()
        
def four():
    global op
    if op == 1:
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))
        num3 = float(input("Enter Third Number: "))
        num4 = float(input("Enter Fourth Number: "))
        add_result= num1 + num2 + num3 + num4
        print(add_result)
    elif op == 2:
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))
        num3 = float(input("Enter Third Number: "))
        num3 = float(input("Enter Fourth Number: "))
        add_result= num1 * num2 *num3 * num4
        print(add_result)
    elif op == 3:
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))
        num3 = float(input("Enter Third Number: "))
        num4 = float(input("Enter Fourth Number: "))
        add_result= num1 / num2 / num3 / num4
        print(add_result)
    elif op == 4:
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))
        num3 = float(input("Enter Third Number: "))
        num4 = float(input("Enter Fourth Number: "))
        add_result= num1 - num2 - num3 - num4
        print(add_result)
    else:
        print("Invalid entry")
        print("Try Again")
        four()
# Calls Main
main()