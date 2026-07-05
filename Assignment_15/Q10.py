# 10.Write a lambda function using filter() which accepts a list of numbers and returns the count of even
# numbers.

def main():
    Data = [1,2,3,4,5,6,7,8,9,10,22,24,71,222,444,13,14]
    print("Input data is : ",Data)
    
    FData = list(filter(lambda x: x % 2 == 0  , Data ))
    
    print("Count of even numbers :",len(FData))
    
if __name__=="__main__":
    main()