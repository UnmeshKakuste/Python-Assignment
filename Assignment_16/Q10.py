# 10. Write a program which accept name from user and display length of its name.
# Input : Marvellous Output : 10

def display(no):
        return len(no)
                    
def main():
    x = input("Enter the name : ")
    
    ret = display(x)
    print(ret)
    
if __name__=="__main__":
    main()