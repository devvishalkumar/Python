# function definition

# first method
def calc_sum(a,b):
    sum = a+b
    print(sum)
    return sum

calc_sum(4,5)
calc_sum(44,55)
calc_sum(24,35)
calc_sum(40,26)

# second method
def calc_sum(a, b):  #parameters
    return a + b

sum = calc_sum(4,5)   #function call ; arguments
print(sum)
sum = calc_sum(44,55)
print(sum)
sum = calc_sum(24,35)
print(sum)
sum = calc_sum(40,26)
print(sum)

# average of 3 numbers

def calc_avg(a,b,c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg

calc_avg(92,95,98)

# Let's Practice

# WAF to print the length of a list. (list is the parameter)

cities = ["palamu","ranchi","hazaribagh","dhanbad","dumka","daltonganj"]

def print_list(list):
    print(len(list))

print_list(cities)

# WAF to print the elements of a list in a single line. (list is the parameter)

heroes = ["thor","ironmen","captain america","shaktiman"] 

def print_list(list):
    for items in list:
        print(items,end=" ")

print_list(heroes)

# WAF to find the factorial of n. (n is the parameter)

def cal_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)

cal_fact(5)

# WAF to convert USD to INR.

usd = int(input("enter usd:"))

def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val,"USD =",inr_val,"INR")

converter(usd)

# WAF to print ODD or EVEN number,
# if user input a number gives output ODD or EVEN.

num = int(input("enter number :"))

def Check_num(nums):
    if (num % 2 == 0):
        print("EVEN")
    else:
        print("ODD")

Check_num(num)

# recursion

# recursive function
def show(n):
    if(n == 0):
        return
    print(n)
    show(n - 1)

show(5)

def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) * n

print(fact(6))

# Let's Practice

# Write a recursive function to calculate the sum of first n natural numbers.

def calc_sum(n):
    if(n == 0):
        return 0
    return calc_sum(n-1) + n

sum = calc_sum(5)
print(sum)

# Write a recursive function to print all element in a list.
# Hint : use list & index as parameter.

def print_list(list,idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

fruits = ["mango","litchi","apple","banana"]

print_list(fruits)
