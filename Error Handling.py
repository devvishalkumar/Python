# a = input("Enter The number : ")
# print(f"multiplication table of {a} is : ")
# try:
#     for i in range(1,11):
#         print(f"{int(a)} X {i} = {int(a)*i}")
# except Exception as e:
#     print("Invalid Input!",e)

# print("Some important lines of code")
# print("End of program")

# Finally Keyword

# def func():
#     try:
#         l = [1,2,3,4,5,6]
#         i = int(input("Enter the index : "))
#         print(l[i])
#         return 1
#     except:
#         print("Some Error Occurred")
#         return 0
#     finally:
#         print("I am always executed")


# x = func()
# print(x)


# Raising custom errors

a = int(input("Enter any value between 5 and 9 : "))

if(a<5 or a>9):
    raise ValueError("value should be between 5 and 9")