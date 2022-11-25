'''
a=[1,2,3,4,5]
print(a)
print(type(a))
a[0]=100
print(a)

#Slicing in List

print(a[1])
print(a[-1])
print(a[0:3])
print(a[2:])
print(a[:3])

'''

#List can be hetrogeneous type

a=[1,True,'Ram',2.5]
print(a)
print(type(a))
print(type(a[0]))
print(type(a[1]))
print(type(a[2]))
print(type(a[3]))
    #List inside a List
a=[1,True,'Ram',2.5,[1,2,3,4]]
print(a)
print(type(a[4]))
print(a[4][1])