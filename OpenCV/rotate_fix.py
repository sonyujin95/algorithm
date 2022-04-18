import cv2
import numpy as np

# 종합 함수(컬러)

one = cv2.imread("image/iu_201908_.png")  # 로컬 파일명
# one_resize = cv2.resize(one,(256,256))

def rotate(one, d):  # d는 90의 배수(d가 1이면 90)

    # --------------------------------------------------------------------------------
    # FIXME 이미지가 정사각형이 아닐경우에 잘려서 회전될 가능성있음
    W = one.shape[0]
    H = one.shape[1]
    # ret = [[0] * N for _ in range(N)]  # 변형할 행렬
    ret = [[0] * W for _ in range(H)]  # 밑에 중첩 for문도 Width,Height에따라 수정필요
    # --------------------------------------------------------------------------------

    # --------------------------------------------------------------------------------
    # FIXME Color와 Gray따로 함수 분리할 필요없음
    loop_num = 0
    if len(one.shape)==3:
        loop_num = 3
    elif len(one.shape)==2:
        loop_num = 1
    # --------------------------------------------------------------------------------

    if d % 4 == 1:  # 90도
        for c in range(loop_num):
            for row in range(W):
                for col in range(H):
                    ret[col][W - 1 - row] = one[row][col]

    elif d % 4 == 2:  # 180도
        ret = [[0] * H for _ in range(W)]
        for c in range(loop_num):
            for row in range(W):
                for col in range(H):
                    ret[W - 1 - row][H - 1 - col] = one[row][col]

    elif d % 4 == 3:  # 270도
        for c in range(loop_num):
            for row in range(W):
                for col in range(H):
                    ret[H - 1 - col][row] = one[row][col]

    else:  # 0도 or 360도
        for c in range(loop_num):
            for row in range(W):
                for col in range(H):
                    ret[row][col] = one[row][col]

    return ret

# 90도
t_one_90 = np.array(rotate(one, 1))
t_one_180 = np.array(rotate(one, 2))
t_one_270 = np.array(rotate(one, 3))

cv2.imshow("original",one)
cv2.imshow('90rotation', t_one_90)
cv2.imshow('180rotation', t_one_180)
cv2.imshow('270rotation', t_one_270)
cv2.waitKey()
cv2.destroyAllWindows()

gray_one = cv2.cvtColor(one, cv2.COLOR_BGR2GRAY)

gray_one_90 = np.array(rotate(gray_one, 1))
gray_one_180 = np.array(rotate(gray_one, 2))
gray_one_270 = np.array(rotate(gray_one, 3))

cv2.imshow("gray_ori",gray_one)
cv2.imshow('gray_one_90', gray_one_90)
cv2.imshow('gray_one_180', gray_one_180)
cv2.imshow('gray_one_270', gray_one_270)

cv2.waitKey()
cv2.destroyAllWindows()