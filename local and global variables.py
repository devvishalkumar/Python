x = 15      # Global variable

def my_function():
    global x
    x = 20
    y = 8       # Local variable
    print(y)

my_function()
print(x)