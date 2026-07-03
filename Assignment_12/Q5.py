# 5. Write a program which accepts one number and prints that many numbers in reverse
# order.
# Input: 5
# Output: 5 4 3 2 1


def Reverse_Numbers(no):
    for i in range(no,0,-1):
        print(i , end = " ")
    
def main():
    no = int(input("Enter number : "))
    
    Reverse_Numbers(no)
    
if __name__ == "__main__":
    main()