nums = []
nums.append(2)
nums.append(3)
nums.append(4)
nums.append(5)
nums.append(6)
nums.append(7)
nums.append(8)

"""
for i in nums:
    print(i)

# set function use remove the duplicate in arrya 

myset = set(['geeks','for','geeks'])
print(myset)


x = int(input('enter the number :'))
y = int(input('enter the number :'))

print(f'the sum is {x+y}')


print('print the values to stream ,or to sys.stdout by default sep\nstring inserted between valus ')


print('welcome to geeks for geeks')

print(nums[2:5])

a = 1; b= 4; c = 5

print(a);print(b)

x = 10
y = 20 
z = 20

no_of_male_students = y
no_of_teachers = x
no_of_female_students = z

if (no_of_teachers == 10 and no_of_female_students == 30
    and no_of_male_students == 20 and x + y == 30):
    print('The course is valid')

else:
    print('invalid ')



x = \
    1+2\
    +4+6\
    +10

print(x)

x = 10
flag = (x == 10) and (x < 12)
print(flag)
x = [1,2,3]
y = 2 
a = y in x
print(a)

x = 10
  
while(x != 0):   
 if(x > 5):   # Line 1 
  print('x > 5')  # Line 2 
 else:        # Line 3 
  print('x < 5') # Line 4 
 x -= 2  


import keyword
# initializing strings for testing while putting them in an array
keys = ["for", "geeksforgeeks", "elif", "elseif", "nikhil",
        "assert", "shambhavi", "True", "False", "akshat", 
        "akash", "break", "ashty", "lambda", "suman",
        "try", "vaishnavi"]
 
for i in range(len(keys)):
     # checking which are keywords
    if keyword.iskeyword(keys[i]):
        print(keys[i] + " is python keyword")
    else:
        print(keys[i] + " is not a python keyword")
        

x,y,z = input('enter the x,y,z').split(',')

print(x)
print(y)
print(z)



n = int(input())

arr = [int(x) for x in input().split()]
print(arr)
sum = 0 
for x in arr:
    sum += x 

print(sum)



from sys import stdin,stdout

def sum():
    n = stdin.readline()
    x = [int(x) for x in stdin.readline().split()]
    sum = 0 
    for x in x :
        sum += x 
    stdout.write(str(sum))

if __name__ == "__main__":
    sum()

    

import random as rd
screte_number  = rd.randint(1,10)
print ("Pick a number between 1 to 10")
while True:
    res  = input('Guess the number :')
    if res == screte_number:
        print("You win")
        break
    else:
        print('You lose')
        continue 



tuple1 = (0,1,3,4,5)
tuple2 = ('tuple','is','a','collect')

tuple3 = tuple1+tuple2

print (tuple3)



arr = set([2,3,4,2,5,2,6,7])
print(arr)
"""
#  unpacking
# def sum(a,b,c,d):
#     return a+b+c+d

# my_list = [3,4,5,6]
# print(sum(*(my_list)))

# packing 
def sum1 (*agrs):
    return sum(agrs)

print(sum1(1,2,3,4,5,6,7,8,9,10))