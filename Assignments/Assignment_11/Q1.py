# 1. Write a program which accepts one number and checks whether it is prime or not.
# Input: 11
# Output: Prime Number


def prime_no(no):
    
    for i in range(2,no):
        if no % i == 0:
            print("Not a Prime Number")
            return
    print("Prime Number.")
            
def main():
    No = int(input("Enter the number : "))
    
    prime_no(No)
    
    
if __name__ == "__main__":
    main()