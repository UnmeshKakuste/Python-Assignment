def cube(no):
    return no*no*no
def main():
    No = int(input("Enter the number : "))
    
    ret = cube(No)
    print("cube : ",ret)
    
if __name__=="__main__":
    main()