# add item on the end of list

a = ['dog', 'dog', 'dog']
a.append("snake")
print(a)

# add item at the specified position

b = [1,2,3]
b.insert(2, 4)
print(b)

# add items of a list to the end of the current list

c = ['cat', 'hamster', 'elephant']
d = ['car', 'ring']
c.extend(d)
print(c)

# remove all items in the list

u = ['item']
u.clear()
print(u)

# return copy of the list

e = ['apple','banana','orange']
i = e.copy()
print(i)

# count items

o = ['apple','banana','orange', 'apple']
x = o.count('apple')
print(x)

# return the index of the first item of given value

y = ['gucci','prada','fendi','balenciaga']
v = y.index('fendi')
print(v)

# remove item from the position

n = [1,2,3]
n.pop(0)
print(n)

# remove item by value

r = ['a','b','c']
r.remove('b')
print(r)

# reverse list

w = [1,2,3,4,5]
w.reverse()
print(w)

# sort the list
l = ['b','e','a','c','d']
l.sort()
print(l)

# sort the list using function
m = ['bird','dog','elephant','cat','mouse','giraffe']
n = sorted(m, key=len)
# len('dog') = 3, len('bird') = 4, len('mouse') = 5, so the order will be: 'dog','bird','mouse'
print(n)