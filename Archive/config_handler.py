import json
import os
import pandas as pd


class Config:
    def __init__(self, file_path=os.getcwd() + '\\config.json'):
        self.file_path = file_path
        self.config_data = self._read_config()

    def _read_config(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"config file '{self.file_path}' not found.")
            return {}

    def get_input_paths(self):
        return self.config_data.get('Paths', [])

    def iterate_input_paths(self):
        input_paths = self.get_input_paths()
        for path in input_paths:
            yield path

    def get_df(self):
        result_df = pd.DataFrame()
        for input_path in self.iterate_input_paths():
            try:
                df = pd.read_excel(input_path, sheet_name=self.get_sheet_names(), usecols=self.get_column_names())
                result_df = pd.concat([result_df, df], ignore_index=True)
            except Exception as e:
                print(f"error reading excel file '{input_path}': {e}")
        return result_df

    def get_sheet_names(self):
        return self.config_data.get('Sheets')

    def iterate_sheet_names(self):
        sheet_names = self.get_sheet_names()
        for name in sheet_names:
            yield name

    def get_column_names(self):
        return self.config_data.get('Columns', [])

    def iterate_column_names(self):
        column_names = self.get_column_names()
        for name in column_names:
            yield name

    def get_color_column(self):
        return self.config_data.get('Color_Column')
