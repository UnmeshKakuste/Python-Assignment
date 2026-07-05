# 1. Write a lambda function using map() which accepts a list of numbers and returns a list of squares of
# each number.

def main():
    Data = [1,2,3,4,5,6,7,8,9,10]
    print("Input data is : ", Data)
    
    MData = list(map(lambda no : no * no,Data))
    print(f"squares of each number is :", MData)
    
if __name__ == "__main__":
    main()
