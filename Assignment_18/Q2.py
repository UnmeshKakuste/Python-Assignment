# 2.Write a program which accept N numbers from user and store it into List. Return Maximum
# number from that List.

def maximum(no):
    Marks = []
    for i in range(no):
        Marks.append(int(input()))
        
    print("Input Elements :",Marks)
    return max(Marks)


def main():
    
    no =int(input("Number of elements :"))
    ret =maximum(no)
    print("Max is : ",ret)
    
if __name__=="__main__":
    main()