'''student="sam"
a=10
b=3+4j
print (b, type(b))
print("Hello world", student,a, type(a))
# Operatior in python
#arithmetic operator
x=10
y=20
z=x+y
z1=x-y
z2=x*y
z3=x/y
print(z)
print(z1)
print(z2)
print(z3)

#relational operator >, >=, <, <=, ==
print(x>y)
print(x>=y)
print(x<y)
print(x<=y)
print(x==y)

#Logical operator &&, ||
r=True
r1=False
print(r & r1)

#string
s = "hello my name is POOJA.."
print(s)
print("length of string: ", len(s))
print("lower case:", s.lower())
print("upper case:", s.upper())
print("replace method:", s.replace('a', 'u'))
print("no of occurence of is:", s.count("is"))
print("find method:", s.find('a'))
print("split method:", s.split('O'))

# Decision making statement
#if else stmt:
t=(1, 'tuple', 3.65, True, 'a', 'z')
t1=('b', 85, False)
list = ['hello', 'c', 56, 89.15, 3+9j]
dict={1:'apple', 2:'banana', 3:'grapes', 4:'mango', 5:'papaya'}
#m = int(input("enter your marks:"))
if 1 in dict:
    print(dict)
    print("keys:", dict.keys())
    print("values : ", dict.values())
    print('pop: ', dict.pop(5))
    print(dict)
    /*print(list)
    print("adding ele:", list.append('hi'))
    list[1] = 'p'
    print("modify the list:", list)
    print(list)
    print("length of list: ", len(list))
else:
    print("it is not present")

#printing 0 to 10 no. and print 101,201,301,401,501 and printing table of 2
i=1
n=2
list=[100,200,300,400,500]
while(i<=10):
    #list[i]=list[i]+i                             # for printing 101,201,301,401,501
    print(list[i])
    print('2 * ', i, ' = ', n*i)
    i=i+1


#for loop
list = ['apple', 'banana', 'mango', 'grapes']
list1=['juice', 'milk shake','fruit']
for i in list:
    for j in list1:
        print(i, j)
a=1 
for i in range(0,5):
    for j in range(0,i+1):
        print(a, end=" ")
        a=a+1
    print('\n')
'''
#def function in python
from numpy import ndarray

