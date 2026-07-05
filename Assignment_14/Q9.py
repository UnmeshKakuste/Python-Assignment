# 9. Write a lambda function which accepts two numbers and returns multiplication.

Multiplication = lambda no1 , no2 : no1 * no2

def main():
    no1 = int(input("Enter the 1 st number : "))
    no2 = int(input("Enter the 2 nd number : "))
    
    ret = Multiplication(no1,no2)
    print(f"Multiplication is {ret}")
    
if __name__ == "__main__":
    main()
