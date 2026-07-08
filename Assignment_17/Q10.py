# 10. Write a program which accept number from user and return addition of digits in that number.
# Input : 5187934 Output : 37

def addition_of_digits(no):
    count = 0
    
    # no = str(no)
    # for i in no:
    #     count += int(i)
    
    while no > 0:
        count += no%10
        no = no//10
        
    return count
    
def main():
    no = int(input("Enter the number : "))
    ret = addition_of_digits(no)
    print(ret)

if __name__=="__main__":
    main()