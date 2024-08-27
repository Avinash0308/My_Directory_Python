# create a program capable of displaying questions to the user like KBc
# use list data type to store the questions and their answer
# Display the final amount the person is taking home after playing the game

list_ques = ["Who is the pm of India?", "What is your name", "Bas"]
list_ans = ["Narendra Modi", "Avinash Agrawal", "Ho Gaya"]

total = 0
cur = 0
for i in list_ques:
    print(i)
    a = input("Enter Your Answer ")
    if a == list_ans[cur]:
        print("congrats it's a correct answer")
    else:
        print("It's wrong, better luck next time")
        break
    total += 1
    cur += 1
print("your total earning is", total*1000)
