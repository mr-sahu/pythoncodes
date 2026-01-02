# print("hello, SAHU JI");
# print("This is my first program");
#**********
# a=5;
# print(a);
# nums=input("Enter a number");
# print(f"Your entered number is ${nums}");
#******************* Basics *****************************
#Q1.Add two numbers entered by the user.
""" num1=float(input("Please enter your first number"));
num2=float(input("Please enter your second number"));
sums=float(num1+num2);
print(f"sum of both numbers is {sums}"); """
# Q2. Swap two numbers using a temporary variable.
""" swpnum1=45;
swpnum2=50;
swpval=swpnum1;
swpnum1=swpnum2;
swpnum2=swpval;
print(f"first swap value that was {swpnum1}");
print(f"second  swap value that was {swpnum2}"); """
""" # Q3. Swap two numbers without a temporary variable.
n1=25.0
n2=26.0
print(f"numbers before swaping are {n1} and {n2}");
n1=n1+n2;
n2=n1-n2;
n1=n1-n2;
print(f"first num is after swap is {n1} second num is {n2}"); """

# **************** Data Types and Operators ***************
# Q1.Check the type of a variable.
""" nums=input("Enter a number");
print(type(nums));
nums2=int(input("Enter a number"));
print(type(nums2)); """
""" # Q2.Use arithmetic operators (+, -, *, /, %, //, **).
f3=float(input("Enter first number"));
f4=float(input("Enter second number"));
divi=f3/f4;
print(F"Result {divi}"); """

""" #Q3. Calculate the area of a circle (given radius).
radi=float(22);
area=3.14*radi**2;
print(F"area of circle will be {area}"); """

""" #Q1.Calculate simple interest.
p=float(3000);
r=float(5);
t=float(3.5);
si=(p*r*t)/100;
print(f"Simple intrest of Principal of rs {p} with rate of {r}% in time {t} years is {si}");
 """

# **************** Conditional Statements *****************
""" #Q1. Check if a number is even or odd.
checknum=float(input("Enter a number "));
if(checknum%2==0){
    print("Number is even");
}
else{
     print("Number is odd");
} """

""" #Q2.Check if a number is positive, negative, or zero.
checkn=float(input("Enter number "));
if checkn>0:
    print("entered number is positive");
elif checkn<0:
    print("entered number is negative ");
else:
    print("entered number is 0"); """

""" #Q1.Find the largest among 3 numbers.
checkf1=float(input("Enter first number "));
checkf2=float(input("Enter second number "));
checkf3=float(input("Enter third number "));
if (checkf1 > checkf2) & (checkf1>checkf3):
    print(f"{checkf1} is greatest");
elif (checkf2 > checkf1) & (checkf2>checkf3):
    print(f"{checkf2} is greatest number ");
else:
    print(f"{checkf3} is greatest number "); """


#*********** Loops (for, while) ***********

#Q1.Print numbers from 1 to 10 using a loop.
""" for i in range(1,11):
    print(i); """
""" a=int(5);
print((a&1)==0);
 """
""" i=5
print(f"{i} is even? {(i & 1)==0}") """
""" 
a=input()
b="25"
print(type(a)); """

""" # Q2. Print the multiplication table of a number.
a=5;
for i in range(1,11):
    print(f"{a}x{i+1}={a*i}");
 """
""" #Q3.Find the factorial of a number.
no=5;
fac=1;
for i in range(1,no+1):
    fac=fac*i
print(fac);
 """

""" #Q4.Print the Fibonacci series up to N terms.

val1=0;
val2=1;
print(val1)
print(val2)
for i in range(5):
    newfab=val1+val2;
    print(newfab)
    val2=newfab;
    val1=val2; """


""" # Q5.Reverse a number using a loop.

realNum=142
revNum=0
while realNum>0:
    rem=realNum%10
    revNum=revNum*10+rem
    realNum//=10

print(revNum)
 """

#Q6.Write a function to check if a number is even.

