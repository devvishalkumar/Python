#  Create a Calculator

first = int(input ("enter first number : "))
second = int(input ("enter second number : "))
operator = input("available operator is +, -, *, / : ")

if(operator == "+"):
    print(first + second)
elif(operator == "-"):
    print(first - second)
elif(operator == "*"):
    print(first * second)
elif(operator == "/"):
    print(first / second)

