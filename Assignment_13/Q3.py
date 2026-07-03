# 3. Write a program which accepts one number and checks whether it is perfect number or
# not.
# Input: 6
# Output: Perfect Number


def perfect_number(no):
    
    store = 0
    
    for i in range(1, no):
        if no % i == 0:
            store += i
    return store == no
            
    
def main():
    no = int(input("Enter number : "))
    
    ret = perfect_number(no)
    if ret:
        print("Perfect number" )
    else:
        print("not a perfect number")
        
if __name__ == "__main__":
    main()