import pandas as pd
from .excel_reader import Excel_Reader
from .ms_reader import Ms_Reader
import os
import glob
from datetime import datetime, timedelta

class Detail_df_Creator:
    # tevon_excel_path = r"C:\Users\eqhw2il\OneDrive - 奥迪一汽新能源汽车有限公司\桌面\项目相关\Aydin purchasing requirement\ProMon 240327.xlsx",
    # part_description_path = r"C:\Users\eqhw2il\OneDrive - 奥迪一汽新能源汽车有限公司\桌面\项目相关\Aydin purchasing requirement\Part Overview for Dashboard.xlsx",
    # file_path_start = r"C:\Users\eqhw2il\OneDrive - 奥迪一汽新能源汽车有限公司\Shared Documents - NEV Co. QPNi\A6L e-tron (AU511_4CE_BL)",
    def __init__(self, tevon_excel_path='', part_description_path='', file_path_start='', excel_reader=Excel_Reader(), ms_reader=Ms_Reader()) -> None:
        self.df = pd.DataFrame(columns=[
                    'Part Description', # done
                    'Part Number', # done
                    'Status', # done
                    'Actions',
                    'TEVON Status',
                    'CORE',
                    'VFF',
                    'PVS',
                    '0-Serie',
                    'Responsible', # done
                    'Supplier', # done
                    'Subgroup' # done
                ])
        # self.tevon_df = pd.read_excel(tevon_excel_path, sheet_name="ProMon", skiprows=6)
        # self.part_description_df = pd.read_excel(part_description_path, sheet_name="Q6L e-tron")
        self.part_description_df = pd.DataFrame()
        self.tevon_df = pd.DataFrame()
        self.file_path_start = file_path_start
        self.excel_reader = excel_reader
        self.ms_reader = ms_reader

    def set_1_part_description(self):
        self.df['Part Description'] = self.part_description_df['Part Description']

    def set_2_part_number(self):
        self.df['Part Number'] = self.part_description_df["Part Number\n(optional)"]

    def set_11_supplier(self):
        self.df['Supplier'] = self.part_description_df['Supplier']

    def set_12_subgroup(self):
        self.df['Subgroup'] = self.part_description_df['Subgroup Filter']

    def set_10_responsible(self):
        self.df['Responsible'] = self.part_description_df['Responsible']

    # def set_3_Status(self):
    #     for i in range(len(self.df)):
    #         file_path = self.file_path_start + f'\\{self.part_description_df.iloc[i, 1]}'
    #         if os.path.isdir(file_path):
    #             level2_files = glob.glob(file_path + '\\*')
    #             for level3_file in level2_files:
    #                 if os.path.isdir(level3_file):
    #                     h = os.path.split(level3_file)
    #                     if "02_Maturity Level" in h[1]:
    #                         level3_files = glob.glob(level3_file + '\\*.xlsx')
    #                         if(len(level3_files) != 0):
    #                             level3_file = level3_files[0]
    #                             self.df.iloc[i, 2] = self.excel_reader.ml2_7_status_per_file(level3_file)
    #                         else: 
    #                             self.df.iloc[i, 2] = 'no excel'
    #         else:
    #             self.df.iloc[i, 2] = 'no folder'
        
    def set_3_Status(self):
        for i in range(len(self.part_description_df)):
            file_path = self.file_path_start + f'\\{self.part_description_df.iloc[i, 1]}'
            if os.path.isdir(file_path):
                level2_files = glob.glob(file_path + '\\*')
                for level2_file in level2_files:
                    if os.path.isdir(level2_file):
                        h = os.path.split(level2_file)
                        if "02_Maturity Level" in h[1]:
                            level3_files = glob.glob(level2_file + '\\*.xlsx')
                            if(len(level3_files) != 0):
                                level3_file = level3_files[0]
                                self.df.iloc[i, 2] = self.excel_reader.ml2_7_status_per_file(level3_file)
                            else: 
                                self.df.iloc[i, 2] = 'no excel'
            else:
                self.df.iloc[i, 2] = 'no folder'
    
    def get_date_from_week(self, year, week_number):
        first_monday = datetime(year, 1, 1) + timedelta(days=(0 - datetime(year, 1, 1).weekday() + 7) % 7)
        week_date = first_monday + timedelta(weeks=week_number - 1)
        return week_date

    def get_date_from_week_string(self, week_string):
        year, week_number = map(int, week_string.split('/'))
        return self.get_date_from_week(year, week_number)

    def set_5_9_tevon(self):
        VFF_ml_1 = self.ms_reader.get_VFF_milestone1()
        VFF_ml_2 = self.ms_reader.get_VFF_milestone2()
        PVS_ml_1 = self.ms_reader.get_PVS_milestone1()
        PVS_ml_2 = self.ms_reader.get_PVS_milestone2()
        Serie0_ml_1 = self.ms_reader.get_0Serie_milestone1()
        Serie0_ml_2 = self.ms_reader.get_0Serie_milestone2()
        for i in range(len(self.df)):
            for j in range(len(self.tevon_df)):
                if self.tevon_df.iloc[j, 4] == self.df.iloc[i, 1]:
                    self.df.iloc[i, 5] = self.tevon_df.iloc[j, 3]
                    self.df.iloc[i, 6] = self.tevon_df.iloc[j, 29]
                    self.df.iloc[i, 7] = self.tevon_df.iloc[j, 34]
                    self.df.iloc[i, 8] = self.tevon_df.iloc[j, 36]
                    if not isinstance(self.tevon_df.iloc[j, 29], str) or not isinstance(self.tevon_df.iloc[j, 34], str) or not isinstance(self.tevon_df.iloc[j, 36], str):
                        continue
                    elif self.get_date_from_week_string(self.tevon_df.iloc[j, 29]) <= self.get_date_from_week_string(VFF_ml_1) and \
                    self.get_date_from_week_string(self.tevon_df.iloc[j, 34]) <= self.get_date_from_week_string(PVS_ml_1) and \
                    self.get_date_from_week_string(self.tevon_df.iloc[j, 36]) <= self.get_date_from_week_string(Serie0_ml_1):
                        self.df.iloc[i, 4] = 'green'
                    elif self.get_date_from_week_string(self.tevon_df.iloc[j, 29]) > self.get_date_from_week_string(VFF_ml_2) and \
                    self.get_date_from_week_string(self.tevon_df.iloc[j, 34]) > self.get_date_from_week_string(PVS_ml_2) and \
                    self.get_date_from_week_string(self.tevon_df.iloc[j, 36]) > self.get_date_from_week_string(Serie0_ml_2):
                        self.df.iloc[i, 4] = 'red'
                    else:
                        self.df.iloc[i, 4] = 'yellow'
                    break
        
    def set_df(self):
        self.set_1_part_description()
        self.set_2_part_number()
        self.set_3_Status()
        self.set_5_9_tevon()
        self.set_10_responsible()
        self.set_11_supplier()
        self.set_12_subgroup()