""" n=5
print(("num is even","num is odd")[n&1])
 """
""" checkNum=25
if(checkNum%2==0):
    print("even")
else:
    print("odd")
 """
""" 
def toggle_doors(num_doors):
    # Initialize all doors to closed (False means closed, True means open)
    doors = [False] * (num_doors + 1)  # index 0 is unused for simplicity

    # Each monkey toggles doors that are multiples of their number
    for monkey in range(1, num_doors + 1):
        for door in range(monkey, num_doors + 1, monkey):
            doors[door] = not doors[door]  # toggle door

    # Print the results
    for door in range(1, num_doors + 1):
        state = "Open" if doors[door] else "Closed"
        print(f"Door {door}: {state}")

# Run the simulation
toggle_doors(100)
 """
#Q7.Count the frequency of characters in a string.


# givenNames="Naman"
# givenNames=givenNames.lower()
# repeats={}

# for char in givenNames:
#     if char in repeats:
#         repeats[char]+=1
#     else:
#         repeats=1
# print(repeats)

# nameChar="Hello"
# repeat={}
# nameChar=nameChar.lower()
# for char in nameChar:
#     if char in repeat:
#         repeat[char]+=1
#     else:
#         repeat[char]=1
# print(repeat)

""" #Q8. Count number of digit in a number
nums=859
sums=0
for i in str(nums):
    sums+=int(i)
print(sums)
 """
#Q9.Check if two strings are anagrams.
""" s1="hello"
s2="helIo"
if s1==s2:
    print("yes")
else:  
    print("no") """
#************* Strings ****************
""" #Q1.Take a string and print its length.
nameString="Hello"
print(len(nameString)) """


""" #Q2.Count the number of vowels in a string.
nam="Aabhijeet"
count=0
vov="aeoiuAEIOU"
for char in nam:
    if char in vov:
        count+=1;
print(count)
 """
#Q3.Check if a string is a palindrome.
# poli="jahajh"
# print(poli==poli[::-1])
""" poliCheck=458
rev=0
while poliCheck>0:
        rem=poliCheck%10
        rev=rev*10+rem
        poliCheck//=10

# print("its polindrome " if poliCheck==rev else"not polindrome")
print(("its not pollindrome","its pollindrom")[poliCheck==rev]) """

""" #Q4.Convert a string to uppercase and lowercase.
nameCase="dhananjay"
print(nameCase.upper())
print(nameCase.lower())
 """
""" #Q5.Replace spaces with hyphens in a string.

spec="my name is Sahu"
print(spec.replace(" ","-")) """

#************** List **************
""" #Q1.Create a list of 5 elements and print it.
myList=[1,5,6,9,7,3]
print(myList)

 """
#Q2.Add, remove, update elements in a list.
# list1=[1,5,6,8]

# #add
# list1.append(9)
## insert at index
# list1.insert(0,9)
##update
# list1[0]=100
##delete
#list1.pop(1) # this will remove value from index 1
## delete
# del list1[3] # remove value at 1

# print(list1)
 
#Q2.Find the largest and smallest number in a list.

""" list2=[72,1,5,9,28,14,65,]
print(max(list2))
print(min(list2)) """

""" #Q3.Sort a list in ascending and descending order.
list3=[72,1,5,9,28,14,65,]
print(sorted(list3)) #for ascending order
print(sorted(list3,reverse=True)) #for descending order """
#Q4.Reverse a list.
# list4=[1,2,3,5,6,8,9,11]
# reveList=list4[::-1]
# print((reveList ))

#************* Tuples and Sets ****************
""" #Q1.Create a tuple and access its elements.
tup=(5,8,9,6,7)
print(tup[0]) """

""" #Q2.Convert a list to a tuple and vice versa.
tup1=(7,8,5,2,4,3,6)
print(type(tup1))
tup2List=list(tup1)
print(type(tup2List))
list2Tup=tuple(tup2List)
print(type(list2Tup))
 """
