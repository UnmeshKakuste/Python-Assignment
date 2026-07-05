# 8. Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers
# divisible by both 3 and 5.

def main():
    Data = [100,30,63,45,55,60,74,83,90,15]
    print("Input data is : ", Data)
    
    RData = list(filter(lambda x:  x % 3 == 0 and x % 5 == 0, Data))
    print("List of numbers divisible by both 3 and 5 :", RData)
    
if __name__ == "__main__":
    main()