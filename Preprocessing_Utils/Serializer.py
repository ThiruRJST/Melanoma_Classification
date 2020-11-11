import pickle


def Serialize_Write(des, lst, file_name="ckpt.pkl"):
    with open(os.path.join(des, file_name), "wb") as f:
        pickle.dump(lst, f)


def Serialize_Read(loc):
    with open(loc, "rb") as f1:
        paths = pickle.load(f1)
    return paths
