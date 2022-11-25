try:
    file = open("joes.txt",'r')
    for line in file:
        print(line)
except FileNotFoundError:
    print("Error : File not found")
else:
    file.close()