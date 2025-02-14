from array import array

class Represent(object):
    """class showing how work repr in python, and how it redifine __repr__ method in class. """
    def __init__(self,x,y):
        self.x , self.y = x,y
    def __str__(self):
        return "Represent x as {} and y as {}.".format(self.x,self.y)
    def __repr__(self):
        return "Represent(x={},y=\"{}\")".format(self.x,self.y)

r1 = Represent(1,"Hopper")
print(r1)
print(r1.__repr__)
print(r1.__repr__())
rep = r1.__repr__()
r2 = eval(rep)
print(r1,type(r1),rep,type(rep),r2,type(r2))
print(r1 == r2)
print(r1 == rep)

class RedifineCompare(object):
    """ Redifine compare operation equal. """
    def __init__(self,item):
        self.item = item
    def __eq__(self,other):
        return self.item == other.item

x = RedifineCompare(5)
y = RedifineCompare(5)
print(x == y, x is y, x != y)

def counter():
    """ Simple counter, simple example of use 'nonlocal' in python language. """
    num = 0
    def incrementer():
        nonlocal num
        num += 1
        return num
    return incrementer

# 'c' is a exemplar of def counter(), wich i create below, when i call it nonlocal num increase by one
"""
Return `incrementer`: `counter` returns a reference to the
`incrementer` function, which is now a closure holding access to the `num` variable.

Creating an instance of `c`:
   - The `c` variable is an instance of the `incrementer` function returned by the `counter()` call.
   - Every time you call `c()`, you are working with the same `incrementer` function, looped into
   the `num` variable in its environment.
"""
c = counter()
print(c())
c()
c()
print(c())

List_1 = ['hello',',',' ','world','!',115,True,False,1.13]
Set_1 = {1,2,3,3,'a'}
Tuple_1 = (1,432,1.53,'hello',)
Dict_1 = {1:"one","two":2,3:3,"four":"four"}

String_1 = f"Hello, world!"
Bytes_1 = b"Hello, world!"

List_1[1] = ",,"
print(List_1)
List_1.remove(',,')
print(List_1)
List_1.append(1)
print(List_1)
List_1.insert(1,',')
print(List_1)
List_1.pop(2)
print(List_1)

Set_1.add('3')
print(Set_1)
Set_1.remove(2)
print(Set_1)
Set_1.pop()
print(Set_1)

print(Tuple_1.index('hello'))

for index,item in enumerate(List_1):
    """ Enumerate function create Tuple wich unpack to index and item . """
    print(index, item)

# Map it is a function wich make operation to each element in iterable collection and return iterator.
# lambda it is a function wich can take many variables and only one operation
x = map(lambda e: e.upper(),['one','two','three','four'])
print(list(x))
List_2 = [1,2,3,4,5,6,7,8,9,0]
print(list(map(lambda x: x+1, List_2)))

searchElement = 11
for index,iter in enumerate(List_2):
    if iter == searchElement:
        print("find {} on {} index.".format(iter,index))
        break
# Else in cycles stop only when break or return.
else:
    print("can't find {} in List".format(searchElement))

while x in range(3):
    # pass it is a zero operator, cap in any function, class, method etc
    pass

for key in Dict_1.keys():
    print(key)
for value in Dict_1.values():
    print(value)
for key,value in Dict_1.items():
    print(key,':',value)

a = 10
while True:
    a = a - 1
    print(a)
    if a<7:
        print("Done")
        break

listOfTuples = [('a','b','c'),('d','e','f'),('g','h','i')]


print(listOfTuples[-1].index('i'))
print(listOfTuples[-1].index(listOfTuples[-1][-1]))

outputString = ''
for i1,i2,i3 in listOfTuples:
    outputString += ("(" + i1 + "," + i2 + "," + i3 + ")")
    if (listOfTuples[-1][-1] == i3) and (listOfTuples[-1].index(i3) == listOfTuples[-1].index(listOfTuples[-1][-1])):
        outputString += "."
    else:
        outputString += ";"
else:
    print(outputString)

lst = ['alpha','bravo','charlie','delta','echo']
for idx,s in enumerate(lst):
    print("%s has an index of %d" % (s,idx))
    # alpha has an index of 0
    # ...

for i in range(2,4):
    print("lst at %d contains %s" % (i,lst[i]))
    # lst at 2 contains charlie
    # lst at 3 contains delta

# same cycles, from 1 to end with step 2
for s in lst[1::2]:
    print(s)
for i in range(1,len(lst),2):
    print(lst[i])

my_array = array('i',[1,2,3,4,5]) # array() function create more compact massive with 'i'-integer elements.
my_array.extend([6,7,8,9]) # extend() function extend array, this function take another array like argument.
# also we have fromlist(listName) to extend list
print(my_array)
my_array.reverse()
print(my_array)
print(my_array.buffer_info()) # return tuple where first element array memory adress, second count of elements.
print(my_array.count(9)) # return count of element in massive (1)

my_int_array = array('b', [107, 97, 116, 101])  # 'k', 'a', 't', 'e' в ASCII
print(my_int_array.tobytes().decode())

my_list = my_array.tolist()
print(my_list)

Dict_2 = {'color':'red','nickname':'zero'}

Dict_1Dict_2 = {**Dict_1,**Dict_2} # merge two dictinories to one dict if keys dublicate, chose
# to second value of dublicate key, same with Dict_1.update(Dict_2)

# get() method better than Dict_2['color'/'zero'] because if Dict_2 don't have key get() return
# none , not KeyError
print(Dict_2.get('color','zero'))

from collections import OrderedDict
Dict_3 = OrderedDict() # OrderedDict save queue isert

def nickColor(color,nickname):
    print(f'my nick is {nickname} and color {color}')

nickColor(**Dict_2) # unpacking Dict_2 values to nickColor() function

import itertools
options = {"x":["a","b"],"y":[10,20,30]}
keys = options.keys()
values = (options[key] for key in keys)
combinations = [dict(zip(keys,combination)) for combination in itertools.product(*values)]
print(combinations)
