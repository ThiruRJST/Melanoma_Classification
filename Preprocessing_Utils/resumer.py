from tqdm import tqdm


def checker(pre_files, org_paths):
    for x in tqdm(pre_files):
        for y in org_paths:
            if x == y.split("/")[7]:
                org_paths.remove(y)
    return org_paths
