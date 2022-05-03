from PIL import Image
def image_crop(image, save_path):

    img = Image.open("openCV/image/KakaoTalk_20220328_134200684.jpg")
    (img_h, img_w) = img.size
    print(img.size)

    # crop 할 사이즈 : grid_w, grid_h
    grid_w = 144
    grid_h = 144
    range_w = (int)(img_w/grid_w)
    range_h = (int)(img_h/grid_h)
    print(range_w, range_h)

    i = 0

    for w in range(range_w):
        for h in range(range_h):
            bbox = (h*grid_h, w*grid_w, (h+1)*(grid_h), (w+1)*(grid_w))
            print(bbox)
            # 가로 세로 시작, 가로 세로 끝
            crop_img = img.crop(bbox)

            fname = "{}.jpg".format("{0:05d}".format(i))
            savename = save_path + fname
            crop_img.save(savename)
            print('save file' + savename + '....')
            i += 1

if __name__ == '__main__':
    image_crop('crop', 'C:/Users/DeepCulus/Desktop/coding/openCV/image/test/')