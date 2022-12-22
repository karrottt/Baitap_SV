import numpy as np

x = np.random.randint(-1000, 1000, (1000,10))
print(x)

a = input("Nhập tên file:")
file = open('D:/data/My Documents/%s.txt' %a, 'w')

#Ghi danh sách trên vào tập tin theo quy tắc:
def write_to_file():
    m = 10
    b = list(range(n))
    for i in range(n//m + int(n%m>0)):
        file.write(','.join([str(i) for i in b[i*m:(i+1)*m]])+'\n')

write_to_file()
file.close()
#Đọc nội dung tập tin ở trên và in ra màn hình theo quy tắc:
filee = open('D:/data/My Documents/file4.txt', mode = 'r')
print(filee.read())