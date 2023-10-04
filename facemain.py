import attendencename as f
import attendencemain as d
import os

print(".....HỆ THỐNG NHẬN DIỆN KHUÔN MẶT.....\n")
i = 1
while 0 < i < 3:
    print("* Nhập một số để thực hiện các chức năng sau\n")
    print("1.Thu thập dữ liệu ảnh khuôn mặt để đào tạo")
    print("2.Nhận diện khuôn mặt và tiến hành điểm danh\n")
    try:
        i = int(input("user input::-"))
    except ValueError:
        print("\nDữ liệu không hợp lệ. Vui lòng nhập lại thông tin.\n")
        continue
    if i == 1:
        k = input("Nhập tên Class: ")
        if not os.path.isdir(k):
            os.makedirs(k)
            print("Class mới đã được tạo - : ", k)
        else:
            print(k, "đã tồn tại.")
        f.extract(k)
    elif i == 2:
        k = input("Nhập tên Class: ")
        if not os.path.isdir(k):
            print(k, "không tồn tại.")
        else:
            print(k, "đã tồn tại\n")
            g = input("Nhập tên tệp .jpg để tiến hành nhận diện khuôn mặt và điểm danh: ")
            d.verify(k, g)
    else:
        print("\nLựa chọn không hợp lệ. Vui lòng nhập lại thông tin.")
