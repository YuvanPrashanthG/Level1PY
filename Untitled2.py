#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1 Hello world
print("Hello World")


# In[2]:


#2 Addition
a=int(input("Enter the first num:"))
b=int(input("Enter the second num:"))

print(a+b)


# In[3]:


#3 swap without tmp

a = int(input("enter the value of a:"))
b = int(input("enter the value of b:"))
a=a+b
b=a-b
a=a-b

print("Value of a is",a)
print("Value of b is",b)


# In[4]:


#4 kilometers
a= int(input("Enter the kilometer: "))


b=a*0.621371

print("Value in Miles is",b)


# In[5]:


#5 num is pos or neg

#positive 
a=int(input("Enter a number:"))
if a>0:
    print("Positive")
elif a<0:
    print("Negative")
else:
    print("Zero")


# In[6]:


#6 leap
a=int(input("Enter a year:"))
if((a%4==0) and (a%100==0)) or (a%400):
    print("Leap Year")
else: 
    print("Not a leap year")


# In[7]:


#7 prime
m=int(input("Enter the start:"))
n=int(input("Enter the end:"))

for i in range(m,n):
    c=0
    for j in range(1,i):
        if i%j==0:
            c=c+1
    if(c==1):
        print(i)


# In[8]:


#8 Fibonacci
n=int(input("Enter the n:"))
a=0
b=1
print(a)
print(b)
for i in range(1,n-1):
    c=a+b
    print(c)
    a=b
    b=c


# In[10]:


#9 Armstrong
y=int(input("enter the number"))
sum=0
temp=y
d=temp%10
e=(temp//10)%10
f=int(temp/100)
sum=(d**3)+(e**3)+(f**3)
if sum==y:
    print("armstrong")
else:
    print("not armstrong")


# In[12]:


#10 sum of n
a=int(input("enter the sum for n th term"))
sum=0
for b in range(1,a+1,1):
    sum+=b
print("sum of n is",sum)


# In[13]:


#11 star pattern fn.

def show_stars(n):
    for i in range(1, n + 1):
        print('*' * i)
n=int(input("Enter how many rows:"))

show_stars(n)


# In[16]:


#12 Remove charc from string
s=input("Enter the string: ")
n=int(input("Enter how much to remove:"))
print(s[n:])


# In[17]:


#13 list-print div by 5
n=int(input("Enter the size of list:"))
print("Enter the values:") 
list = []

for i in range(0,n):
    element = int(input("Enter an element: "))
    list.append(element)
    
print("The entered list is:")
print(list)
for i in list:
    if i%5==0:
        print(i)


# In[ ]:


#14 count of hi in string
s=input("Enter a string:")

print("The number of times hi is",s.count("hi"))


# In[ ]:


#15  number pattern
for i in range(1, 6):
    for j in range(i):
        print(i, end=' ')
    print()


# In[ ]:


#16 palindrome num or not
num=input("Enter a number:")

rev = num[::-1]

if num == rev:
    print("Palindrome")
else:
    print("Not a palindrome")


# In[ ]:


# 17 swap first and last in list 
n=int(input("Enter the size of list:"))
print("Enter the values:") 
list = []

for i in range(0,n):
    element = int(input("Enter an element: "))
    list.append(element)
    
print("The entered list is:")    
print(list)

list[0], list[-1] = list[-1], list[0]
print("List after swapping last and first:")
print(list)


# In[ ]:


#18swap two in list 
n=int(input("Enter the size of list:"))
print("Enter the values:") 
list = []

for i in range(0,n):
    element = int(input("Enter an element: "))
    list.append(element)
    
print("The entered list is:")    
print(list)

a = int(input("Enter the first index to swap:"))
b = int(input("Enter the secnod index to swap:"))

list[a], list[b] = list[b], list[a]
print("List after swapping last and first:")
print(list)


# In[ ]:


#19  ways-find len of list
n=int(input("Enter the size of list:"))
print("Enter the values:") 
list = []

for i in range(0,n):
    element = int(input("Enter an element: "))
    list.append(element)
    
#using built-in function
print("Length of list: ",len(list))

#using for loop
c=0
for i in list:
    c+=1
print("Length of list: ",c)


# In[ ]:


#20 Max of 2 num
a=int(input("enter value 1: "))
b=int(input("enter value 2: "))
if a>b:
    print("Maximum value:",a)
else:
    print("Maximum value:",b)


# In[ ]:


#21 Min of 2 num
a=int(input("enter value 1: "))
b=int(input("enter value 2: "))
if a<b:
    print("Minimum value:",a)
else:
    print("Minimum value:",b)


# In[ ]:


#22 string is pal. or not
s=input("Enter sting value: ")
print("\npallindrome checking:")
if s==s[::-1]:
    print("It is a pallindrome")
else:
    print("It is not a pallindrome")
print("\nsymmentrical checking:")
half=len(s)//2
if s[half:]==s[:half]:
    print("It is symmentrical")
else:
    print("It is not symmentrical")


# In[ ]:


#23 rev words in string
s=input("Enter sting value: ")
print(s[::-1])


# In[ ]:


#24 ways-remove i char in stirng

s=input("Enter the string :")
i=int(input("Enter index to remove:"))
r=s[:i]+s[i+1:]
print(r)


# In[ ]:


#25 len of string

s=input("Enter the string :")

#using built-in function
print("Length of string: ",len(s))

#using for loop
c=0
for i in s:
    c+=1
print("Length of string: ",c)


# In[ ]:


#26 print even len words in string

s=input("Enter the string :")
r=s.split(" ")
for i in r:
    if len(i)%2==0:
        print(i)


# In[ ]:


#27 size of tuple

tuple=(1,2,3,4,5)

print(len(tuple))


# In[ ]:


#28 max and min in tuple

t=(1,2,3,4,5)
print("Maximum value= ",max(t))
print("Minimum value= ",min(t))


# In[ ]:


#29 sum in tuple

t=(1,2,3,4,5)
print("Sum of elements in the tuple:",sum(t))


# In[ ]:


#30 row add. in tuple matrix

tup_mat = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
for row in tup_mat:
    s=sum(row)
    print("Row sum:",s)

