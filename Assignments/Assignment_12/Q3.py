# 3. Write a program which accepts two numbers and prints addition, subtraction,
# multiplication and division.

def Addition(no1 , no2):
    return no1 + no2

def Subtraction(no1 , no2):
    return no1 - no2

def Multiplication(no1 , no2):
    return no1 * no2

def Division(no1 , no2):
    return no1 / no2
    
    
def main():
    no1 = int(input("Enter 1st number : "))
    no2 = int(input("Enter 2nd number : "))
    
    ret1 = Addition(no1,no2)
    print("Addition is : ",ret1)
    
    ret2 = Subtraction(no1,no2)
    print("Subtraction is : ",ret2)
    
    ret3 = Multiplication(no1,no2)
    print("Multiplication is : ",ret3)
    
    ret4 = Division(no1,no2)
    print("Division is : ",ret4)
    
    
if __name__ == "__main__":
    main()