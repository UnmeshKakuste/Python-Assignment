# 6. Write a lambda function which accepts one number and returns True if number is odd
# otherwise False.

Odd_no = lambda no : no % 2 != 0

def main():
    no = int(input("Enter the number : "))
    
    ret = Odd_no(no)
    print(ret)
if __name__ == "__main__":
    main()
