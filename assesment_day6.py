list1=["2020-10-12","2023-10-13","2023-10-08"]

for i in list1:
    print(i[-2:])

for i in list1:
    print(i.split("-")[-1])

b=[]
for i in list1:
    b.append(i.split("-")[-1])
b

l1=[1,2,3]
l2=["a","b","c"]
list(zip(l1,l2))

dict(list(zip(l1,l2)))

a=int(input("enter the number:"))
b=100
c=b/a
print(c)

"""#exceptional handling
1. try block :- The try block lets you test a block of code for errors.
2. except    :- The except block lets you handle the error.
3. else      :- The else is nothing but lets you execute code when there is no error.
4.finally block :- The finally block lets you excute code,regardless of the result of the try and except block (or) which will create a block and it is execute by defaultly after execution of try and except.
"""

try:
    a=int(input("enter the number:"))
    b=100
    c=b/a
    print(c)
except:
    print("enter proper value greater zero")

try:
    a=int(input("enter the number:"))
    b=100
    c=b/a
    print(c)
except ValueError:
    print("pls give int value")
except ZeroDivisionError:
    print("enter proper value greater zero")
print("done")

try:
    a=int(input("enter the number:"))
    b=100
    c=b/a
    print(c)
except Exception as e:
    print(e)
print("done")

try:
    a=int(input("enter the number: "))
    b=100
    c=b/a
    print(c)
except Exception as e:
    print(e)
else:
    print("no error")
print("done")

try:
    a=int(input("enter the number: "))
    b=100
    c=b/a
    print(c)
except Exception as e:
    print(e)
else:
    print("no error")
finally:
    print("successfully finished")#--------------the boss

try:
    a=int(input("enter the number: "))
    b=100
    c=b/a
    print(c)
except Exception as e:
    print(e)
finally:
    print("successfully finished")

"""1.**Int**:- Integer are whol number or natural number with out decial point.(default value is "0")

2.**boo**l:- A boolean data type represents truth values,either True or False.

3.**float**:-It is a single value data type real value with decimal point.

4.**String**:-String is a predefined data type and data structure and string is a collection of characters enclosed in single or double quotes.

5**.list**:-A list is ordered collection of items that can be of any data type.List are mutable,meaning you can change their contents.

6.**tuple**:-similar to list, a tuple is an orderd collection of items,but it is immutable,it means you can't change its contents once defined.

7.**range**:-The range data type is used to generate a sequence of numbers,often used in loops.It's effcient for iterating over a range of values.

8.**dict**:-A dictionary is an unorderd collection of Key-value pairs.Each key must be unique,and you can use it to look up the associated value.

9.**complex**:-his data type represents complex numbers with a real and imaginary part, written as a + bj, where a and b are real numbers and j represents the square root of -1.

10.**set**:- A set is an unordered collection of unique elements. It's useful for performing operations like union, intersection, and difference on sets.


11.**frozenset**:-imilar to a set, a frozenset is an immutable version of a set. Once you create a frozenset, you cannot modify its elements.


"""

a=20

mutable and immutable
list        tuple, int, str, bool, float, complex, frozenset
set
dict

#set unordered, unchangeable, unindex, dot not allow duplicates values
#set items or elements are any data types

1.add
2.clear
3. copy
4. difference

#creating empty use below step
set1={()}

type(set1)

set2={1,2,3,4,5,6,6,6}

set2

set3={1,2,3,4,5,6,6,7,True}

set3

set4={1,2,3,4,5,"t",1.0,6,True,1+2j}

set4.add("h")

set4

set4.clear()

set5=set4.copy()

set5

id(set4)

id(set5)

set3

set4

z=set3.difference(set4)

z

y=set4.difference(set3)

set3

set4

set3.difference_update(set4)

set3

?set4.discard

set4.discard(1) #it must be element otherwise no error

set4

set3

set6= set3.intersection(set4)#it creates new set fetching matching items

set4.update

set4.intersection_update(set3)#it remove the itmes is not present in both sets it is updated original set

set7={"1","5"}

?set4.isdisjoint

#isdisjoint
set3.isdisjoint(set7)

set3

z=set4.issubset(set3)#bollean output true or false

z

set3.issuperset(set4)#bollean output true or false

set3.remove(7) #remove specific element must be elemnt otherwise error

set3

#union

set3

set4

t=set3.union(set4)

t

?t.symmetric_difference

u=set3.symmetric_difference(set4)#here it will create new set which remove both set common item

u

set3.symmetric_difference_update(set4)#here it will update original set which remove both set common item

set3

#updation
set3.update(set4)

set3={1,2,3,5,8,9}

set3

#index
set3

set3[1]

set3[3]="7" # Set object does not support item assigment

