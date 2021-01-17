from Preprocess import removal_iterator
import glob
import argparse

def pre(img_paths,destination,r):
    files = glob.glob(img_paths)
    removal_iterator(files,des_path=destination,resume=r)


if __name__ == 'main':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--img_path',metavar='img_paths',type=str,help='Paths to Images')
    parser.add_argument('--des_path',metavar='des_paths',type=str,help='paths to store the preprocessed images')
    parser.add_argument('--resume',metavar=resum,type=bool)

    args = parser.parse_args()
    img_paths = args.img_path
    destination = args.des_path
    resume = args.resume

    print(img_paths,destination,resume)

    pre(img_paths,destination,resume)

