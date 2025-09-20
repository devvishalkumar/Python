letter = "Hey my name is {} and I am from {}."
name = "Vishal kumar"
state = "jharkhand"

print(letter.format(name,state))

letter = "Hey my name is {1} and I am from {0}."
print(letter.format(state,name))

print(f"Hey my name is {name} and I am from {state}.")

price = 50.25648
total = f"for only {price:.2f} Rs."
print(total)

# Docstring

def square(n):
    """Takes in a number n, returns the square of n"""
    print(n**2)
square(5)
print(square.__doc__)


