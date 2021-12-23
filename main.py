import os
import cv2


def img_encode(in_imgs, quality=5):
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
    encimg_list = []

    for img in in_imgs:
        result, encimg = cv2.imencode('.jpg', img, encode_param)
        if not result:
            print('could not encode image!')
            return None
        encimg_list.append(encimg)

    return encimg_list


def img_decode(in_imgs, ch):
    decimg_list = []

    for img in in_imgs:
        decimg_list.append(cv2.imdecode(img, ch))

    return decimg_list


def main(path):
    img_list = []
    img_path_list = os.listdir(path)
    for file_name in img_path_list:
        img_list.append(cv2.imread(path+file_name))
    encimg_list = img_encode(img_list, 50)
    decimg_list = img_decode(encimg_list, 3)


if __name__ == '__main__':
    main('image_list/')