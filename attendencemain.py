# np.save('ten_tep', mang_can_luu): luu 1 mang np vao 1 file .npy
# np.load(): tai du lieu tu tep .npy da duoc luu tru truoc do bang np.save()
# face_recognition.load_image_file("image.jpg"): nap 1 file anh tra ve 1 mang np bieu thi hinh anh
# face_recognition.face_encodings(): ma hoa khuon mat tra ve mang np danh sach ma hoa tat ca khuon mat tim thay trong anh

import os
import face_recognition
import cv2
import numpy as np
from PIL import Image, ImageDraw
import pickle
import ex as et


def verify(v, we):  # v: class, we: ảnh
    import remove as f
    known_face_encodings = []   # file -en.npy
    known_face_names = []       # mang ten
    m = 1
    f.clean(v)
    t = None
    l = []
    r = []
    b = []
    u = []
    fonts = cv2.FONT_HERSHEY_SIMPLEX
    w = 0
    org = (50, 50)
    fontScale = 1
    color = (255, 0, 0)
    thickness = 2
    s = []
    all_face_encodings = {}
    path1 = v + "/"
    h = ""      # tên
    d = []      # list tên
    listing = os.listdir(path1)
    for file in listing:
        k = str(file)
        print(file)
        for p in k:  # lấy tên ảnh gán vào h
            if p == '.':
                break
            h = h + p
        d.append(h)
        h = ""
    print("Đào tạo và mã hóa khuôn mặt [##", end="")
    for o in d:
        shah_image = face_recognition.load_image_file(v + "/" + str(o) + ".jpg")
        np.save(v + "/" + str(o), shah_image)
        print("#", end="")
        shah_encoding = face_recognition.face_encodings(shah_image)[0]
        np.save(v + "/" + str(o) + "-en", shah_encoding)
        print("#", end="")
    for o in d:
        shah_image = np.load(v + "/" + str(o) + ".npy")
        all_face_encodings[str(o)] = face_recognition.face_encodings(shah_image)[0]
        print("#", end="")
    with open(v + "/" + 'dataset_sali1.dat', 'wb') as f:
        pickle.dump(all_face_encodings, f)
    print("##]Completed")
    print("\nBắt đầu so sánh [##", end="")
    for o in d:
        print("##", end="")
        shah_encoding = np.load(v + "/" + str(o) + "-en.npy")
        known_face_encodings.append(shah_encoding)
        known_face_names.append(str(o))
    test_images = face_recognition.load_image_file(we)
    face_locations = face_recognition.face_locations(test_images)
    face_encoding = face_recognition.face_encodings(test_images, face_locations)
    pil_image = Image.fromarray(test_images)
    draw = ImageDraw.Draw(pil_image)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encoding):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        print("#", end="")
        name = "unknown"
        if True in matches:
            print("#", end="")
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
        draw.rectangle(((left + 2, top + 2), (right + 2, bottom + 2)), outline=(0, 255, 255), width=5)
        print("#", end="")
        text_size = cv2.getTextSize(name, fonts, fontScale, thickness)[0]
        text_width, text_height = text_size[0], text_size[1]
        # draw.rectangle(((left,bottom-text_height-10),(right,bottom)),fill=(0,0,0),outline=(0,0,0),width=5)
        # draw.text((left+6,bottom-text_height-5),name,fill=(255,255,255,255))
        l.append(left)
        r.append(right)
        print("#", end="")
        u.append(text_height)
        b.append(bottom)
        #  print(name)
        s.append(name)
        print("#", end="")
        w = w + 1
    del draw
    ku = et.reads(s, v)     # mang sv vang mat
    print("##]Completed")
    print(ku)
    pu = 0
    for ju in ku:
        pu = pu + 1
    if pu == 0:
        print("Tất cả đều có mặt")
    else:
        for ju in ku:
            print(ju)
        print("vắng")
    img = np.array(pil_image)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # print(s)
    for t in s:
        print(".", end="")
    if t is not None:
        for z in range(0, w):
            # print(t)
            img = cv2.putText(img, s[z], (l[z] + 6, b[z] - u[z]), fonts,
                              fontScale, color, thickness, cv2.LINE_AA)
    # scale_percent = 60 # percent of original size
    # width = int(img.shape[1] * scale_percent / 100)
    # height = int(img.shape[0] * scale_percent / 100)
    # dim = (width, height)
    # img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    cv2.imshow("test", img)
    print("press any key to continue")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

