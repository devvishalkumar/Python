# def cube(x):
#     return x * x * x

# print(cube(2))

# l = [1, 2, 3, 4, 6, 3]
# newl = []
# for item in l:
#     newl.append(cube(item))

'''newl = list(map(cube,l))
print(newl)
'''
# Filter

'''def filter_function(a):
    return a>2

newnewl = list(filter(filter_function,l))
print(newnewl)'''

from functools import reduce

# list of numbers
numbers = [1, 2, 3, 4, 5]

# calculate the sum of the numbers using the reduce function

# def my_sum(x,y):
#     return x + y

sum = reduce(lambda x, y: x + y, numbers)

# sum = reduce(my_sum, numbers)

# print the sum
print(sum) 