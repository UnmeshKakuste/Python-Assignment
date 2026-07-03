def square(no):
    return no*no
def main():
    No = int(input("Enter the number : "))
    
    ret = square(No)
    print("Square : ",ret)
    
if __name__=="__main__":
    main()