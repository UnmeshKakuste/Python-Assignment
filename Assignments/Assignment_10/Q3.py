# 3. Write a program which accepts one number and prints factorial of that number.
# Input: 5
# Output: 120

def factorial(no):
    fac = 1
    for i in range(1, no+1):
        fac = fac * i
    return fac
    
def main():
    No = int(input("Enter the number : "))
    
    ret = factorial(No)
    print(ret)

if __name__ == "__main__":
    main()