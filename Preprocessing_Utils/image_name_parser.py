import glob
import os


def img_name_parser(path="/home/thirumalaikumar/FinalYearProject/Train_Cleaned"):
    assert path is not None
    image_names = []
    files = glob.glob(os.path.join(path, "*.jpg"))
    for i in range(len(files)):
        image_names.append(files[i].split("/")[5])
    return image_names
