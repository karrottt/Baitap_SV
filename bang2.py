#Mở 1 tập tin văn bản (đường dẫn và tên file do bạn tự xác định) để đọc
file1 = open('D:/data/My Documents/file2.txt', mode = 'r')

print("Tên của file là:", file1.name)
print("File có đóng hoặc không? :", file1.closed)
print("Chế độ mở file :", file1.mode)

print('#######################################################################################################################################')
#Mở 1 tập tin văn bản (đường dẫn và tên file do bạn tự xác định) để ghi
file2 = open('D:/data/My Documents/file2.txt', mode = 'r+')

print("Tên của file là:", file2.name)
print("File có đóng hoặc không? :", file2.closed)
print("Chế độ mở file :", file2.mode)

print('#######################################################################################################################################')
#Mở 1 tập tin nhị phân (đường dẫn và tên file do bạn tự xác định; có thể chọn 1 file ảnh) để đọc và ghi
file3 = open('D:/data/My Documents/xing.jpg', mode = 'rb+')

print("Tên của file là:", file3.name)
print("File có đóng hoặc không? :", file3.closed)
print("Chế độ mở file :", file3.mode)

print('#######################################################################################################################################')
#Mở 1 tập tin văn bản để đọc, biết các kí tự của tập tin này tuân theo chuẩn Unicode – UTF-8
file4 = open('D:/data/My Documents/file3.txt', mode = 'r', encoding = 'utf-8')

print("Tên của file là:", file4.name)
print("File có đóng hoặc không? :", file4.closed)
print("Chế độ mở file :", file4.mode)

print('#######################################################################################################################################')
#Thao tác đóng tập tin
file1.close()
print("File1 có đóng hoặc không? :", file1.closed)
file2.close()
print("File2 có đóng hoặc không? :", file2.closed)
file3.close()
print("File3 có đóng hoặc không? :", file3.closed)
file4.close()
print("File4 có đóng hoặc không? :", file4.closed)

print('#######################################################################################################################################')
#Mở tập tin văn bản để đọc bằng cấu trúc câu lệnh try: .... finally:
try:
    file5 = open("D:/data/My Documents/file3.txt", mode = 'r')
finally:
    file5.close()
print("File1 có đóng hoặc không? :", file1.closed)
print('#######################################################################################################################################')
#Mở tập tin văn bản để đọc bằng cấu trúc: with ... as f:
try:
    file6 = open("D:/data/My Documents/file2.txt", mode = 'r') # thực hiện các thao tác với tệp
finally:
    file6.close()

print('#######################################################################################################################################')
#Mở tập tin văn bản Unicode và ghi vào 3 dòng có nội dung tùy ý bạn
with open("D:/data/My Documents/file2.txt",mode = 'a') as file2:
    file2.write("123")
    file2.write("456")
    file2.write("789")

print('#######################################################################################################################################')
#Mở tập tin văn bản Unicode, đọc toàn bộ nội dung của văn bản và in ra màn hình
file6 = open('D:/data/My Documents/file3.txt', mode = 'r')
a= file6.read()
print(a)

print('#######################################################################################################################################')
#Mở tập tin nhị phân (chọn 1 bức ảnh), đọc và ghi toàn bộ nội dung tập tin ra màn hình.
file7 = open('D:/data/My Documents/xing.jpg', mode = 'rb+')
c= file7.read()
print(c)

