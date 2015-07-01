def a(x):
   '''
   x: int or float.
   '''
   return x + 1

def b(x):
   '''
   x: int or float.
   '''
   return x + 1.0

def c(x, y):
   '''
   x: int or float. 
   y: int or float.
   '''
   return x + y

def d(x, y):
   '''
   x: Can be of any type.
   y: Can be of any type.
   '''
   return x > y

def e(x, y, z):
   '''
   x: Can be of any type.
   y: Can be of any type.
   z: Can be of any type.
   '''
   return x >= y and x <= z

def f(x, y):
   '''
   x: int or float.
   y: int or float
   '''
   x + y - 2
 
z1 = a(1)
z2 = b(2)
z3 = c(1, 2)
z4 = d(1.0, 2)
z5 = e(True, 1.0, 3)
z6 = f(1,2)

y1 = a(6)
y2 = a(-5.3)
y3 = a(a(a(6)))
y4 = c(a(1), b(1))
y5 = d('apple', 11.1)
y6 = e(a(3), b(4), c(3, 4))
y7 = f

print(type(z1))
print(type(z2))
print(type(z3))
print(type(z4))
print(type(z5))
print(type(z6))

print (type(y1), y1)
print (type(y2), y2)
print (type(y3), y3)
print (type(y4), y4)
print (type(y5), y5)
print (type(y6), y6)
print (type(y7), y7)

print("..............")

def a(x, y, z):
     if x:
         return y
     else:
         return z

def b(q, r):
    return a(q>r, q, r)

x1 = a(False, 2, 3)
print (type(x1), x1)
x2 = b(3,2)
print (type(x2), x2)
x3 = a(3>2, a, b)
print (type(x3), x3)
x4 = b(a,b)
print (type(x4), x4)