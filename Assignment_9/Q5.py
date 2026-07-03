def div(no):
    return no%3==0 and no%5==0
def main():
    No = int(input("Enter the number : "))
    
    if div(No):
        print("Divisible by 3 and 5. ")
    else:
        print("NA")
    
if __name__=="__main__":
    main()



# def div(no):
#     if no%3==0 and no%5==0:
#         print("Divisible by 3 and 5")
#     else:
#         print("NA")
# def main():
#     No = int(input("Enter the number : "))
    
#     div(No)
    
# if __name__=="__main__":
#     main()