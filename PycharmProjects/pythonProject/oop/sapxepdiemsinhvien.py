from student import SinhVien
sv = [SinhVien('Lê Anh Duy', 2004, 10),
      SinhVien('Thầy Giáo Ba', 2004, 1),
      SinhVien('Nguyễn Văn Minh Khánh', 2004, 100),
      SinhVien('Nguyễn Văn A', 2004, 5),
      SinhVien('Nguyễn Văn B', 2004, 4)]

print("SX tăng dần ĐTB")
sv = sorted(sv)
for item in sv:
    print(item)
print()
print("SX giảm dần ĐTB")
sv = list(reversed(sv))
for item in sv:
    print(item)

