# 4. Write a program which accepts one number and prints that many numbers starting
# from 1.
# Input: 5
# Output: 1 2 3 4 5


def Numbers(no):
    for i in range(1,no+1):
        print(i , end = " ")
    
def main():
    no = int(input("Enter number : "))
    
    Numbers(no)
    
if __name__ == "__main__":
    main()