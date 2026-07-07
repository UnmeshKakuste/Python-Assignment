# 2. Write a program which contains one function named as ChkNum() which accept one
# parameter as number. If number is even then it should display “Even number” otherwise
# display “Odd number” on console.
# Input : 11 Output : Odd Number
# Input : 8 Output : Even Number

def ChkNum(no):
    return no % 2 == 0
    
def main():
    no = int(input("Enter the number : "))
    ret = ChkNum(no)
    if ret:
        print("Even number")
        
    else:
        print("Odd number")
if __name__=="__main__":
    main()