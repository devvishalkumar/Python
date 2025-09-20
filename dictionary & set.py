info = {
    "name" : "vishalkumar",
    "subject" : ["python","C","java"],
    "topics" : ("dict","java"),
    "age" : 17,
    "is_adult" : True,
    12.99 : 94.4
}

"""info["name"] = "vishal"
info["surname"] = "kumar"
print(info)"""

# create empty dictionary

null_dict = {}
null_dict["name"] = "helloworld"
"""print(null_dict)"""

# nested dictionary

student = {
    "name" : "vishalkumar",
    "subject" : {
        "phy" : 97,
        "che" : 98,
        "math" : 95
    }
}

print(student["subject"]["phy"])

print(len((list(student.keys()))))
print(len((list(student.values()))))
student.update({"city" : "delhi"})
print(student)

# set in python 

# set is the collection of the unordered items.
# Each element in the set must be unique & immutable.

nums = {1,2,3,4,5}

print(nums)
print(type(nums))

nums2 = {1,2,2,3,3,4,5,4,5}
print(nums2)

# repeated elements stored only once, so it resolved to {1,2,3,4,5}

collection = set()   #empty set; syntax

print(type(collection))

set1 = {1,2,3}
set2 = {2,3,4}

print(set1.union(set2))
print(set1.intersection(set2))


# Let's Practice

# Store following word meanings in a python dictionary :
    # table : "a piece of furniture","list of facts & figures"
    # cat : "a small animal"

dict = {
    "table" : ["a piece of furniture","list of facts & figures"],
    "cat" : "a small animal"
}

"""print(dict)"""


# You are given a list of subjects for students. assume one classroom
# is required for 1 subjects. how many classrooms are needed by all students.

#   "python", "java", "C++", "python", "javascript",
#   "java", "python", "java","C++", "C"

subject = {
    "python", "java", "C++", "python", "javascript",
    "java", "python", "java","C++", "C"
}

"""print(len(subject))"""


# WAP to enter marks of 3 subjects from the user and store them in a dictionary.
# Start with an empty dictionary & add one by one. use subject name as
# key & marks as value.

marks = {}
x = int(input("enter physics : "))
marks.update({"physics" : x})

x = int(input("enter chemistry : "))
marks.update({"chemistry" : x})

x = int(input("enter math : "))
marks.update({"math" : x})

print(marks)

# Figure out a way to store 9 & 9.0 as seprate values in the set. 
# (you can take help of built-in data types)

value = {
    ("float", 9.0),
    ("int", 9)
}
print(value)


