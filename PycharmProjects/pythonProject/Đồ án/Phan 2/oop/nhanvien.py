class NhanVien:
    listNhanVien = []
    '''def __init__(self, fullname, age, wage):
        self.hoten = fullname
        self.tuoi = age
        self.luong = wage'''

#Viết hàm nhập dữ liệu cho 1 list các đối tượng thuộc lớp NhanVien
    def nhapNhanVien(self):
        fullname = input("Nhập họ tên nhân viên: ")
        age = input("Nhập tuổi nhân viên: ")
        wage = input("Nhập lương nhân viên: ")
        nv = NhanVien(fullname, age, wage)
        self.listNhanVien.append(sv)

#Viết hàm hiển thị list các đối tượng thuộc lớp NhanVien ra màn hình
    def __str__ (self):
        massage = '[Ho ten: ' + self.hoten + "; Tuoi: " + str(self.tuoi) + "; Luong: " + str(self.luong) + " đ]"
        return massage

#Viết hàm sắp xếp list các đối tượng thuộc lớp NhanVien theo chiều giảm dần của độ tuổi
    def __gt__ (self, obj):
        return (self.tuoi < obj.tuoi)

#Viết hàm lưu list các đối tượng thuộc lớp NhanVien vào tập tin nhị phân
    def luulist(self):
        file = open("%s.bin" % b,mode = 'xb')
        file.write
#Viết hàm đọc list các đối tượng thuộc lớp NhanVien từ tập tin nhị phân
    def doclist(self):
        file = open("%s.bin" % b, mode='xb')
        file.read

