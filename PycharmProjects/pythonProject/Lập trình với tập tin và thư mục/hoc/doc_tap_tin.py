import os

path = 'D:/data/My Documents'
filename = 'file3.txt'
#Cach 1
#f = open('D:/data/My Documents/file3.txt', 'rt')
#content = f.readlines()
#f.close()
#print(content)

#Cach2
#with open(os.path.join(path, filename), 'rt') as f:
#    content = f.readlines()
#print(content)

#Cach 3
try:
    f =open(os.path.join(path, filename), 'rt')
    content = f.readlines()
    print(content)
except Exception as e:
    print('Error: ', e)

print('Ket thuc chuong trinh')