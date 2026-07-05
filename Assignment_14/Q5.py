# 5. Write a lambda function which accepts one number and returns True if number is even
# otherwise False.

Even_no = lambda no : no % 2 == 0

def main():
    no = int(input("Enter the number : "))
    
    ret = Even_no(no)
    print(ret)
    
if __name__ == "__main__":
    main()
