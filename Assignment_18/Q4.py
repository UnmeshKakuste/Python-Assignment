# 4.Write a program which accept N numbers from user and store it into List. Accept one another
# number from user and return frequency of that number from List.
# Input : Number of elements : 11
# Input Elements : 13 5 45 7 4 56 5 34 2 5 65
# Element to search : 5
# Output : 3


def frequency(no):
    Marks = []
    for i in range(no):
        Marks.append(int(input()))
        
    print("Input Elements :",Marks)
    return Marks
    
def Search(Marks,search):
    count = 0
    for i in Marks:
        if search == i:
            count += 1
    return count


def main():
    
    no =int(input("Number of elements :"))
    Marks =frequency(no)
    search = int(input("Element to search :"))
    ret2 = Search(Marks,search)
    print("Output :",ret2)
    
    
if __name__=="__main__":
    main()