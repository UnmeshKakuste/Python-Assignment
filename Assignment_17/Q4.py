# 4.Write a program which accept one number form user and return addition of its factors.
# Input : 12 Output : 16 (1+2+3+4+6)

def factors_addition(no):
    count = 0
    for i in range(1,no):
        if no % i == 0:
            count += i
    return count
    
def main():
    no = int(input("Enter the number : "))
    ret = factors_addition(no)
    print(ret)

if __name__=="__main__":
    main()