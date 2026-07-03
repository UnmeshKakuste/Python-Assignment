# 5.Write a program which accepts one number and prints all odd numbers till that number.

def odd(no):
    
    for i in range(1, no+1):
        if i % 2 == 1:
            print(i , end=" ")
    
def main():
    No = int(input("Enter the number : "))
    
    odd(No)
    
if __name__ == "__main__":
    main()