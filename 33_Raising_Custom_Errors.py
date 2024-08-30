# a = int(input("Enter any value between 5 & 9: "))
# if(a<5 or a>9):
#     raise ValueError("Vlaue should be between 5 and 9")

#quick quiz
a = input("Enter any value between 5 & 9: ")
try:
    if(int(a)<5 or int(a)>9):
        raise ValueError("Vlaue should be between 5 and 9")
    else:
        print("Well Done")
except:
    if a == "quit" :
        print("Quiting....")
    else:
        raise ValueError("Value should be integer")
