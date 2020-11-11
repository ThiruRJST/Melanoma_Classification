import os
import cv2
from tqdm import tqdm
from Preprocessing_Utils.Serializer import  Serialize_Write


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


def shade_of_gray_cc(img, power=6, gamma=2.2):
    """
    img (numpy array): the original image with format of (h, w, c)
    power (int): the degree of norm, 6 is used in reference paper
    gamma (float): the value of gamma correction, 2.2 is used in reference paper

    """
    img_dtype = img.dtype

    if gamma is not None:
        img = img.astype('uint8')
        look_up_table = np.ones((256, 1), dtype='uint8') * 0
        for i in range(256):
            look_up_table[i][0] = 255 * pow(i / 255, 1 / gamma)
        img = cv2.LUT(img, look_up_table)

    img = img.astype('float32')
    img_power = np.power(img, power)
    rgb_vec = np.power(np.mean(img_power, (0, 1)), 1 / power)
    rgb_norm = np.sqrt(np.sum(np.power(rgb_vec, 2.0)))
    rgb_vec = rgb_vec / rgb_norm
    rgb_vec = 1 / (rgb_vec * np.sqrt(3))
    img = np.multiply(img, rgb_vec)

    # Andrew Anikin suggestion
    img = np.clip(img, a_min=0, a_max=255)

    return img.astype(img_dtype)


def removal_contractor(paths, des_path, Subset, color_const=False):
    if des_path == None:
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
                if color_const is not False:
                    cleaned_img = shade_of_gray_cc(img=cleaned_img, gamma=2.2)
                cv2.imwrite(os.path.join(des_path, img_name), cleaned_img)
                paths.remove(p)
                Serialize_Write("/home/thirumalaikumar/FinalYearProject/Train_Cleaned", paths)


        else:
            os.makedirs(des_path)
            # assert len(paths) == len(paths) - len(paths_files_preprocessed)
            for i in tqdm(range(len(paths))):
                p = paths[i]
                img_name = p.split("/")[7]
                img = cv2.imread(p)
                img = cv2.resize(img, (512, 512))
                cleaned_img = hair_remove(img)
                if color_const is not False:
                    cleaned_img = shade_of_gray_cc(cleaned_img, gamma=2.2)
                cv2.imwrite(os.path.join(des_path, img_name), cleaned_img)
                paths.remove(p)
                Serialize_Write("/home/thirumalaikumar/FinalYearProject/Train_Cleaned", paths)
