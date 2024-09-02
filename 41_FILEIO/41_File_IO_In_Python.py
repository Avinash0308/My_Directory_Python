'''

READING FILE

f = open('41_FILEIO/myfile.txt','r')
#r is deafault mode
# print(f)
text = f.read()
print(text)
f.close()

f = open('41_FILEIO/myfile2.txt','w') #creates new file if not exist, deletes all previous data

f = open('41_FILEIO/myfile3.txt','a') #similar to 'w' but not delete previous data.

#f = open('41_FILEIO/myfile.txt','x') #creates new and give error if already exit.
# f = open('41_FILEIO/myfile4.txt','x')

f = open('41_FILEIO/myfile.txt','rt') #t after mode defines the way we are opening the file, t means text file

text = f.read()
print(text)

f = open('41_FILEIO/myfile.txt','rb') #b for binary mode

text = f.read()
print(text)

f.close()

'''


#WRITING FILE

f = open("41_FILEIO/myfile2.txt",'w')
f.write("OHSDfi")
f.close()

f = open("41_FILEIO/myfile2.txt",'a')
f.write("OHSDOFHO")
f.close()

with open('41_FILEIO/myfile3.txt','a') as f:
    f.write("oihotlijdfoslj")