"""  #Q3.Create a set and perform add/remove operations.
set1={1,5,9,6,7,3}
# print(type(set1))
# set1.add(76)
set1.remove(5)
print(set1) """

""" #Q4.Find the union and intersection of two sets.
set2={1,5,9,7,6,1,6}
set3={1,8,10,65,48,6}
# print(set2.union(set3)) #all
print(set2.intersection(set3)) #commmon """


##*********************Dictionaries ************
""" #Q1.Create a dictionary with name and age.
dict1={'name':"Sohan",'age':18}
print(dict1) """

""" #Q2.Access and update dictionary values.
dict2={'name':"Sohan",'age':18,"class":"2"}
print(dict2['name']) #accessing element
dict2['class']=3 #update


print(dict2) """
""" #Q3.Delete a key from a dictionary.
dict3={'name':"Sohan",'age':18,"class":"2"}
del dict3['name'] #deleting key
print(dict3) """

#Q$.Loop through a dictionary.
#dict4={'name':"Sohan",'age':18,"class":"2"}
#for key in dict4:
 #   print(key)

#for key, value in dict4.items():
   # print(key, "→", value)



#************ Bonus Challenges ************
""" #Q1.FizzBuzz (print "Fizz", "Buzz", or number for 1–50).
for i in range(1,51):
    if(i%3==0 & i%5==0):
        print(f"the number {i} is fizz and buzz")
    elif(i%3==0):
        print(f"number {i} is fizz")
    elif(i%5==0):
        print(f"number {i} is buzz")
    else:
        print(i) """


#********** Advanced Loops and Comprehensions ****************
""" #Q1.Print all prime numbers between 1 and 100.
nums=5
isPrime=True
if nums<=1:
    isPrime=False
else:
    for i in range(2,nums):
        if nums%i==0:
            isPrime=False
            break
        else:
            isPrime=True
print(isPrime) """


# *********** Bonus Challenges ***************
""" #Q1.FizzBuzz (print "Fizz", "Buzz", or number for 1–50).

checkFizzBuzz=50
for i in range(1,checkFizzBuzz+1):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")    
    else:
        print(i)    
 """

""" # Count Frequency of a string
checkText="Jahaj"
freq={}
checkText=checkText.lower()
for char in checkText:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
print(freq) """

# Q3.Check if two strings are anagrams.

# def are_anagrams(s1, s2):
#     return sorted(s1.lower()) == sorted(s2.lower())

# # Example usage
# print(are_anagrams("Rescue", "Secure"))  # Output: True
# print(are_anagrams("Hello", "World"))  # Output: False

# String1 = "Listen"
# String2 = "Silent"

# String1 = sorted(String1.lower())
# String2 = sorted(String2.lower())

# print("String1 after sorting: ", String1)
# print("String2 after sorting: ", String2)

# # check if now strings matches
# if String1 == String2:
#     print('Strings are anagram')
# else:
#     print('Strings are not anagram')
# str1="Rescue"
# str2="Seccre"
# if sorted(str1.lower())== sorted(str2.lower()):
#     print("anagram")
# else:
#     print("not")

#************* Advanced Loops and Comprehensions *******************

#Q1.Print all prime numbers between 1 and 100.

# for i in range(2,70):
#     for j in range(2,70):
#         if(i%j==0):
#             break
#     if(i==j):
#         print(i)


# #Q2.Print odd numbers between 1 and 100
# for i in range(1,100):
#     if i%2 !=0:
#         print(i)


# #Q3.Print star patterns (pyramid)
# stars=5
# for i in range(stars):
#     for j in range(i+1):
#         print("*",end=" ")
#     print("")

# #Q4.Use list comprehension to create a list of squares of numbers from 1 to 20.


# #Q5.Filter out all even numbers from a list using list comprehension.
# allList=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# evenList=[i for i in allList if i%2==0]
# print(evenList)

# #Q6.Use list comprehension to create a list of squares of numbers from 1 to 20.
# listComp=[i for i in range(1,21)]
# print(listComp)

