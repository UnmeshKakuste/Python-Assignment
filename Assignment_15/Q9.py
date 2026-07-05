# 9. Write a lambda function using reduce() which accepts a list of numbers and returns the product of all
# elements.

from functools import reduce

def main():
    Data = [1,2,3,4,5]
    print("Input data is : ",Data)
    
    RData = reduce(lambda x,y : x * y , Data )
    
    print("Product of all elements :",RData)
    
if __name__=="__main__":
    main()