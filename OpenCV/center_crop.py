import cv2
import numpy as np

iu = cv2.imread("image/iu_201908_.png")
iu_gray = cv2.cvtColor(iu, cv2.COLOR_RGB2GRAY)
# print(iu_gray)

H = int(iu.shape[0]/2)
W = int(iu.shape[1]/2)


c_size_g = np.zeros((300, 500), dtype=np.uint8)
c_size_c = np.zeros((300, 500, 3), dtype=np.uint8)

NH = int(c_size_c.shape[0]/2)
NW = int(c_size_c.shape[1]/2)

def img_crop(ori, new):
    if len(ori.shape) == 2:
        for i in range(len(new)):
            for j in range(len(new[0])):
                new[i][j] = ori[i + H - NH][j + W - NW]

    elif len(ori.shape) == 3:
        for i in range(len(new)):
            for j in range(len(new[0])):
                for c in range(3):
                    new[i][j][c] = ori[i + H - NH][j + W - NW][c]
    return new

g = img_crop(iu_gray, c_size_g)
h = img_crop(iu, c_size_c)

cv2.imshow('ori', iu)
cv2.imshow('gray', iu_gray)
cv2.imshow('new_gray', g)
cv2.imshow('new_color', h)
cv2.waitKey()
cv2.destroyAllWindows()