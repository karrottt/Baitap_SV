#Nhập một chuỗi kí tự từ bàn phím
a = input("Nhập chuỗi kí tự từ bàn phím: ")

#Nhập tên tập tin từ bàn phím
b = input("Nhập tên tập tin từ bàn phím: ")

#Lưu chuỗi ký tự ở trên vào tập tin
file = open("D:/data/My Documents/ %s.txt" % b,mode = 'w')
file.write(a)