'''def hi():
    print('hi world')
hi()

def add(x):
    print(x+5)
add(5)
add(4)
add(6)
def odev(n):
    if(n%2==0):
        print(n, ' is even')
    else:
        print(n, ' is odd')
n=int(input('enter any number: '))
odev(n)

# use of  lambda keyword
g=lambda x:x*x*x
print(g(5))

# lambda keyword with filter
list1=[1,2,3,4,5]
fil_met=list(filter(lambda x: (x%2!=0), list1))
print(fil_met)       # it filter the odd no and then print it.

# lambda method with map()
list1= [4,6,8,2,9,7,1,3,5,0]
map_met=list(map(lambda x: (x*2), list1))
print(map_met)

# use of reduce methode it provide the final result of pgm, it is imported from functools package
from functools import reduce
list1=[5,1,6,8,4,2]
sum=reduce(lambda x,y:(x+y), list1)
print(sum)            #it produce the o/p as 26 i.e. the sum of all ele in the list, and it gives final result 

# oop concepts in python
# class is a blueprint of real world entity
# simple python pgm that demonstrate the class
class phone:
    def makecall(self):
        print("making a call")
    def playgame(self):
        print("playing a game")
p=phone()
p.makecall()
p.playgame()

# another ex of class, function with parameter
class fun_pm:
    def prize(self, p):
        self.x=p
        print('prize of phone is: ', self.x)
    def color(self, c):
        self.c=c
        print('color of phone is: ', self.c)
obj=fun_pm()
obj.prize(40000)
obj.color('black-n-white')

# use of constructor we write pgm that display the info of employee
class Emp:
    def __init__(self, name, age, sal, gen):
        self.n=name
        self.a=age
        self.s=sal
        self.g=gen
    def show(self):
        print('Name is:', self.n, '\n' 'Age is: ', self.a, '\n' 'Salary is:',self.s, '\n' 'Gender is: ', self.g)
i=1
for i in range(1,3):
    n = input('enter name: ')
    a = int(input('enter age: '))
    s = int(input('enter salary: '))
    g = input('enter gender: ')
    e=Emp(n, a, s, g)
    e.show()

# use of inheritance
class Emp:
    def __init__(self, name, age, sal, gen):
        self.n=name
        self.a=age
        self.s=sal
        self.g=gen
    def show(self):
        print('Name is:', self.n, '\n' 'Age is: ', self.a, '\n' 'Salary is:',self.s, '\n' 'Gender is: ', self.g)

class student(Emp):
    def display(self):
        print("I am Student.")

for i in range(1,3):
    n = input('enter name: ')
    a = int(input('enter age: '))
    s = int(input('enter salary: '))
    g = input('enter gender: ')
    s=student(n, a, s, g)
    s.show()
    s.display()

# use of method overriding, in this it overrides the init method of parent class using super().
#super() is used to invoke the method from super class.
class Emp:
    def __init__(self, name, age, sal, gen):
        self.n=name
        self.a=age
        self.s=sal
        self.g=gen
    def show(self):
        print('Name is:', self.n, '\n' 'Age is: ', self.a, '\n' 'Salary is:',self.s, '\n' 'Gender is: ', self.g)

class student(Emp):
    def __init__(self, name, age, sal, gen, rollno):
        super().__init__(name, age, sal, gen)
        self.r=rollno
    def display(self):
        print("I am Student.")
        #print("Name is :", self.n)
        print("roll no is :", self.r)

n = input('enter name: ')
a = int(input('enter age: '))
s = int(input('enter salary: '))
g = input('enter gender: ')
#n1=input("enter stud name :")
r=input("enter rollno :")

s=student(n, a, s, g, r)
s.show()
s.display()


# implementation of multiple inheritance
class A():
    def A_meth(self, name):
        self.n=name
        print("name of class A is :", self.n)
class B():
    def B_meth(self, name):
        self.n=name
        print("name of class B is :", self.n)
class C(A, B):
    def C_meth(self, name):
        self.n = name
        print("name of class C is :", self.n)
c=C()
c.A_meth("A. pooja")
c.B_meth("B. pritee")
c.C_meth("C. Vinayak")


# multilevel inheritance
class parent():
    def getname1(self, name):
        self.n=name
        print("name of parent :", self.n)
class child(parent):
    def getname2(self, name):
        self.n=name
        print("name of child :", self.n)
class grandchild(child):
    def getname3(self, name):
        self.n=name
        print("name of grandchild :", self.n)
gc=grandchild()
gc.getname1("pooja")
gc.getname2("pritee")
gc.getname3("vinayak")


# python library
# Numpy
import numpy as np
n=np.array([[10, 20, 30, 40, 50], [1, 2, 3, 4, 5]])
print(n, type(n))

import numpy as np
n=np.zeros((4, 8))   # this method help to print defined no.of row and column as zeros
print(n)

import numpy as np
n=np.full((2, 3), 5)
print(n, type(n))     # it print the same no as mentioned

import numpy as np
n=np.arange(1, 10, 2)       # it help to print range of no in array after specific interval of number. by default interval no. is 1
print(n, type(n))

import numpy as np
n=np.random.randint(1, 50, 10)      #it generate mentioned random no with specified no of random no e.g it will give 10 random no. between 1 to 50
print (n)

import numpy as np
l1=[2, 4, 6, 8, 10]
l2=[5, 10, 15, 20, 25]
n=np.array((l1, l2))
print (n)
n.shape = (5, 2)      # it help to build array as specified no.of rows and column
print(n)

import numpy as np
l1=[2, 4, 6, 8, 10]
l2=[5, 10, 15, 20, 25]
n=np.array((l1, l2))
print (n)
print(np.vstack((l1, l2)))           # it represents the array in verticle stack
print(np.hstack((l1, l2)))           # it represents the array in horizontal stack
print(np.column_stack((l1, l2)))     # it represents the array in column wise stack

import numpy as np
l1=[2, 4, 6, 10, 25]
l2=[5, 10, 15, 20, 25]
n=np.array((l1, l2))
print(n)
i=np.intersect1d(l1, l2)              # this method gives us same ele from the l1, l2
setdiff=np.setdiff1d(l1, l2)          # this gives different ele from l1 and subtract same ele from l1 and l2
setdiff1=np.setdiff1d(l2, l1)         # this gives different ele from l2 and subtract same ele from l1 and l2
print(setdiff)
print(setdiff1)

import numpy as np
l1=[2, 4, 6, 10, 25]
l2=[5, 10, 15, 20, 25]
sum = np.sum([l1, l2])       # it gives the addition of array
print (sum)
sum1 = np.sum([l1, l2], axis=0)  # it gives the sum of ele row wise
print(sum1)
sum2 = np.sum([l1, l2], axis=1)   # it gives the sum of ele column wise
print(sum2)

# Basic addition
a=np.array(l1)
b=np.array(l2)
print(a)
add=a+2
print (add)
sub= a-2
print(sub)
mul=a*2
print(mul)
div=b/5
print(div)

# mean, median and standard deviation
import numpy as np
l1=[2, 4, 6, 10, 25]
l2=[5, 10, 15, 20, 25]
a=np.array(l1)
b=np.array(l2)
mean=np.mean(l1)                    # calculating mean
print ('mean is :', mean)
median=np.median(l2)                # calculating median
print('median is :', median)
std=np.std(l1)                      # calculating standard deviation
print('standard deviation is :', std)

# how to save an array  using np.save("file name", arrayname)
import numpy as np
l1=[2, 4, 6, 10, 25]
l2=[5, 10, 15, 20, 25]
save=np.save("Array1", l1)
print (save)                    # it gives output as none
save1=np.save("Array2", l2)
print(save1)                    # it gives output as none

# now we have to load the array file
load=np.load('Array1.npy')
load1=np.load('Array2.npy')
print(load)
print(load1)
'''
# now let's see pandas library
# pandas library is used to data analsis and manipulation.
# it consist two data structure i.e. single and multi diamensional
# single diamensional - Series
# multi diamensional - dataframe

import pandas as pd
s=pd.Series([10, 20,30,40,50])             # we can change the index no. also or even we can use alphabet instead of no.
s2=pd.Series([5,10,15,20,25])
s1=pd.Series({'a':100, 'b':200, 'c':300, 'd':400}, index=['c', 'a', 'd', 'b'])
print(s[-4:], type(s))
print(s1)
sum=s-2
print(sum)
sum1=s+s2
print(sum1)