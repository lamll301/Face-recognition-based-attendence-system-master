# remove các file có đuôi .npy or .dat
import os
def clean(d):   # d: class
    i = 0
    listing = os.listdir(d+"/")
    for file in listing:
        # print(file)
        for k in file:  # kiểm tra ký tự trong tên
            if k == ".":
                i = 1
            if i >= 1 and k == "n" or k == "d":
                i = i+1
            if i >= 1 and k == "p" or k == "a":
                i = i+1
            if i >= 1 and k == "y" or k == "t":
                i = i+1
        if i == 4:  # .npy or .dat
            os.remove("D:\\Project\\Face-recognition-based-attendence-system-master\\" + d + "\\" + file)
            # print("file removed")
            i = 0
