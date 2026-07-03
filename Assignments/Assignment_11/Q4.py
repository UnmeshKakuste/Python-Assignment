# 4. Write a program which accepts one number and prints reverse of that number.
# Input: 123
# Output: 321


def rev(no):
    store = 0
    
    while no > 0:
        store = store*10 + no%10
        no = no//10
    return store
    
def main():
    No = int(input("Enter number : "))
    
    ret = rev(No)
    print(ret)
    
if __name__ == "__main__":
    main()
    
