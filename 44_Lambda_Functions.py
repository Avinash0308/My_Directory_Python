# def double(x):
#     return x*2

def appl(fx,value):
    return 6 + fx(value)

double = lambda x:x*2
cube = lambda x: x**3
avg = lambda x,y: (x+y)/2
avg3 = lambda x,y,z: (x+y+z)/3

print(double(5))
print(cube(5))
print(avg(3,4))
print(avg3(3,5,10))
print(appl(cube,2))
print(appl(lambda x: x**3,2))