#Nhập tên tập tin từ bàn phím
a = input("Nhập tên tập tin từ bàn phím: ")

#Đọc nội dung tập tin và in ra màn hình
file = open('D:/data/My Documents/%s.txt' % a, mode = 'r')
print(file.read(3))

#Ghi danh sách trên vào tập tin theo quy tắc:
