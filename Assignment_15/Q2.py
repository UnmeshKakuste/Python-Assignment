# 2. Write a lambda function using filter() which accepts a list of numbers and returns a list of even
# numbers.


def main():
    Data = [1,2,3,4,5,6,7,8,9,10]
    print("Input data is : ", Data)
    
    FData = list(filter(lambda no : no % 2 == 0 , Data))
    print(f"Even numbers :", FData)
    
if __name__ == "__main__":
    main()
