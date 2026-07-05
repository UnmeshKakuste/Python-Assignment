# 7. Write a lambda function which accepts one number and returns True if divisible by 5.

Check_Divisible = lambda no : no % 5 == 0

def main():
    no = int(input("Enter the number : "))
    
    ret = Check_Divisible(no)
    print(ret)
    
if __name__ == "__main__":
    main()
