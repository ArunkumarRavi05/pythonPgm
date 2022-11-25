a = (1,2.5,True,"Ram")
print(a)
print(type(a))
print(a[0])
print(a[1])
print(a[-1])
#Range
print(a[0:2])

b=list(a)
print(b)
b.append("Raja")
print(b)
print(type(b))
a=tuple(b)
print(a)
print(type(a))

for i in a:
    print(i)

if 'Raja' in a:
    print("Present")
else:
    print("Not found")

#length Function
print(len(a))

###############################################################
a=(1)
print(type(a))
a=(1,)
print(type(a))

############Concadinate Tuple

a = (1,2,7,4)
b = (5,6,7,8)
c = a+b
print(c)
print(c.count(7))

###########Nested Tuple

a = (1,2,7,4)
b = (5,6,7,8)
c = (a,b)
print(c)
print(c[0])
print(c[1])
print(c[0][1])

#Repetation in Tuple

x=("joes",)*10
print(x)

a=(1,2,3,4)
print(min(a))
print(max(a))
