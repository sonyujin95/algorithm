import cv2
import numpy as np

def img_crop(ori, new):
    if len(ori.shape) == 2:
        for i in range(len(new)):
            for j in range(len(new[0])):
                new[i][j] = ori[i][j]

    elif len(ori.shape) == 3:
        for i in range(len(new)):
            for j in range(len(new[0])):
                for c in range(3):
                    new[i][j][c] = ori[i][j][c]
    return new

iu = cv2.imread("image/iu_201908_.png")
iu_gray = cv2.cvtColor(iu, cv2.COLOR_RGB2GRAY)
print(iu_gray)

crop = np.zeros((300, 700, 3), dtype=np.uint8)  # (행, 열, 채널)
crop_gray = np.zeros((300, 700), dtype=np.uint8)

a = img_crop(iu, crop)
b = img_crop(iu_gray, crop_gray)
print(a, b)

cv2.imshow('iu', iu)
cv2.imshow('iu_gray', iu_gray)
cv2.imshow('color', a)
cv2.imshow('gray', b)
cv2.waitKey()
cv2.destroyAllWindows()