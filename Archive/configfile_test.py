from config_handler import Config
import pandas as pd

config = Config()
# result_df = pd.DataFrame()
# for input_path in config.iterate_input_paths():
#     try:
#         df = pd.read_excel(input_path)
#         result_df = pd.concat([result_df, df], ignore_index=True)
#     except Exception as e:
#         print(f"error reading excel file '{input_path}': {e}")
#
# print(result_df)

print(config.get_input_paths())
print('----------------------')
print(config.get_column_names())
print('----------------------')
print(config.get_color_column())
print('----------------------')
print(config.get_sheet_names())
print('----------------------')
print(config.get_df())

