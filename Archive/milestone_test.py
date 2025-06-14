import json
import os
import pandas as pd


class Config:
    def __init__(self, file_path=os.getcwd() + '\\milestone.json'):
        self.file_path = file_path
        self.config_data = self._read_config()

    def _read_config(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"config file '{self.file_path}' not found.")
            return {}

    def get_VFF_milestone1(self):
        return self.config_data.get('VFF').get('Delivery Assembly/directed parts')
    
    def get_VFF_milestone2(self):
        return self.config_data.get('VFF').get('ZP8 VFF Ramp up 1')
    
    def get_PVS_milestone1(self):
        return self.config_data.get('PVS').get('Delivery Assembly/directed parts')
    
    def get_PVS_milestone2(self):
        return self.config_data.get('PVS').get('ZP8 PVS Ramp up 1')
    
    def get_0Serie_milestone1(self):
        return self.config_data.get('0-Serie').get('Delivery Assembly/directed parts')
    
    def get_0Serie_milestone2(self):
        return self.config_data.get('0-Serie').get('ZP8 0-Serie Ramp up 1')
    
    def set_VFF_milestone1(self, str):
        self.config_data['VFF']['Delivery Assembly/directed parts'] = str
        try:
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump(self.config_data, file, indent=4)
        except Exception as e:
            print(f"error message: '{e}'")
            return {}
    
    def set_VFF_milestone2(self, str):
        self.config_data['VFF']['ZP8 VFF Ramp up 1'] = str
        try:
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump(self.config_data, file, indent=4)
        except Exception as e:
            print(f"error message: '{e}'")
            return {}
        
    def set_PVS_milestone1(self, str):
        self.config_data['PVS']['Delivery Assembly/directed parts'] = str
        try:
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump(self.config_data, file, indent=4)
        except Exception as e:
            print(f"error message: '{e}'")
            return {}
        
    def set_PVS_milestone2(self, str):
        self.config_data['PVS']['ZP8 PVS Ramp up 1'] = str
        try:
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump(self.config_data, file, indent=4)
        except Exception as e:
            print(f"error message: '{e}'")
            return {}
        
    def set_0Serie_milestone1(self, str):
        self.config_data['0-Serie']['Delivery Assembly/directed parts'] = str
        try:
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump(self.config_data, file, indent=4)
        except Exception as e:
            print(f"error message: '{e}'")
            return {}
        
    def set_0Serie_milestone2(self, str):
        self.config_data['0-Serie']['ZP8 0-Serie Ramp up 1'] = str
        try:
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump(self.config_data, file, indent=4)
        except Exception as e:
            print(f"error message: '{e}'")
            return {}
        

    
# config = Config()
# config.set_VFF_milestone1('23/24')
# config.set_VFF_milestone2('30/24')
# config.set_PVS_milestone1('36/24')
# config.set_PVS_milestone2('42/24')
# config.set_0Serie_milestone1('14/25')
# config.set_0Serie_milestone2('20/25')
# print(config.config_data.get('0-Serie'))
# print(config.get_VFF_milestone1(), config.get_VFF_milestone2(), config.get_PVS_milestone1(), config.get_PVS_milestone2(), config.get_0Serie_milestone1(), config.get_0Serie_milestone2())