""" #Q7.Print squares of numbers 1 to 10 using list comprehension
sqList=[i**2 for i in range(1,21)]
print(sqList)
 """
    
# #Q8.Filter out all even numbers from a list using list comprehension.

# evenNums=[i  for i in range(1,21) if i%2==0]
# print(evenNums)



#************************File Handling**************

#w is for write in file
# r is for read the file
# a is for to append in file or add some data in pre exist file
# r+ is for add data in from 0 cursor position
# code filename.txt is for to open a file in next tab
# seek() is for to find cursor position


# file write
# with open("newFile.txt","w") as f:
#     f.write("This is new file.Thank you for your contribution")

# file read
# f=open("hellos.txt","r")
# print(f.read())
# f.close()

# with open("pract.txt","w") as file:
#     file.write("This is new file for again practice of opening and write data in file")
#     file.close()

# f=open("pract.txt","r")
# print(f.read())
# f.close()

# f=open("pract.txt")
# print(f"cursor position before read {f.tell()}")
# print(f.read())
# print(f"cursor position after read {f.tell()}")

# print("before seek method")
# print(f.seek(20))
# print(f"cursor position after seek method {f.tell()}")
# print("after seek method")
# print(f.readline())
# print(f.readline())
# print(f.readline())
# ******************

# with open("random1.txt","w") as file:
#     file.write("This is file for random data.\n There is lot of information available. \n Get more knowledge about this file you have to read")
#     file.close

# f=open("random1.txt","r")
# print(f.tell())
# print(f.read())
# print(f.tell())
# print(f.seek(20))
# print(f.tell())
# print(f.readline())
# for line in f.readline()[:-12]:
    # print(line,end="")
# f.close
# to open file in new tab 
# code random1.txt
#*********** append in file ***************

# with open("random1.txt","a") as f:
#     f.write("\n this line is genearted by append ")


#******* using command we can create a file..write below command in terminal
#echo "hello this file is generated by echo command" >> echofile.txt
# r+ mode write but as override ....so handle this use seek

#******
# with open("pract.txt","r+") as f:
#    f.seek(len(f.read()))
#    f.write("ok.hello, sir this is generated by r+")

#*********** copy from one file to another*************
# with open("originnalFile.txt","w") as wf:
#     wf.write("Maya, 500000  \n Zoya ,28000 \n Kiran, 48000")
#     wf.close
 
#  #now copy

# with open("originnalFile.txt",'r') as rf:
#     with open("copyFile.txt",'a') as wf:
#         for line in rf.readlines():
#             name,salary=line.split(",")
#             wf.write(f"{name}'s salary is {salary}")


# for practice purpose
# with open("orginal2.txt","w") as wf:
#     wf.write("Anand,28 \nMaya,48 \nDua,24")
#     wf.close
 
# with open("orginal2.txt","r") as rf:
#     with open("copy2.txt",'a') as wf:
#         for line in rf.readlines():
#             name,age=line.split(",")
#             wf.write(f"{name} is {age} years old")
#*****************************************************************************************

# with open("mainFile1.txt","w") as wf:
#     wf.write("This is first line\nThis is second line. \nThis is third line.")
#     wf.close()

# with open("mainFile1.txt","r") as rf:
#     with open("mainFile1Copy.txt","a") as wf:
#         for line in rf.readlines():
#             lin1=line.split(",")
#             wf.write("".join(lin1))
        
#************************ copy links from one file to other file ****************************
#
# with open("linksFile.txt","w") as wf:
#     wf.write("""<!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Social Links</title>
#     <style>
#         body {
#             font-family: Arial, sans-serif;
#             background-color: #f4f4f4;
#             text-align: center;
#             margin-top: 50px;
#         }
#         .social-link {
#             display: inline-block;
#             margin: 15px;
#             padding: 10px 20px;
#             background-color: #007bff;
#             color: white;
#             text-decoration: none;
#             border-radius: 10px;
#             transition: background-color 0.3s;
#         }
#         .social-link:hover {
#             background-color: #0056b3;
#         }
#     </style>
# </head>
# <body>
#     <h1>Follow Us</h1>
#     <a href="https://www.facebook.com" class="social-link" target="_blank">Facebook</a>
#     <a href="https://www.instagram.com" class="social-link" target="_blank">Instagram</a>
#     <a href="https://www.twitter.com" class="social-link" target="_blank">Twitter</a>
# </body>
# </html>
# """)

