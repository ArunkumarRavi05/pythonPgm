'''
para = ["25","26","27","33"]
print(para)
print(para[2])
print(','.join(para))
print('|'.join(para))
'''

para = []
print("Enter a para :")
while True :
    line = input()
    if line :
        para.append(line)
    else :
        break

print(para)
output = '\n'.join(para)
print(output)
