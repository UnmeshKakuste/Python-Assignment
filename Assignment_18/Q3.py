# 3.Write a program which accept N numbers from user and store it into List. Return Minimum
# number from that List.
# Input : Number of elements : 4
# Input Elements : 13 5 45 7
# Output : 5

def Minimum(no):
    Marks = []
    for i in range(no):
        Marks.append(int(input()))
        
    print("Input Elements :",Marks)
    return min(Marks)


def main():
    
    no =int(input("Number of elements :"))
    ret =Minimum(no)
    print("Minimum is : ",ret)
    
if __name__=="__main__":
    main()