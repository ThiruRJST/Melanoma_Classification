import os
import cv2
from tqdm import tqdm


def hair_remove(image):
    # convert image to grayScale
    grayScale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    # kernel for morphologyEx
    kernel = cv2.getStructuringElement(1, (17, 17))

    # apply MORPH_BLACKHAT to grayScale image
    blackhat = cv2.morphologyEx(grayScale, cv2.MORPH_BLACKHAT, kernel)

    # apply thresholding to blackhat
    _, threshold = cv2.threshold(blackhat, 10, 255, cv2.THRESH_BINARY)

    # inpaint with original image and threshold image
    final_image = cv2.inpaint(image, threshold, 1, cv2.INPAINT_TELEA)

    return final_image


def removal_contractor(paths, des_path, Subset):
    if des_path is None:
        des_path = os.path.join(os.getcwd(), Subset)
    else:
        des_path = os.path.join(des_path, Subset)
        if os.path.exists(des_path):
            # assert len(paths) == len(paths) - len(paths_files_preprocessed)
            for i in tqdm(range(len(paths))):
                p = paths[i]
                img_name = p.split("/")[7]
                img = cv2.imread(p)
                img = cv2.resize(img, (512, 512))
                cleaned_img = hair_remove(img)
                cv2.imwrite(os.path.join(des_path, img_name), cleaned_img)


        else:
            os.makedirs(des_path)
            # assert len(paths) == len(paths) - len(paths_files_preprocessed)
            for i in tqdm(range(len(paths))):
                p = paths[i]
                img_name = p.split("/")[7]
                img = cv2.imread(p)
                img = cv2.resize(img, (512, 512))
                cleaned_img = hair_remove(img)
                cv2.imwrite(os.path.join(des_path, img_name), cleaned_img)
