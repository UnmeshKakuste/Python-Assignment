# 3. Write a lambda function which accepts two numbers and returns maximum number.

Maximum =  lambda no1,no2 : no1 > no2

def main():
    no1 = int(input("Enter the 1st number : "))
    no2 = int(input("Enter the 2nd number : "))
    
    ret = Maximum(no1,no2)
    if ret:
        print("Maximum number is :", no1)
    else:
        print("Maximum number is :", no2)
    
if __name__ == "__main__":
    main()