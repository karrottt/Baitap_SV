# Khai báo danh sách các số
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 2, 1, 10]

# Nhập số n từ bàn phím
n = int(input("Nhập số n: "))

# Tìm số n trong danh sách
if n in numbers:
  # Duyệt qua từng phần tử trong danh sách và lấy ra các vị trí có giá trị bằng với n
  positions = []
  for i, num in enumerate(numbers):
    if num == n:
      positions.append(i)
  print(f"Tìm thấy số n trong danh sách tại các vị trí: {positions}")
else:
  print("Không tìm thấy số n trong danh sách")