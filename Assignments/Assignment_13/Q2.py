# 2. Write a program which accepts radius of circle and prints area of circle.

def area_circle(radius):
    return 3.14 * radius * radius
    
def main():
    radius = int(input("Enter radius : "))
    
    ret = area_circle(radius)
    print("Area of circle is ", ret)
        
if __name__ == "__main__":
    main()