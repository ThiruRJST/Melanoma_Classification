from Preprocess import removal_iterator
import glob
files = glob.glob('/home/thirumalaikumar/FinalYearProject/Dataset/jpeg/train/*.jpg')
removal_iterator(files,des_path="/home/thirumalaikumar/FinalYearProject",resume=True)