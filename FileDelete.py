import os
if os.path.exists("test.txt"):
    os.remove("test.txt")
    #os.rmdir("folder_name")
else:
    print("File not found")