#frozenset ----------->immuatable
#Syntax: frozenset([Iterable])

set3

q=frozenset(set3)

type(q)

q.add["v"] # 'frozenset' object has no attribute 'add'

dict1={"1":1,"2":2}

dict.copy

dict1.copy()

dict2={"2":2,"3":3}

y=dict1.difference(dict2) # Difference: Returns keys that are in dict1 but not in dict2.But dict object has no attribute 'difference'

u=dict1.intersection(dict2) # Intersection: Returns keys that are common between dict1 and dict2.But dict object has no attribute "intresection"

dict3=dict1.symmetric_difference(dict2) #Symmetric Difference: Returns keys that are in either dict1 or dict2 but not both. dict oject has no attribute 'symmetric_difference.

c=dict1.union(dict2) # Union: Merges both dictionaries, keeping values from dict2 for overlapping keys.

v=dict1.issuperset(dict2) # dict we can't possible to use issuperset().Is Superset: Checks if dict1 is a superset of dict2 (based on keys).

v=dict1.issubset(dict2) #Is Superset: Checks if dict1 is a superset of dict2 (based on keys).but dict object has no attribute 'issubset'.

v=dict1.isdisjoint(dict2) #Is Disjoint: Checks if dict1 and dict2 have no common keys.But here dict object has no attribute 'isdijoint'

#copy, difference, intersection, symetric_difference, union, issuperset, issubset, isdisjoint
# this above methods are typically used sets not dictionaries in python.They are not the same ,and these methods are not directly applicable to dictionaries.

frozenset(dict1)

t1=(1,3,2,1,4,5)

sorted(t1, reverse=True)

#sort is a method (list, string) it will chnage origial datatype
#sorted is function() it is cerated new data type

#built in function
#1. all

?all #Return True if bool(x) is True for all values x in the iterable.If the iterable is empty, return True

all(t1)

all([ ])

all([True,False])

divmod(4,2)#otput is (floor division, quetint)

any([True,False])

any([False,False])

all([1,0])

?round #Round a number to a given precision in decimal digits.The return value is an integer if ndigits is omitted or None.
#Otherwisethe return value has the same type as the number.  ndigits may be negative.

round(1.6)

#operators
1. arithemetic
+,-,*,/,%,//,**

1+2

"q"+"2"

"w"+1 # can only concatinate 'str' to 'str' not 'int'

int+float=float
complex+complex=complex
comple+float=complex
int+complex=complex
int+boolean=int
boolean+boolean=int
str+str=str
int+int=int
list+list=list
tple+tple=tuple
set+set (we cant add)

{1,2}+{1,2} # set to set can't add

True+False

2+True

["s"]+["e"]

["s"]+("e") # can only concatinate 'list' to 'list' not string'

(1,)+(2,)

{1:1}+{2:2} # dict to dict can't add

2+2j+1+1j

1+1j+"w" # 'complex' and 'string' also can't add

a=30
b=20

a-b

list-list # list to list we can't supract

[1,2]-[1,2] # list to list also we can't supract.

True-False

#* multiplication

a*b

int*int
str*str(not)
float*float
boolean*boolean
str*int
str*float

(2+2j)*(2+2j)# j^2=-1 # it is (a+b)^2 formula  4+4j^2+8j :-j^2 is nothing but (-1) =4+4(-1)+8j=4-4+8j=8j

"ganesh"*6

True*True

"ganesh"*6.2 # can't multiply sequence by non-int of type float

list*list # list and list also we can't multiply

[1,2,3]*[1,2,3] # list and list also we can't multiply

list*int # list and int also we can't multiply

list*complex #list and complex also we can't multiply

[1,2,3]*(2+2j) #list and complex also we can't multiply

/,%,//

int**int #unsupported operand type(s) for ** or pow(): 'type' and 'typ

complex**complex # complex and complex we can but here type(complex)we will take thats why we con't possible to pow()

(2+2j)**(2+2j)

(2+2j)/(2+2j)

(2+2j)%(2+2j) # complex and complex we can't

#relational conditional
==,>,<,!=,>=,<=

a

b

a==b

a>b

a<b

a!=b

a<=b

a>=b

a,b=30,30

a!=b

#Assignment operotor

a

c=a

c

a=a+1#a+=1

a

a+=1

a

a=a-1#a-=1

a*=2

a/=30

a

a//=1

a

a%=1

a

a**=2

"""# Logicla opearotes are and, or, not"""

a=12
b=2
if a==12 and b==3:
    print("hi")
else:
    print("not matching with seven")

a=12
b=2
if a != b:
    print("hi")
else:
    print("not matching with seven")

a = 10

if not a:
	print("Boolean value of a is True")
else:
	print("10 is divisible by either 3 or 5")

