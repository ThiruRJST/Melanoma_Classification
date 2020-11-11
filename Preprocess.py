from Preprocessing_Utils.remover import removal_contractor
from Preprocessing_Utils.Serializer import Serialize_Read
import warnings


def removal_iterator(paths, des_path=None, Subset="Train_Cleaned", resume=False):
    if resume:
        if os.path.exists("/home/thirumalaikumar/FinalYearProject/Train_Cleaned/ckpt.pkl"):
            print("Found Checkpoint")
            print("Loading Checkpoint")
            dirs = os.path.join(des_path, Subset)
            paths = Serialize_Read(os.path.join(dirs, "ckpt.pkl"))
            removal_contractor(paths, des_path, Subset, color_const=True)

        else:
            print("Checkpoint Not Found")
    else:
        print("Normal Run....")
        removal_contractor(paths, des_path, Subset)
