# Loops :-  Loops are used to repeat instructions.

# while loop

count = 1
while count <= 5 :
    print("hello",)
    count +=1

# print numbers from 1 to 5

i = 1
while i <= 5 :
    print(i)
    i+=1

print("end 1 to 5")

# print numbers from 5 to 1  

i = 5
while i >= 1 :
    print(i)
    i-=1

print("end 5 to 1")

# Let's Practice

# Print number from 1 to 100.

i = 1
while i <= 100 :
    print(i)
    i += 1

print("question solved ")

# print numbers from 100 to 1.

i = 100
while i >= 1 :
    print(i)
    i -= 1

print("question solved ")

# print the multiplication table of a number n.

"""i = 1
n = int(input("enter number : "))

while i <= 10 :
    print(n*i)
    i += 1

print("question solved")"""

# print the elements of the following list using a loop.
#   [1,4,9,16,25,36,49,64,81,100]

nums = [1,4,9,16,25,36,49,64,81,100]

idx = 0
while idx < len(nums) :
    print(nums[idx])
    idx += 1

print("question solved ")

# search for the number x in this tuple using loop:
#   (1,4,9,16,25,36,49,64,81,100)

nums = (1,4,9,16,25,36,49,64,81,100,25)

x = 25

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("FOUND at idx :", i)
    else:
        print("finding...")
    i += 1

# Break & Continue

i = 1
while i <= 10 :
    print(i)
    if(i == 5):
        break
    i += 1

print("end of loop")

i = 0
while i <= 10:
    if(i%2 != 0):
        i += 1
        continue    #skip
    print(i)
    i += 1

print("end of loop")

# for loop :- loop are used sequential traversal. for traversing list,string,tuples etc.

list = [1,2,3,4,5,6,7,12]

for val in list:
    print(val)

tup = (12,13,14,15,10)

for vals in tup:
    print(vals)

str = "vishalkumar"

for char in str:
    print(char)

# Let's Practice
# using for

# print the element of the following list using a loop:
#   [1,4,9,16,25,36,49,64,81,100]

list = [1,4,9,16,25,36,49,64,81,100]
for nums in list:
    print(nums)

print("question solved")

# search for a number x in this tuple using loop:
#   (1,4,9,16,25,36,49,64,81,100)

tup = (1,4,9,16,25,36,49,64,81,100)
x = 64

idx = 0
for vals in tup:
    if vals == x:
        print("x is found at idx :",idx)
        break
    idx += 1

# Range() :- Range functions returns a sequence of numbers,starting from 
# 0 by default, and increments by 1(by default),and stops before a specified number.

#   range( start?,stop,step?)

for i in range(10):  #range(stop)
    print(i)
print("end")

for i in range(2,10):  #range(start,stop)
    print(i)
print("end")

for i in range(2,10,2):  #range(start,stop,step)
    print(i)
print("end")

# Let's Practice
# using for & range()

# Print numbers from 1 to 100.

for i in range(1,101):
    print(i)
print("end")

# Print numbers from 100 to 1.

for i in range(100,0,-1):
    print(i)
print("end")

# Print the multiplication table of a number n.

"""n = int(input("enter number : "))

for i in range(1,11):
    print(n*i)
print("end")"""

# Pass Statement :- pass is a null statement that does nothing.It is used
# as a placeholder for future code.

for i in range(5):
    pass

if i > 5 :
    pass
print("some useful work")

# Let's Practice

# WAP to find the sum of first n numbers.(using while)

n = int(input("enter number : "))
sum = 0

i = 1
while i <= n :
    sum += i
    i += 1

print("total sum : ",sum)


# WAP to find the factorial of first n numbers. (using for)

n = int(input("enter number : "))
fact = 1

for i in range(1,n+1):
    fact *= i


print("factorial of number is : ",fact)


# WAP to create a table of n number by taken user input.
n = int(input("Enter a number : "))
for i in range(1,11):
    print(n, "*", i, "=", n * i)