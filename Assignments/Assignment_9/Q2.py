def ChkGreater(V1,V2):
    if V1 > V2:
        print( V1 ,"is greater. ")
    elif(V1 == V2):
        print("Both are equal.")
    else:
        print(V2 , "is greater.")

def main():
    No1 = int(input("Enter 1st number : "))
    No2 = int(input("Enter 2nd number : "))
    
    ChkGreater(No1 , No2)

if __name__=="__main__":
    main()