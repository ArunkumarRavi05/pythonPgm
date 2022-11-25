try:
    file = open("joes.txt",'w')
    file.write("This is stanley from Tutor joes")
    file.close()
    file = open("joes.txt",'r')
    print(file.read())
except FileNotFoundError:
    print("Error : File not found")
else:
    file.close()