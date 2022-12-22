from student import SinhVien

def main():
    sv = [SinhVien('Lê Anh Duy', 2004, 10),
          SinhVien('Thầy Giáo Ba', 2004, 1),
          SinhVien('Nguyễn Văn Minh Khánh', 2004, 100)]

    for item in sv:
        print(item)

if __name__ == "__main__":
    main()
