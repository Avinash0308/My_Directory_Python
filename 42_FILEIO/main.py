# f = open("42_FILEIO/myfile.txt",'r')
# while True:
#     line = f.readline()
#     # print(line,type(line))
#     if not line:
#         break
#     print(line)
# f.close()

# f = open("42_FILEIO/myfile1.txt",'r')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
#     print(m1, m2, m3)

f = open("42_FILEIO/myfile.txt",'r')
while True:
    line = f.readline()
    # print(line,type(line))
    if not line:
        break
    print(line)
f.close()

f = open("42_FILEIO/myfile2.txt",'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close