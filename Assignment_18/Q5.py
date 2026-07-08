# 5.Write a program which accept N numbers from user and store it into List. Return addition of all
# prime numbers from that List. Main python file accepts N numbers from user and pass each
# number to ChkPrime() function which is part of our user defined module named as
# MarvellousNum. Name of the function from main python file should be ListPrime().
# Input : Number of elements : 11
# Input Elements : 13 5 45 7 4 56 10 34 2 5 8
# Output : 54 (13 + 5 + 7 +2 + 5)

import MarvellousNum

def ListPrime(Marks):
    Sum = 0

    for i in Marks:
        if MarvellousNum.ChkPrime(i):
            Sum += i

    return Sum


def main():
    
    no =int(input("Number of elements :"))
    
    Marks = []
    for i in range(no):
        Marks.append(int(input()))
    
    ret = ListPrime(Marks)

    print("Addition of prime numbers :", ret)
   
    
if __name__=="__main__":
    main()