try:
    file = open("joes.txt",'r')
    print(file.readline())
    print(file.readline(2))
except FileNotFoundError:
    print("Error : File not found")
else:
    file.close()


                        # readlines()
try:
    file = open("joes.txt", 'r')
    #print(file.readline())
    #print(file.readline(2))
    print(file.readlines())
except FileNotFoundError:
    print("Error : File not found")
else:
    file.close()
