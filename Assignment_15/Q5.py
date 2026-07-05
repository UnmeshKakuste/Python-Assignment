# 5. Write a lambda function using reduce() which accepts a list of numbers and returns the maximum
# element.

from functools import reduce

def main():
    Data = [100,34,300,4,55,2,74,83,9,10]
    print("Input data is : ", Data)
    
    RData = reduce(lambda x, y : x if x > y else y , Data)
    print(f"Maximum element :", RData)
    
if __name__ == "__main__":
    main()
