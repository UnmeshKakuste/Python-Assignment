# 1.Write a program which accept N numbers from user and store it into List. Return addition of all
# elements from that List.
# Input : Number of elements : 6
# Input Elements : 13 5 45 7 4 56
# Output : 130

def addition(no):
    Marks = []
    for i in range(no):
        Marks.append(int(input()))
    print("Input Elements :",Marks)
    Sum = 0
    for i in Marks:
        Sum = Sum+i
    print("Addition is : " ,Sum)


def main():
    
    no =int(input("Enter the no :"))
    addition(no)
    
    
if __name__=="__main__":
    main()