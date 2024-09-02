# # f = open("43_FILEIO/myfile.txt",'w')
# with open("43_FILEIO/myfile.txt",'r') as f:
#     print(type(f))
#     #move to 10th byte in file
#     f.seek(10)

#     #read the next 5 bytes
#     print(f.tell())
#     data = f.read(5)
#     print(data)

with open('43_FILEIO/myfile1.txt','w') as f:
    f.write("Hellow World!")
    f.truncate(7)

with open('43_FILEIO/myfile1.txt','r') as f:
    print(f.read())