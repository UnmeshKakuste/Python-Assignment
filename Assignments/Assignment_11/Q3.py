# 3. Write a program which accepts one number and prints sum of digits.
# Input: 123
# Output: 6


def total(no):
    store = 0
    
    while no>0:
        digit = no % 10
        no = no // 10
        store += digit
    
    return store
    
    
def main():
    No = int(input("Enter number : "))
    
    ret = total(No)
    print(ret)
    
if __name__ == "__main__":
    main()