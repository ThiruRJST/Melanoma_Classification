from Preprocess import removal_iterator
import glob
import argparse

files = glob.glob("/home/lustbeast/Datasets/2019/mel/*.jpg")
removal_iterator(files,des_path='/home/lustbeast/Datasets/Train_Cleaned/images',resume=False)

