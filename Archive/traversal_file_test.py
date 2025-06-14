import glob
import os

file_path_start = r"C:\Users\eqhw2il\OneDrive - 奥迪一汽新能源汽车有限公司\Shared Documents - NEV Co. QPNi\A6L e-tron (AU511_4CE_BL)"


def traversalDir_SecDir(path):
    lists = []
    if os.path.exists(path):
        level1_files = glob.glob(path + '\\*')
        # print(level1_files)
        for level2_file in level1_files:
            # level2_list = []
            if os.path.isdir(level2_file):
                level2_files = glob.glob(level2_file + '\\*')
                # print("-----")
                # print(level2_files)
                for level3_file in level2_files:
                    # level3_list = []
                    if os.path.isdir(level3_file):
                        h = os.path.split(level3_file)
                        # print("*****")
                        # print(h[1])
                        if "02_Maturity Level" in h[1]:
                            # level3_files = glob.glob(level3_file + '\\*')
                            level3_files = glob.glob(level3_file + '\\*.xlsx')
                            # print("++++++")
                            # print(level3_files)
                            for level4_file in level3_files:
                                lists.append(level4_file)
    return lists
