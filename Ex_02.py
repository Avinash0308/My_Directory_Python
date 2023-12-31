import time
tame = time.strftime('%H:%M:%S')
print("The current time is",tame)
tame = int(time.strftime('%H'))
if(tame >= 0 and tame < 12):
    print("Good Morning Sir")
elif(tame>=12 and tame<18):
    print("Good Afternoon Sir")
else:
    print("Good Evening Sir")
