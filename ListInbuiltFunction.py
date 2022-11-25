'''
a = [10,25,35,45]
print(a)
a.clear()
print(a)

'''
a = [10,25,35,45]
b = a.copy()
print(b)

a = [10,25,35,25,4,45,25]
print(a.count(25))
print(a.index(25))
print(len(a))
print(max(a))
print(min(a))
print(a)
a.pop(1)
print(a)

#####################################
a = [10,25,35,45,25,4,25]
print(a)
a.remove(25)
print(a)
print("----------------------")
names = ["Ram"]
print(names)
names.append("sam")
names.append("Ravi")
names.append("kumar")
print(names)

#Extend() function used to join two list

name2 = ['sara','Anitha']
names.extend(name2)
print(names)

#insert() function

names.insert(0,'suriya')
print(names)