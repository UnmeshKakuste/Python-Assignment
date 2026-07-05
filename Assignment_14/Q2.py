# 2. Write a lambda function which accepts one number and returns cube of that number.


Cube =  lambda no : no * no * no

def main():
    no = int(input("Enter the number : "))
    ret = Cube(no)
    print(ret)
    
if __name__ == "__main__":
    main()