# import re

# with open("linksFile.txt", "r") as rf, open("linksCopyFile.txt", "w") as wf:
#     content = rf.read()
#     links = re.findall(r'href="([^"]+)"', content)
#     for link in links:
#         wf.write(link + "\n")

#************************************************************************************************************


# num1=int
# num2=int
# num1=5
# print(num1)

# here both will give same output
# # for i in range(5):
# #     print("hello")

# #or
# for _ in range(5):
#     print("hello")
#***********************************
# l=[1,2,3]
# x,_,y=l
# print(x)
# print(_)
# escape sequence
#expected output ---> Line A \n Line B
#print("Line A \\n Line B")
# expected output ---> \" \'
# print("\\\"  \\\' ")

#expected output ---> this is \\ double backslash
#print(" this is \\\\ double backslash")
#expected output ---> these are /\/\/\/\ mountains
# print("these are  /\\/\\/\\/\\ mountains")
#expected output ---> he is    awesome (use escape sequence instead of manual spaces)
# print(" he is \t awesome ")
#expected output --->\" \n \t \'
# print('\\"  \\n  \\t \' ')
# also we use r to do this...se below exaMPLE
# print(r"this is \n") // wecan print any escape sequence using r

#*****p
# print(2**2.05)
# print(round(2**2.05,2))
# name,age=input("enter your name and age").split()
# print(name)
# print(age)
#***********************************************************


# num1,num2,num3=map(int,input("enter three number in order to get average").split())
# num1,num2,num3=input("enter three number in order to get average").split()
# print(type(num1))
# avgr=int(num1+num2+ num3)/3
# print(f"the average of {num1},{num2} and {num3} is {avgr}")

#********************
#1string slicing
# #syntax [start argument:stop argument]
# lang="python"
# print(lang[0:3])

#2 string slicing

# #syntax [start argument:stop argument-1:step]
# lang="python"
# # print(lang[::-1])
# print(lang[2::2])
# **********************************replace**********************************
# st="He is nice guy"
# newst=st.replace("is","was")
# print(st)
# print(newst)

# st1="He is going to school and he is also listening song"
# newst1=st1.replace("is","was") # in this way both is replaced
# print(newst1)
# newst2=st1.replace("is","was",1)  #it will replace only one is
# newst2=st1.replace("is","was",2)  #it will replace only both is
# print(newst2)

#*************** find ******************
# strfind="Jacob is good guys and he is watching movie"
# # strshow=strfind.find("is") ## it will give first position of finding word
# # strshow=strfind.find("is",7) # it will find is after the first occurance or after the 7th position
# # print(strshow)
# # but we dont know the position of first is then how to do......................>
# strshow=strfind.find("is")
# strshownext=strfind.find("is",strshow+1)
# print(strshownext)

# #**************************center ********************************************
# nm="Raj"  #add * before and after name like *Raj* we use center
# print(nm.center(5,'*'))

#note------------: String is always immutable..let see example

# str="Hello"
# #str[1]='T'   # so we can no do this..... as strings are immutable but we do like
# ss=str.replace("l","L")  # we can do this but original string can't be change
# print(ss)

# print(str)
#*****************************Asignment Operators **********************************************************************
# name="Raj"
# name=name+"a"
# print(name) #but we can do this 
#********
# nam="kan"
# nam="du"+nam
# print(nam)

#***other example********
# age=31
# age+=1
# print(age)

# **************** if and if else ******************************

# aa=45
# if aa<20:
#     print("hello")
# elif aa==0:
#     print("this value is 0")
# else:
#     print("less than 45")

