# 8. Write a program which accept number from user and print that number of “*” on screen.
# Input : 5 Output : * * * * *

def Fun(no):
    for i in range(no):
        print("*", end=" ")
        
def main():
    x = int(input("Enter the number : "))
    Fun(x)
    
if __name__=="__main__":
    main()