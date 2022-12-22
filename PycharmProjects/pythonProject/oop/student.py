class SinhVien:
  def __init__(self, fullname: str, yob, score: float):
    self.hoten = fullname
    self.namsinh = yob
    self.dtb = score

  def __str__(self) -> str:
    massage = '[Họ tên: ' + self.hoten + '; năm sinh: ' + str(self.namsinh) + '; ĐTB: ' + str(self.dtb) + ']'
    return massage

  #Lớn hơn
  def __gt__(self, obj):
    return(self.dtb > obj.dtb)
  #Lớn hơn hoặc bằng
  def __ge__(self, obj):
    return (self.dtb >= obj.dtb)
  #Nhỏ hơn
  def __lt__(self, obj):
    return (self.dtb < obj.dtb)
  #Nhỏ hơn hoặc bằng
  def __le__(self, obj):
    return (self.dtb <= obj.dtb)
  #So sánh bằng
  def __eq__(self, obj):
    return (self.dtb == obj.dtb)