# # and and or operators
# nm="Raj"
# ag=23
# if nm=="Raj" and ag==23:
#     print("details are correct")
# else:
#     print("both condition are not true")
#or 
# nm="Maya"
# ag=45
# if nm=="Maya" or ag==46:
#     print("both of them one is true...output is true")
# else:
#     print("none of them is true")


#*************** in keyword ****************************
# chkIn="Hello"
# if "e" in chkIn:
#     print("yes e is exits")
# else:
#     print("not exist")

# check empty
# str=""
# if str:
#     print("its not empty")
# else:
#     print("its empty")

#******************** while ************************

# a=1
# while a<=10:
#     print(a)
#     a+=1


# ********************** sum of numbers ****************
# a=1 
# sums=0
# while a<=10:
#     sums=sums+a
#     a=a+1
# print(sums)

# *********** sum of digits of a number ***********************************

# a=input("enter a num")
# print(type(a))
# i=0
# total=0
# while i<len(a):
#     total=total+int(a[i])
#     i+=1
# print(total)

# num=12345
# total=0
# i=0
# str_num=str(num)
# while i<len(str_num):
#     total+=int(str_num[i])
#     i+=1
# print(total)

#********************
# name=input("Enter your name ")
# name=name.lower()
# rep={}
# for i in name:
#     if i in rep:
#         rep[i]+=1
#     else:
#         rep[i]=1
# print(rep)





# name=input("Enter your name ")
# i=0
# dict={}
# name=name.lower()

# while i<len(name):
#     char =name[i]
#     if char in dict:
#         dict[char]+=1
#     else:
#         dict[char]=1
#     i+=1
# print(dict)

#************* sum of digits of number***************


# nm="456"
# total=0
# for i in range(0,len(nm)):
#     total+=int(nm[i])
# print(total)

#********* reverse  number ***************
# for i in range(10,0,-1):
#     print(i)

#*********************** slicing string ***********************************

# mainString="Hello India"
# print(mainString[:5]) # give ====> Hello
# print(mainString[6:]) # give ====> India bcoz start from 5 and end in last
# print(mainString[3:8]) # give ====> lo In
# print(mainString[0::2]) # give ====> HloIda..bcoz print one character and skip other
# print(mainString[::-1]) # give ====> it reverse string  aidnI olleH
# print(mainString[2:8].upper()) # give ====> LLO IN




# ************ append method in list ***********************
# myList=[1,2,3,"four","five",6]

# print(myList)
# print(myList[0:3]) # same as string slicing

# myList.append("seven") ## add item in last index of list
# print(myList)
 ##**************************************
# fruits1=["Mango","Guava"]
# fruits2=["Plum","Papaya"]

# print(fruits1+fruits2) #gives ['Mango', 'Guava', 'Plum', 'Papaya']
# # but
# fruits1.append(fruits2) # gives ['Mango', 'Guava', ['Plum', 'Papaya']] add list2 inside list 1
# print(fruits1)
# but if
# fruits1.extend(fruits2) # ['Mango', 'Guava', 'Plum', 'Papaya']
# print(fruits1)
# print(fruits1[2]) # gives Plum

#******************************* pop method *****************************
myFruitsList=['mango','plum','orange','papaya']
# myFruitsList.pop(0) # it will remove mango
# print(myFruitsList)
# # 
# myFruitsList.pop() # it will remove last index by default papaya will remove
# print(myFruitsList)

### ************************* remove method ***********************

# myFruitsList.remove("mango") # it will remove mango and also if there if two mango then it remove first mango
# print(myFruitsList)

#***************************************** delete method ***********************************
#del myFruitsList[1]  # it will delete plum as i gave index but if
#print(myFruitsList)

# del myFruitsList[-1] # it will delete papaya...as same as list works
# print(myFruitsList)

