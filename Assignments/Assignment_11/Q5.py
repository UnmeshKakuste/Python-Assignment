# 5. Write a program which accepts one number and checks whether it is palindrome or not.
# Input: 121
# Output: Palindrome

def Palindrome(no):
    store = 0
    x = no
    
    while no > 0:
        store = store*10 + no%10
        no = no//10
        
    if store == x:
        print("Palindrome")
    else:
        print("Not a Palindrome")

    
def main():
    No = int(input("Enter number : "))
    
    Palindrome(No)
    # print(ret)
    
if __name__ == "__main__":
    main()
    