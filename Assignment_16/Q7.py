# 7. Write a program which contains one function that accept one number from user and returns
# true if number is divisible by 5 otherwise return false.
# Input : 8 Output : False
# Input : 25 Output : True

def Fun(no):
    return no % 5 == 0
        
def main():
    x = int(input("Enter the number : "))
    ret = Fun(x)
    print(ret)
    
if __name__=="__main__":
    main()