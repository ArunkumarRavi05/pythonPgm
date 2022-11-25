try:
    file = open("joes.txt",'a')
    file.write("\nTutor joes Computer Education")
    file.close()
    file = open("joes.txt",'r')
    print(file.read())
except FileNotFoundError:
    print("Error : File not found")
else:
    file.close()