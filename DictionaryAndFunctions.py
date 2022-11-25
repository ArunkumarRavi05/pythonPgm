user = {
    'name':'Ram',
    'age':25,
    'isMarried':True
}
print(user)
print(type(user))
print(user['name'])
print(user.get('age'))
print(user.keys())
print(user.values())
print(user.items())

for x in user:
    print(x,"",user[x])

#To print only values
for x in user.values():
    print(x)

#To print only keys
for x in user.keys():
    print(x)

#To print items
for x,y in user.items():
    print(x,y)

#To check particular index
if 'age' in user:
    print("present")

if 'gender' in user:
    print("present")


#To add new index
#changing values #UPDATE

user.update({'gender':'male'})
print(user)
user['age'] = 35
print(user)

user.pop("age")
print(user)
user.clear()
print(user)
#del user
print(user)

#####################   NESTED Dictionary
users = {
    "user1":{
        'name':'Ram',
        'age': 25,
        'isMarried':True
    },
    "user2":{
        'name': 'Sam',
        'age': 35,
        'isMarried': False
    }
}

print(users)