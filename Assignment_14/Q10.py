# 10. Write a lambda function which accepts three numbers and returns largest number.

# Largest = lambda no1 , no2 , no3 : max(no1,no2,no3)

Largest = lambda no1 , no2 , no3 : no1 if no1 > no2 and no1 > no3 else(no2 if no2 > no3 else no3)  

def main():
    no1 = int(input("Enter the 1 st number : "))
    no2 = int(input("Enter the 2 nd number : "))
    no3 = int(input("Enter the 3 rd number : "))
    
    ret = Largest(no1,no2,no3)
    print(f"Largest is {ret}")
    
if __name__ == "__main__":
    main()
