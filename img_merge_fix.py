import cv2
import numpy as np

na = cv2.imread("KakaoTalk_20220328_134200684.jpg")
# na = cv2.cvtColor(na, cv2.COLOR_BGR2GRAY)  # 흑백으로 할 시 활성화
nb = cv2.imread("KakaoTalk_20220328_134200807.jpg")
# nb = cv2.cvtColor(nb, cv2.COLOR_BGR2GRAY)  # 흑백으로 할 시 활성화

# 흑백일 때와 컬러일 때 구분하기 위해
loop_num = 0
if len(na.shape) == 3:
    loop_num = 3

elif len(na.shape) == 2:
    loop_num = 1

# 변형할 행렬
alpha = na.copy()

# 이미지의 행렬 길이
W = na.shape[0]
H = na.shape[1]

def sum_1(alpha,image1,image2,weight):
    for c in range(loop_num):
        for row in range(W):
            for col in range(H):
                alpha[row][col] = image1[row][col] * weight + image2[row][col] * (1 - weight)
                if (alpha[row][col] > 255).any():
                    alpha[row][col] = 255
        return alpha

sum_t = np.array(sum_1(alpha,na,nb,0.5))

cv2.imshow('sum', sum_t)
cv2.waitKey()
cv2.destroyAllWindows()