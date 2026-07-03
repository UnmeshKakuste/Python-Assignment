# 1. Write a program which accepts length and width of rectangle and prints area.

def area(no1,no2):
    return no1 * no2
    
def main():
    no1 = int(input("Enter length : "))
    no2 = int(input("Enter width : "))
    
    ret = area(no1,no2)
    print("Area of rectangle is ", ret)
        
if __name__ == "__main__":
    main()