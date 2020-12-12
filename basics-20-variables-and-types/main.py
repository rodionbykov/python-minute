#
# integers
#

a = 42
b = 6
c = a + b
print(a)
print(b)
print(c)

# show type of variable
print(type(c))

# basic math with integers
d = (c + 14) * 2

# power
e = d ** 2
print(d)
print(e)

#
# floating point numbers
#

# square of large papa john's pizza diameter = 34cm
pi = 3.1415
r = 17
sq = pi * r * r
print(pi)
print(sq)

# division is always produce a float
f = 42
g = f / 6
print(f)
print(g)

# show type of variable
print(type(g))

# integer division
e = f // 5
print(e)
# remainder of division
h = f % 5
print(h)

#
# strings
#

s = "Some text in the string"
print(s)

# show type of variable
print(type(s))

# multiline strings
mls = """
this 
is
a
multiline
string
"""

print(mls)

# uppercase a string
print(s.upper())

# concatenate strings
firstname = "John"
lastname = "Smith"
fullname = firstname + " " + lastname
print(fullname)

# split a string
print(fullname.split(" "))

# formatted string
greeting = f"Hello, {firstname}"
print(greeting)
