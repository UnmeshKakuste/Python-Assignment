# 2. Write a program which accepts one number and prints its factors.
# Input: 12
# Output: 1 2 3 4 6 12

def factors(no):
    for i in range(1 , no+1):
        if no % i == 0:
            print(i , end=" ")
    
def main():
    no = int(input("Enter number : "))
    
    factors(no)
    
    
if __name__ == "__main__":
    main()