# String are immutable
# Method :- upper(), lower(), rstrip(), replace(), count(), capitalize() 

name = "Vishal kumar"
print(name.upper())
print(name.lower())
print(name.replace("Vishal","Ashish"))
print(name.split(" "))

str1 = "!!!!hello!!!!!!!!!!"
print(str1.rstrip("!"))

str2 = "introduction"
print(str2.capitalize()) 

str3 = "Welcome"
print(len(str3))
print(str3.center(50))
print(len(str3.center(50)))

print(str1.count("!"))

str4 = "my name is vishal kumar i am study python."
print(str4.title())