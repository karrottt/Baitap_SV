#Nhập tên tập tin từ bàn phím
a = input("Nhập tên tập tin từ bàn phím: ")

#Nhập một chuỗi kí tự từ bàn phím
b = input("Nhập chuỗi kí tự từ bàn phím: ")

#Ghi chuỗi kí tự này vào cuối tập tin ở trên

file = open('D:/data/My Documents/%s.txt' % a, mode = 'a')
file.write(b)
