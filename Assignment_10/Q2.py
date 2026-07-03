# 2. Write a program which accepts one number and prints sum of first N natural numbers.
# Input: 5
# Output: 15


def sum(no):
    sum = 0
    for i in range(no+1):
        sum = sum + i
    print(sum)
    
def main():
    No = int(input("Enter the number : "))
    
    sum(No)

if __name__ == "__main__":
    main()