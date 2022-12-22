import os

def doc_noi_dung_tap_tin(thucmuc, ten_taptin: str) -> list:
    try:
        f = open(os.path.join(thucmuc, ten_taptin), 'rt')
        content = f.readlines()
        f.close()
        return content
    except Exception as e:
        print(e)
        return None

def main():
    path = 'D:/data/My Documents'
    filename = 'file3.txt'
    noidung = doc_noi_dung_tap_tin(path, filename)
    if noidung is None:
        print('Xay ra loi')
    else:
        print(noidung)

if __name__ == '__main__':
    main()
