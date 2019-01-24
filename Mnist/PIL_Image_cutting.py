from PIL import Image
import os

path = "C:\\Users\\admin1\\Desktop\\AI & Big Data\\스터디\\딥러닝 스터디\\딥러닝 Mnist"
img = Image.open('Linear Algebra.jpg')
cnt, s_x, s_y, slice_x , slice_y = 0, 30, 34, 16.84, 24.55
# area = (30,34,872,746)
for i in range(0,29):
    for j in range(0,50):
        crop_img = img.crop((s_x, s_y, s_x+slice_x, s_y+slice_y))
        crop_img.save(os.path.join(path,str(cnt)+'.jpg'))
        s_x+=slice_x
        cnt+=1
    s_x = 30
    s_y += slice_y

