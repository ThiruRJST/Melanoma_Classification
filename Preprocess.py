from Preprocessing_Utils.image_name_parser import img_name_parser
from Preprocessing_Utils.resumer import checker
from Preprocessing_Utils.remover import removal_contractor
import warnings


def removal_iterator(paths, des_path=None, Subset = "Train_Cleaned", resume=False):
    if resume is True:
        print("Deleting Preprocessed File paths >>>>> It may take few minutes")
        paths = checker(img_name_parser(), paths)
        removal_contractor(paths, des_path, Subset,color_const=True)
    else:
        warnings.warn(
            message="This is a normal run and will start from the very first, If you have preprocessed some files "
                    "already Please turn resume=True")
        removal_contractor(paths, des_path, Subset,color_const=True)
