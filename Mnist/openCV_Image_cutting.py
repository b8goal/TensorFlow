from PIL import Image
import cv2

def img_trim(img,cnt,x,y,w,h): # 1152 x 1264
    img_trim = img[y:y+h,x:x+w]
    cv2.imwrite(str(cnt) + ".jpg",img_trim)
    return img_trim


flag ,cnt = 0, 0
img_color = cv2.imread('Linear Algebra and Group.jpg', cv2.IMREAD_COLOR )
x =30; y=33; #x =30; y=33;
w = 17; h = 25;  # x로 부터 width y로부터 height
img_trim(img_color, cnt,x,y,842,713)


for i in range(0,50):
    for j in range(0,29):
        if cnt//6 % 2 and flag == 1:
            x-=1
            flag=0
        else:
            flag=1
        cnt += 1
        img_trim(img_color, cnt,x+w*i,y+h*j,w,h)  # 자르고 싶은 x,y좌표 지정
