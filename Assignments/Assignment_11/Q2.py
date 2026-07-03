# 2.Write a program which accepts one number and prints count of digits in that number.
# Input: 7521
# Output: 4

def count(no):
    total = 0
    
    while no > 0:
        total += 1
        no = no // 10
        
    return total

def main():
    No = int(input("Enter the number : "))
    ret = count(No)
    print(ret)
    
if __name__ == "__main__":
    main()