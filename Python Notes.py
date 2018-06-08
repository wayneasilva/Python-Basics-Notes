##Functions with Parameters##

def basic_window(width,height,font='TNR',
                 bgc='w',scrollbar=True):
    print(width,height,font,bgc,)

basic_window(500,350,)
###############################################
##Global vs Local Var##

x = 6

def example():
    globx = x
    print(globx)
    globx += 5
    print(globx)

    return globx

x = example()
print(x)
###############################################
##Append##

text = []

for i in range(0,69):
    text.append(69)

print(text)
print('\n')
print('Length = ', len(text))
print(len(text))
###############################################
##Open/Write/Close File##

text = 'asdasda'

saveFile = open('exampleFile.txt','w')
saveFile.write(text)
saveFile.close()
###############################################
##Open/Append/Close File##

appendMe = '\n all the information)'

appendFile = open('exampleFile.txt','a')
appendFile.write(appendMe)
appendFile.close()
###############################################
##Open/Read/Readlines/

readMe = open('exampleFile.txt', 'r').read()
readMe = open('exampleFile.txt', 'r').readlines()
readMe = close()
print(readMe)
###############################################
##Modules/Statistics Module##

import statistics

example_list = [5,3,2,4,6,4,5,45,6,7,3,8,9,2,1,3,4,1,2,3,]

x = statistics.mean(example_list)
x = statistics.median(example_list)
x = statistics.mode(example_list)
x = statistics.stdev(example_list)
x = statistics.variance(example_list)

print(x)
###############################################
##Module Import Syntax##

from statistics import variance as v,mean as m

example_list = [4,3,5,6,77,5,4,3,4,5,9,8,9,2,1,18]

x = v(example_list)
y = m(example_list)

print(x)
print(y)
###############################################
#Tuples

#x = 5,6,2,6
#x = (5,6,2,6)

#Lists

#y = [5,6,2,6]

#Example

#def example_function():
#    return 15,6

#x,y = example_function()
###############################################
x = [1,2,5,34,3,4,5,4,3,5,5,6,245,6,]
y = [1,2,5,34,3,4,5,4,3,5,5,6,245,6,]
z = [1,2,3,4,5,6,7,8,9,10]
s = [5,3,8,4,1,9,6,8,6,7,2,9,1,0,2,5,4,]
names = ['Jenny', 'Jan','Marsha', 'Bob', 'Doug', 'Alisha','Carlton','Zedd']

#x.append(2)
y.insert(2,99)
z.remove(2)
z.remove(z[5])

print(x)
print(y)
print(z[5])
print(s[5:7])
print(s[-2])
print(s.index(2))
print(s.count(6))
s.sort()
print(s)
names.sort()
print(names)
###############################################
##Multi-dimensional Lists##

#multi-list 4 in 1
x = [
    [[5,7],[6,6]],
    [[6,6],[7,8]],
    [7,2],[2,5]
    ]

#print element of index [1][0][0] of list x
print(x[1][0][0])
#################################