#************ use of in Keyword in list
# cityList=["Lucknow","Dlehi","Bhopal","Chennai","Mumbai","Jaipur"]
# if "Lucknow" in cityList:
#     print("Lucknow is in list")
# else:
#     print("this city is not found")

# some other method in list
# #*********************** count method ********************
# myNumList=[10,20,7,21,6,12,30,6,20,15,54]  
# print(myNumList.count(20))# it will count repeated numbers

#*********************** sort method ********************
# myNumList=[10,20,7,21,6,12,30,6,20,15,54]  
# myNumList.sort()# it will sort list inascending order
# print(myNumList)


#*********************** sorted method ********************
# myNumList=[10,20,7,21,6,12,30,6,20,15,54]  
# print(sorted(myNumList)) # it will sort list but dont change in original list
# print(myNumList)

#*********************** clear  method ********************
# myNumList=[10,20,7,21,6,12,30,6,20,15,54]  
# myNumList.clear() #it will clear list
# print(myNumList)

#*********************** reverse method ********************
# myNumList=[10,20,7,21,6,12,30,6,20,15,54]  
# myNumList.reverse() # it will reverse list 
# print(myNumList)


# ***************************** copy a  list *******************************
# nameList=["Raju",'Mayank','Sonu','Jitendra','Pawan']  
# newNameList=nameList.copy() # it will copy all element in new list
# print(newNameList)
#******************
#******************************** is vs equal *************************************************
# list1=['pant','rahul','msd','gayle']
# list2=['pant','rahul','msd','gayle']
# list3=['pant','Kohli','rohit', 'rahul','msd','gayle']
# print(list1==list2)  # it will gives true as it check values are same or not but if
# print(list1 is list2) # it gives false it check all values location is same or not

# ***************************************join method************************************************
# userList=["Raj",'45']
# print(','.join(userList))
# userList1=["maya",'45','Teacher']  # gives output like maya:45:Teacher
# print(':'.join(userList1))


#**************************************** List inside list *********************************
# matrix=[[1,2,3],[4,5,6],[7,8,9]] # its 2d list

# # print(matrix[1][1]) # it gives 5

# # print all element of matrix list
# # for sublist in matrix:
# #     for i in sublist:
# #         print(i)
 

# ******************** create list using for loop ****************
# newList= list(range(1,11)) # this gives [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(newList)



# #  pop and append
# list1=list(range(1,11))
# print(list1.pop(2)) # it gives 3 as output at 3 is on 2nd index lof list1
# print(list1.append(5))

# ******** practice ************
# originalList=[1,2,3,4,5]
# def negListFunc(l):
#      negList=[]
#      for i in l:
#         negList.append(-i)
#      return negList
# print(negListFunc(originalList))




# #negative List practice
# list2=[1,2,3,4,5,6]
# def negList(l):
#     neg=[]
#     for i in l:
#         neg.append(-i)
#     return neg
# print(negList(list2))
#*************************************************************
# print square of element of a list in other list
# list4=[1,2,3,4,5,6,7,8,9,10]
# def squareFunc(l):
#     squareList=[]
#     for i in l:
#         squareList.append(i*i)
#     return squareList
# print(squareFunc(list4))


#****************************************** reverse a list using function******************************

# list5=[1,2,3,4]
# def reverseListFunc(l):
#     revList=[]
#     for i in l[::-1]:
#         revList.append(i)
#     return revList
# print(reverseListFunc(list5))

# ****************** other method to do same

# list6=[1,2,3,4]
# def revL(l):
#     return l[::-1]

# print(revL(list6))

# *********** practice exercise ********************
# question ['abc','ghi','xyz']=======>['cba','ihg','zyx']


# myList=['abc','ghi','xyz']
# def revAllList(l):
#     revList=[]
#     for i in l:
#         revList.append(i[::-1])
#     return revList
# print(revAllList(myList))

# ls1=[1,2,3,4,5,6]
# ls2=[5,6,7,8,9]
# res=[]
# def checkFunc(l1,l2):
#     for i in l1:
#         if i in l2:
#             res.append(i)
#     return res

