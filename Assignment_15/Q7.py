# 7. Write a lambda function using filter() which accepts a list of strings and returns a list of strings
# having length greater than 5.

def main():
    Data = ["ox","elephant","tree","spaceship","banana","apple","pyramid"]
    print("Input data is : ", Data)
    
    FData = list(filter(lambda no : len(no) > 5 , Data))
    print("Strings having length greater than 5 :", FData)
    
if __name__ == "__main__":
    main()
