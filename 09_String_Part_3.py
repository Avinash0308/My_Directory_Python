a = "Avi, Avi, Avi!!!!!"
print(len(a))  # Strings are immutable ie they can't be changed
# We will get new string using this lower function which will have all the characters in lowercase
print(a.lower())
b = a.lower()
print(a, b)
# We will get new string using this upper function which will have all the charcaters in uppercase
print(a.upper())
print(a)
b = a.rstrip("!")
print(a, b)
print(a.rstrip("!"))  # Remove the terminating same characters
# Replace the occurence of given word with the new word
print(a.replace("Avi", "Tulsi"))
# This function will change the string in form of list by splitting the string on the basis of given character here it is space and we can choose any other caharacter also .
print(a.split(" "))
john = "and his name is john cena"
# This function will make the first character of string to capital and all other to lowercase
print(john.capitalize())
# This function will help to give spacing to the print statement on the basis of width given
print(john.center(50))
print(len(john), len(john.center(50)))
# This function will count the number of occurence of given keyword in the string
print(a.count("Avi"))
print(a.count("Tulsi"))
# This function will check whether the given string ends with the entered the keyword or not and this function returns bool datatype
print(a.endswith("!!!"))
# This function is used to check the functionality of endswith with given range or we can say that this function will check that the substring is ending with given keyword or not
print(a.endswith("vi", 4, 10))
the = "hello everyone my name is avinash agrawal , I'm a student of AKS university , Satna and studying uder B.Tech course under cse branch that is it for today guys we will meet in next video with some new topics till then bye bye"
print(the.find("a"))  # This function will return the index of the first occurence of the given keyword in the string and if the keyword is not present in the string it will print -1
print(the.index("a"))  # This function is almost same as the find function the only difference is instead of printing -1 it will throw an error if the given keyword is not present in the string
alphanum = "Hello everyone my name is avinash agrawal and my age is 19"
print(alphanum.isalnum())  # This function is used to check whehter the given string is purely alphanumeric or not if there is any special character or spaces in the string it will return false as in above case
an = "thisisyourboybadshah"
print(an.isalnum())
print(an.isalpha())  # This function is used to check whether given string is purely alphabatically made or not ie it contains only alphabets of lowercase and uppercase only and not even numbers
print(an.islower())  # This function is used to check whether given string is purely in lowrecase or not also it allows numbers and special characters in the string
# This function returns true if all the characters in the string is printable else false
print(an.isprintable())
ab = "3df\ffdd"
print(ab.isprintable())
ab = "    "
# If the string only contains whitespaces it will return true else false;
print(ab.isspace())
ab = "                  dfd"
print(ab.isspace())
# This function return true if all the words in the string starts with capital letter ie if the string is written in title language it will return true else false..
print(ab.istitle())
title = "My Name Is Avinash Agrawal And That Is It For Today Guys"
print(title.istitle())
print(title.startswith("my"))  # This function return true if the given string starts with mentioned keyword else it will return false also the lowercase and uppercase letters are different here and they can't be considered equal
print(title.startswith("My "))
# This string is used to convert the lowercase letters to the uppercase and uppercase to lowercase ie it swap the cases of the alphabets.
print(title.swapcase())
title2 = "And this is really something new"
# This function convets the string into title case ie the first alphabet of each and every word will be in uppercase
print(title2.title())
