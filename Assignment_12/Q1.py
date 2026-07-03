# 1. Write a program which accepts one character and checks whether it is vowel or
# consonant.
# Input: a
# Output: Vowel

# def vowel(char):
#     if char == "A" or char == "a" or char == "E" or char == "e" or char == "I" or char == "i" or char == "O" or char == "o" or char == "U" or char == "u":
#         print("vowel")
#     else:
#         print("Consonant")


def vowel(char):
    if char in "AEIOUaeiou":
        print("vowel")
    else:
        print("Consonant")
    
def main():
    char = input("Enter charcter : ")
    
    vowel(char)
    
    
if __name__ == "__main__":
    main()