# print(checkFunc(ls1,ls2))
# copy and update...........
# lst1=[1,2,3,5,6]
# lst2=lst1.copy()
# print(lst2)
# # lst1[1]=5
# # print(lst1)
# # print(lst2)
# #//***********
# lst3=lst1
# lst3[2]=20
# print(lst3)
# sets...............union and intersection
#union -------------- only unique
# s1={1,2,3,4,5,6}
# s2={3,4,5,7}
# union_sets=s1|s2
# print(union_sets)

# #intersection --- common
# print(s1 & s2)
#**************************************

#List comprehension
# lst_comprehension=[ i**2 for i in range(1,11)]
# print(lst_comprehension)

# lst_comprehension2=[i**3 for i in range(1,11)]
# print(lst_comprehension2)

#******************negative using list comprehension
# negative_number=[ -i for i in range(1,11)]
# print(negative_number)

#***************** show first letter **************************
# list_names=["Naman","Radhey","Mohan"]
# list_names2=[]
# show_names=[ list_names2.append(name[0])  for name in list_names]
# show_names2=[ name[0]  for name in list_names]
# print(list_names2)
# print(show_names2)

#*******************
# string_list=['abc','tuv','xyz'] #********** ['cba','vut','zyx']

# def reveList(l):
#     return [ i[::-1] for i in l]

# dd=reveList(string_list)
# print(dd)

#***********************************************

# generate list without for loop 
# myList=list(range(1,11))
#print(myList)

# ******** if in list comprehnsion ****************

#type 1 list

# newList= [i for i in range(1,11) if i%2==0] # it gives only even numbers
# print(newList)


#********
# oddList=[i for i in range(1,11) if i%2!=0 ]
# print(oddList)
# ****************************************************************************************
# normal method
# numList=[]
# myLis=['True','False','Monday',1,2,3,'Sunday','yes',4,5,6,]
# def funcs(l):
#     for i in l:
#         if type(i)==int:
#             numList.append(str(i))
#     return i

# funcs(myLis)
# print(numList)

# list comprehension method

# myLis2=['True','False','Monday',1,2,3,'Sunday','yes',4,5,6,7]
# numLis=[]
# def myfuncc(l):
#     return [numLis.append(str(i)) for i in myLis2 if type(i)==int]

# myfuncc(myLis2)
# print(numLis)


# ******** **********if and else in list comprehnsion ****************
# nuList=[1,2,3,4,5,6,7,8,9,10]

# newLis3=[ i**2 if i%2==0 else -i for i in nuList]
# print(newLis3)



#**********
# a="Hi"
# print(a*3)

# def shows(list):
#     return list[0]

# z=shows([1,2,3,4,5,6])
# print(z)


# def greet(name="Guest"):
#     return f"Hello, {name}"

# print(greet("sahu"))

#//*****************************function
# def myFunc(o):  #with argument
#     print(o)
# myFunc(5)


# def myFuncs(f_name,l_name):  # function with multiple arguments
#     print(f"my name is {f_name} {l_name}")

# myFuncs("Maya",'Agarwal')

#args
# def myArgs(*args):
#     print(max(args))
# myArgs(5,4,8,6)

# *kwargs example

# def myKwargsFunc(**kwargs):
#     print(kwargs["a"])
#     print(kwargs["b"])
#     print(kwargs['a']+kwargs['b'])

# myKwargsFunc(a=5,b=6)

#
# def myKwargFunc(**kwargs):
#     print(kwargs['name'])
#     print(kwargs['last_name'])


# myKwargFunc(name='Maya',last_name="Agrawal")


#default parameter
# def myDefault(a=5):
#     print(a)

# myDefault()
# myDefault(6)
# myDefault(7)
# myDefault(8)

#Passing a List as an Argument
# def passList(myList):
#     print(myList[2])
# passList(['Mnago','Guava','Plum','Papaya','Melon'])

def hh(p,o):
    print(p,o)
hh(5,25)
