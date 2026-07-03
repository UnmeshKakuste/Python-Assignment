# 4. Write a program which accepts one number and prints binary equivalent.

def binary(no):
    s=""
    while no > 0:
        rem = no % 2
        s = str(rem) + s
        no = no//2
    return s
        
    
def main():
    no = int(input("Enter number : "))
    
    ret = binary(no)
    print(ret)
        
if __name__ == "__main__":
    main()