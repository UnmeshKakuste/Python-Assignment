# 5.Write a program which accept one number for user and check whether number is prime or not.
# Input : 5 Output : It is Prime Number

def prime(no):
    if no <= 1:
        return "Not a prime number"
    
    for i in range(2,no):
        if (no % i == 0):
            return "Not a prime number"
    else:
        return "Prime number"
 
def main():
    no = int(input("Enter the number : "))
    ret = prime(no)
    print(ret)

if __name__=="__main__":
    main()
