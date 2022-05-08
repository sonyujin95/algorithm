import cv2
import os
import shutil


def crop_ovr(image_path,crop_size,ovr_size,main_path):
    image = cv2.imread(image_path)

    image_name = image_path.split('/')[-1].split('.')[0]
    save_path = main_path + "/" + "testimages" +"/"+ image_name
    if not os.path.exists(main_path + "/" + "testimages"):  # testimages 폴더가 없으면 만들어라
        os.mkdir(main_path + "/" + "testimages")
    if os.path.exists(save_path):
        shutil.rmtree(save_path)
    if not os.path.exists(save_path):  # testimages 폴더 하위 이미지 이름 폴더가 없으면 만들어라
        os.mkdir(save_path)
    image_extension = image_path.split('/')[-1].split('.')[1]

    crop_size = crop_size
    overlap_size = ovr_size

    counter = 0
    print(image.shape[1])  # 900 -> width
    print(image.shape[0])  # 506 -> height
    for i in range(image.shape[1]//crop_size + 1):  # 900//200 + 1 = 5
        for j in range(image.shape[0]//crop_size + 1):  # 506//200 + 1 = 3
            if i != image.shape[1]//crop_size:  # i가 4가 아닐 때 -> 가로 끝 지점 안왔을 때
                if j != image.shape[0]//crop_size:  # j가 2가 아니면 -> 세로도 끝 지점이 안왔다면
                    # crop_image = image[(j*150): 200 + (j*150), (i*150): 200 + (i*150)] -> 가로, 세로 150씩 이동
                    crop_image = image[(j)*(crop_size-overlap_size):crop_size + (j)*(crop_size-overlap_size), (i) * (crop_size-overlap_size):crop_size + (i) * (crop_size-overlap_size)]
                if j == image.shape[0]//crop_size:  # j가 2라면 -> 세로 끝 지점이라면
                    # crop_image = image[306:506, (i*150) : 200 + (i*150)] -> 가로 150만큼 이동
                    crop_image = image[image.shape[0]-crop_size:image.shape[0], (i) * (crop_size-overlap_size):crop_size + (i) * (crop_size-overlap_size)]
            elif i == image.shape[1]//crop_size:  # i가 4일 때 -> 가로 끝 지점 왔을 때
                if j != image.shape[0]//crop_size:  # j가 2가 아니면 -> 세로가 끝이 아니면
                    crop_image = image[(j)*(crop_size-overlap_size):crop_size + (j)*(crop_size-overlap_size), image.shape[1]-crop_size:image.shape[1]]  # crop_image = image[(j*150) : 200 + (j*150), 700:900] -> 세로를 150만큼 이동
                elif j == image.shape[0]//crop_size:  # j가 2라면 -> 세로 끝 지점 왔을 때
                    crop_image = image[image.shape[0]-crop_size:image.shape[0], image.shape[1]-crop_size:image.shape[1]]  # crop_image = image[306:506, 700:900] -> [세로시작점:끝점, 가로시작점:끝점] -> 가로,세로 끝

            crop_image = cv2.resize(crop_image,dsize=(1024,1024),interpolation=cv2.INTER_CUBIC)  # crop된 이미지 1024*1024 로 resize
            cv2.imwrite(save_path + "/" + image_name + "_" + str(counter)+"." + image_extension , crop_image)  # crop이미지 저장경로

            counter = counter + 1
# 이미지를 200*200 사이즈로 자르지만 이동하는 건 150씩 이동하므로 50씩 겹친다.


image_path = "iu_201908_.png"
index = "0"
crop_size = 200
ovr_size = 50
main_path = "./"

crop_ovr(image_path,crop_size,ovr_size,main_path)