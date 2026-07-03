# 1. Write a program which accepts one number and prints multiplication table of that
# number.
# Input: 4
# Output:
# 4 8 12 16 20 24 28 32 36 40

def table(no):
    for i in range(1,11):
        print(no * i , end=" ")
    
def main():
    No = int(input("Enter the number : "))
    
    table(No)

if __name__ == "__main__":
    main()