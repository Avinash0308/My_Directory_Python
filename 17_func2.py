def avg(a=3,b=2):
    print("The average is",(a-b)/2)
avg()
avg(6)
avg(b=6)
avg(3,2)
avg(b=234,a=3)
def aver(*numbers):
    sum = 0
    for i in numbers:
        sum = sum+i
    print("Avg is",sum/len(numbers))
aver(2,6,3,2,2,5,4,1,35,9,35)
def avg2(a,b):
    return (a+b)/2
m = avg2(2,5)
print(m)