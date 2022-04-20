import numpy as np
import cv2

def image_resize(original_array, new_array):
    if len(original_array.shape) == 2:  # 원본파일이 흑백이라면
        for i in range(len(original_array)):
            for j in range(len(original_array[0])):  # 요소의 주변도 같은 값으로 영행렬에 넣어준다.
                n = int(new_array.shape[0] / original_array.shape[0])
                for k in range(n):
                    for z in range(n):
                        new_array[i * n + z][j * n + k] = original_array[i][j]

    elif len(original_array.shape) == 3:  # 원본파일이 컬러라면
        for i in range(len(original_array)):
            for j in range(len(original_array[0])):
                for c in range(3):  # 요소의 주변도 같은값으로 영행렬에 넣어준다.
                    n = int(new_array.shape[0] / original_array.shape[0])
                    for k in range(n):
                        for z in range(n):
                            new_array[i * n + z][j * n + k][c] = original_array[i][j][c]
    return new_array


# 흑백 이미지
gray_image = cv2.imread("image/KakaoTalk_20220328_134200684.jpg")
gray_image = cv2.cvtColor(gray_image, cv2.COLOR_RGB2GRAY)
gray_image = cv2.resize(gray_image, dsize=(256, 256))  # 사이즈 재정의

# 컬러 이미지
color_image = cv2.imread("image/KakaoTalk_20220328_134200684.jpg")
color_image = cv2.resize(color_image, dsize=(256, 256))  # 사이즈 재정의

new_g_array = np.zeros((768, 768), dtype=np.uint8)  # 흑백의 영행렬 생성
new_c_array = np.zeros((768, 768, 3), dtype=np.uint8)  # 컬러의 영행렬 생성

# 확대
resize_gray_image = image_resize(gray_image, new_g_array)
resize_color_image = image_resize(color_image, new_c_array)

# 이미지 출력
cv2.imshow("g", gray_image)
cv2.imshow("c", color_image)
cv2.imshow("g_r", resize_gray_image)
cv2.imshow("c_r", resize_color_image)
cv2.waitKey(0)
cv2.destroyAllWindows()