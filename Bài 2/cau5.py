#Sinh ngẫu nhiên 1 danh sách gồm 1000 số nguyên trong khoảng từ [-1000, 1000]
import numpy as np
np.random.seed(123)

x = np.random.randint(low = -1000, high = 1000, size = 1000)
print(x)

#Nhập tên tập tin từ bàn phím
a = input("Nhập tên tập tin từ bàn phím: ")

#Ghi danh sách trên vào tập tin theo quy tắc:
file = open("D:/data/My Documents/ %s.txt" % b,mode = 'w')
b = 0
c = 10
for i in range(b, len(v5)):
  if i <= c:
    print(i)
    b += 10
    c += 10
    file.write(" %s," % a)

#Đọc nội dung tập tin ở trên và in ra màn hình theo quy tắc:
file = open("D:/data/My Documents/ %s.txt" % b,mode = 'w')
b = 0
c = 10
for i in range(b, len(v5)):
  if i <= c:
    print(i)
    b += 10
    c += 10
    file.read(" %s  " % a)
