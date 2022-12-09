#Sử dụng thư viện os
import os

'#######################################################################################################################################'
#In ra màn hình thư mục làm việc hiện tại của chương trình
def current_path():
    print('Thư mục hiện tại:', os.getcwd())
    print()
current_path()

'#######################################################################################################################################'
#Chuyển đến thư mục: ‘D:/data’, sau đó in thư mục hiện tại ra màn hình
os.chdir('D:/data/')
current_path()

'#######################################################################################################################################'
#Tạo thư mục con có tên là ‘nnlt’, sử dụng hàm makedirs()
#Thư mục con
directory = 'nnlt'
#Đường dẫn đến thư mục gốc
parent_dir = 'D:/data/'
path = os.path.join(parent_dir, directory)
os.makedirs(path)
print("Directory '% s' created" % directory)

'#######################################################################################################################################'
#Liệt kê tất cả các tập tin và thư mục có trong thư mục ‘My Documents’ trên máy tính của bạn và in ra màn hình
path = "D:/data/My Documents/"
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")
# print the list
print(dir_list)

'#######################################################################################################################################'
#Kiểm tra 1 file (tự nhập đường dẫn và tên tập tin gồm cả phần mở rộng) có tồn tại trong máy hay không, sử dụng hàm os.path.exists()
def kiem_tra_file(path):
    result = os.path.exists(path)
    print(result)
    return result
#test
kiem_tra_file("D:/data/My Documents/")
kiem_tra_file("D:/data/My Documents/file1.txt")

'#######################################################################################################################################'
#Xóa 1 thư mục và xóa 1 file trong máy tính
#Xóa 1 file
location = "D:/data/My Documents/"
path = os.path.join(location, "file1.txt")
os.remove(path)

#Xóa 1 thư mục
directory = "bachayconbochet"
parent = "D:/data/My Documents/"
path = os.path.join(parent, directory)

os.rmdir(path)