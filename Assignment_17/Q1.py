# 1.Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
# for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
# parameters as number and perform the operation. Write on python program which call all the
# functions from Arithmetic module by accepting the parameters from user.

import Arithmetic
def main():
    no1 = int(input("Enter the 1st number : "))
    no2 = int(input("Enter the 2nd number : "))

    ret1 = Arithmetic.Add(no1,no2)
    print("Addition is :",ret1)
    
    ret2 = Arithmetic.Sub(no1,no2)
    print("Subtraction is :",ret2)
    
    ret3 = Arithmetic.Mult(no1,no2)
    print("Multiplication is :",ret3)
    
    ret4 = Arithmetic.Div(no1,no2)
    print("Division is :",ret4)
    
if __name__=="__main__":
    main()