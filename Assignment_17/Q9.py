# 9. Write a program which accept number from user and return number of digits in that number.
# Input : 5187934 Output : 7

def digits(no):
    no = str(no)
    return len(no)
    
def main():
    no = int(input("Enter the number : "))
    ret = digits(no)
    print(ret)

if __name__=="__main__":
    main()