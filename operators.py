x = 2
y = 3 
                # Arithmatic operator
print(x+y)
print(x-y)
print(x*y)
print(x/y)

                # Assignment operator

x = x+2
print(x)
x+=2
print(x)
x-=2
print(x)
x*=2
print(x)
a,b = 5,6
print(a)
print(b)
                # Unary operator

n = 7
print(n)
n = -n
print(n)

                # Relational operator

print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)

a=6
print(a==b)
print(a!=b)
print("finish Relational operator example")


                    # logical operator
                    
              #    AND             OR
              #  x  y  o         x  y  o
              #  F  F  F         F  F  F
              #  F  T  F         T  F  T
              #  T  F  F         T  T  T
              #  T  T  T         F  T  T
              

a = 5
b = 4

print(a < 8 and b < 5)
print(a < 8 and b > 5)
print(a > 8 or b > 5)
print(a < 8 or b < 5)
