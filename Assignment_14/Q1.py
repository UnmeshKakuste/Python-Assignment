# 1. Write a lambda function which accepts one number and returns square of that number.

Square =  lambda no : no * no 

def main():
    no = int(input("Enter the number : "))
    ret = Square(no)
    print(ret)
    
if __name__ == "__main__":
    main()