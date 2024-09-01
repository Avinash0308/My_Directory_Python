#Write a program to translate a message into secret code language. Use the rules below to translate normal english into secret code language.

#coding:
# If the word contains atleast 3 characters, remove the first letter and append it at the end now append three random characters at the starting and the End 
# else simply reverse the SyntaxWarning

# decoding:
# if the word contains less than 3 characters reverse iter
# else remove 3 random characters from start and end. Now remove the last letter and append at the beginning.
import string
import random
def encode(a):
    if len(a)<3:
        return "".join(reversed(a))
    else:
        a = a + a[0]
        n = 3
        ran ="".join(random.choices(string.ascii_letters,k = n))
        a = a[1:]
        a = ran + a + ran
        return a
    
def decode(a):
    if len(a)<3:
        return "".join(reversed(a))
    else:
        a = a[3:-3]
        c = a[-1]
        a = c + a
        a = a[:-1]
        return a
    
a = input("Please enter your name: ")
a = encode(a)
print(a)
print(decode(a))