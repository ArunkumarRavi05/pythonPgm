names = {"Ram","Sam","Ravi"}
print(names)
print(type(names))

#Access set elements using Loop

for name in names:
    print(name)

#Add Element

names.add('Sara')
print(names)

#UPDATE

a={'kumar','sundar','suresh'}
names.update(a)
print(names)

#Remove and Discard function in sets

names.remove('Sara')
print(names)
names.discard('suresh')
print(names)

#pop
names.pop()
print(names)

#clear
names.clear()
print(names)

#delete
del names
#print(names)


#Removes Duplicate value
names = {'Ram','Ram','Sam','Ravi','Kumar','Sundar','Suresh'}
print(names)

#Union in set
a = {1,2,3,4}
b = {'a','b','c','d'}
c = a.union(b)
print(c)
# To store b in a
a.update(b)
print(a)

#Intersection in set
a = {1,2,3,4,5}
b = {5,6,7,8,9}
c = a.intersection(b)
print(c)
# To store b in a
a.intersection_update(b)
print(a)


#Symmetric difference in set
a = {1,2,3,4,5}
b = {5,6,7,8,9}
c=a.symmetric_difference(b)
print(c)

# To store b in a
a.symmetric_difference_update(b)
print(a)


#Isdisjoint()
a = {1,2,3,4,5}
b = {5,6,7,8,9}
c = a.isdisjoint(b)
print(c)
#Issunset()
c = a.issubset(b)
print(c)
#issuperset()
c = a.issuperset(b)
print(c)


