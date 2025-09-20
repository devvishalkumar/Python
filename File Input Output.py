# Reading a File;
"""f = open("demo.txt","r")
data = f.read()
print(data)
print(type(data))
f.close()"""

# Writing a File;
"""f = open("demo.txt","w")
f.write("I want to learn JavaScript tommorrow.")

f.close()"""

# Appending a File;
"""f = open("demo.txt","a")
f.write("\nThen I'll move to ReactJS.")
f.close()"""


"""f = open("sample.txt","w")
f.write("This is my sample file.")
f.close()"""


"""f = open("sample.txt","r+")
f.write("That")
print(f.read())
f.close()"""


"""f = open("sample.txt","w+")
f.read()
f.close()"""


"""f = open("sample.txt","a+")
f.write("abc")
f.close()"""


# with syntax :

"""with open("demo.txt","r") as f:
    data = f.read()
    print(data)"""


"""with open("demo.txt","w") as f:
    f.write("New data")"""


# Deleting a file :
# using the os module
#   Module (like a code library) is a file written by another programmer
#   that generally has a function we can use.

"""import os

os.remove("demo.txt")"""

# Let's Practice 

# Create a new file "practice.txt" using python.Add the following data in it.
#   Hi everyone
#   we are learning File I/O
#   using Java.
#   I like programming in Java.

"""with open("practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning File I/O\n")
    f.write("using Java.\nI like programming in Java.")
"""

# WAF that replace all occurrence of "java" with "python" in above file.
"""def replace_word():
    with open("practice.txt","r") as f:
        data = f.read()
    new_data = data.replace("Java","python")
    print(new_data)

    with open("practice.txt","w") as f: 
        f.write(new_data) 

replace_word()"""

# Search if the word "learning" exists in the file or not.
"""def check_for_line():
    word = "learning"
    with open("practice.txt","r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("FOUND")
        else:
            print("not found")

check_for_line()"""

# WAF to find  which line of the file does the word "learning" occur first.
# Print-1 if word not found.

"""def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1

    return -1

check_for_line()"""

# From a file containing numbers seprated by commas,print the count of even nmbers.

count = 0
with open("practice.txt","r") as f:
    data = f.read()

    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1

print(count)
