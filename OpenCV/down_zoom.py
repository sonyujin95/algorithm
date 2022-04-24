import cv2
import numpy as np

def image_resize(original_array, new_array):
    if len(original_array.shape) == 2:  # 원본파일이 흑백이라면
        for i in range(len(new_array)):  # 축소될 영행렬에서
            for j in range(len(new_array[0])):  # 원본의 행렬의 요소의 주변값을 축소될 영행렬 요소에 추가한다.
                new_array[i][j] = original_array[i * 2][j * 2]
                new_array[i][j] = original_array[i * 2 + 1][j * 2]
                new_array[i][j] = original_array[i * 2][j * 2 + 1]
                new_array[i][j] = original_array[i * 2 + 1][j * 2 + 1]

    elif len(original_array.shape) == 3:  # 원본파일이 컬러라면
        for i in range(len(new_array)):  # 축소될 영행렬에서
            for j in range(len(new_array[0])):  # 원본의 행렬의 요소의 주변값을 축소될 영행렬 요소에 추가한다.
                for c in range(3):  # 채널 반복
                    new_array[i][j][c] = original_array[i * 2][j * 2][c]
                    new_array[i][j][c] = original_array[i * 2 + 1][j * 2][c]
                    new_array[i][j][c] = original_array[i * 2][j * 2 + 1][c]
                    new_array[i][j][c] = original_array[i * 2 + 1][j * 2 + 1][c]
    return new_array

# 흑백 이미지
gray_image = cv2.imread("image/KakaoTalk_20220328_134200684.jpg")
gray_image = cv2.cvtColor(gray_image, cv2.COLOR_RGB2GRAY)
gray_image = cv2.resize(gray_image, dsize=(256, 256))  # 사이즈 재정의

# 컬러 이미지
color_image = cv2.imread("image/KakaoTalk_20220328_134200684.jpg")
color_image = cv2.resize(color_image, dsize=(256, 256))  # 사이즈 재정의

new_g_array = np.zeros((128, 128), dtype=np.uint8)  # 흑백의 영행렬 생성
new_c_array = np.zeros((128, 128, 3), dtype=np.uint8)  # 컬러의 영행렬 생성

# 축소 적용
resize_gray_image = image_resize(gray_image, new_g_array)
resize_color_image = image_resize(color_image, new_c_array)

# 이미지 출력
cv2.imshow("g", gray_image)
cv2.imshow("c", color_image)
cv2.imshow("g_r", resize_gray_image)
cv2.imshow("c_r", resize_color_image)
cv2.waitKey(0)
cv2.destroyAllWindows()