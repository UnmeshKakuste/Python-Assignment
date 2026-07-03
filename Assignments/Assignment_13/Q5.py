# 5. Write a program which accepts marks and displays grade.
# Condition Example:
# • ≥ 75 → Distinction
# • ≥ 60 → First Class
# • ≥ 50 → Second Class
# • < 50 → Fail

def display_grade(marks):
    if marks >= 75:
        print("Distinction")
    elif marks >= 60:
        print("First Class")
    elif marks >= 50:
        print("Second Class")
    else:
        print("Fail")
    
    
def main():
    no = int(input("Enter number : "))
    
    display_grade(no)
        
if __name__ == "__main__":
    main()