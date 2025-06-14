import pandas as pd
import dash
from dash import dcc, html, dash_table
import os
import glob
from excel_reader import Excel_Reader
from milestone_test import Config
from datetime import datetime, timedelta

app = dash.Dash(__name__)

tevon_excel_path = r"C:\Users\eqhw2il\OneDrive - 奥迪一汽新能源汽车有限公司\桌面\项目相关\Aydin purchasing requirement\ProMon 240327.xlsx"
part_description_path = r"C:\Users\eqhw2il\OneDrive - 奥迪一汽新能源汽车有限公司\桌面\项目相关\Aydin purchasing requirement\Part Overview for Dashboard.xlsx"
file_path_start = r"C:\Users\eqhw2il\OneDrive - 奥迪一汽新能源汽车有限公司\Shared Documents - NEV Co. QPNi\A6L e-tron (AU511_4CE_BL)"
tevon_df = pd.read_excel(tevon_excel_path, sheet_name="ProMon", skiprows=6)
part_description_df = pd.read_excel(part_description_path, sheet_name="Q6L e-tron")

df = pd.DataFrame(columns=[
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


df['Part Description'] = part_description_df['Part Description']
df['Part Number'] = part_description_df["Part Number\n(optional)"]
df['Responsible'] = part_description_df['Responsible']
df['Supplier'] = part_description_df['Supplier']
df['Subgroup'] = part_description_df['Subgroup Filter']

# df['Status']
excel_reader = Excel_Reader()
for i in range(len(df)):
    file_path = file_path_start + f'\\{part_description_df.iloc[i, 1]}'
    if os.path.isdir(file_path):
        level2_files = glob.glob(file_path + '\\*')
        for level3_file in level2_files:
            if os.path.isdir(level3_file):
                h = os.path.split(level3_file)
                if "02_Maturity Level" in h[1]:
                    level3_files = glob.glob(level3_file + '\\*.xlsx')
                    if(len(level3_files) != 0):
                        level3_file = level3_files[0]
                        df.iloc[i, 2] = excel_reader.ml2_7_status_per_file(level3_file)
                    else: 
                        df.iloc[i, 2] = 'no excel'
    else:
        df.iloc[i, 2] = 'no folder'

# df['TEVON Status']
def get_date_from_week(year, week_number):
    first_monday = datetime(year, 1, 1) + timedelta(days=(0 - datetime(year, 1, 1).weekday() + 7) % 7)
    week_date = first_monday + timedelta(weeks=week_number - 1)
    return week_date

def get_date_from_week_string(week_string):
    year, week_number = map(int, week_string.split('/'))
    return get_date_from_week(year, week_number)
config = Config()
VFF_ml_1 = config.get_VFF_milestone1()
VFF_ml_2 = config.get_VFF_milestone2()
PVS_ml_1 = config.get_PVS_milestone1()
PVS_ml_2 = config.get_PVS_milestone2()
Serie0_ml_1 = config.get_0Serie_milestone1()
Serie0_ml_2 = config.get_0Serie_milestone2()
for i in range(len(df)):
    for j in range(len(tevon_df)):
        if tevon_df.iloc[j, 4] == df.iloc[i, 1]:
            df.iloc[i, 5] = tevon_df.iloc[j, 3]
            df.iloc[i, 6] = tevon_df.iloc[j, 29]
            df.iloc[i, 7] = tevon_df.iloc[j, 34]
            df.iloc[i, 8] = tevon_df.iloc[j, 36]
            if not isinstance(tevon_df.iloc[j, 29], str) or not isinstance(tevon_df.iloc[j, 34], str) or not isinstance(tevon_df.iloc[j, 36], str):
                continue
            elif get_date_from_week_string(tevon_df.iloc[j, 29]) <= get_date_from_week_string(VFF_ml_1) and \
            get_date_from_week_string(tevon_df.iloc[j, 34]) <= get_date_from_week_string(PVS_ml_1) and \
            get_date_from_week_string(tevon_df.iloc[j, 36]) <= get_date_from_week_string(Serie0_ml_1):
                df.iloc[i, 4] = 'green'
            elif get_date_from_week_string(tevon_df.iloc[j, 29]) > get_date_from_week_string(VFF_ml_2) and \
            get_date_from_week_string(tevon_df.iloc[j, 34]) > get_date_from_week_string(PVS_ml_2) and \
            get_date_from_week_string(tevon_df.iloc[j, 36]) > get_date_from_week_string(Serie0_ml_2):
                df.iloc[i, 4] = 'red'
            else:
                df.iloc[i, 4] = 'yellow'
            break



table = dash_table.DataTable(id='detail-table', 
                             style_data={
                                'whiteSpace': 'normal',
                                'height': 'auto',
                            },
                            style_header={
                                'whiteSpace': 'normal',
                                'height': 'auto',
                            },
                            columns=[{'name': col, 'id': col, 'hideable': True, 'editable': col == 'Actions'} for col in df.columns],
                            style_cell_conditional=[
                                {'if': {'column_id': 'Actions'},
                                'width': '35%'},
                                {'if': {'column_id': 'Part Description'},
                                'width': '10%'},
                                {'if': {'column_id': 'Part Number'},
                                'width': '7%'},
                                {'if': {'column_id': 'Status'},
                                'width': '5%'},
                                {'if': {'column_id': 'TEVON Status'},
                                'width': '5%'},
                                {'if': {'column_id': 'CORE'},
                                'width': '4%'},
                                {'if': {'column_id': 'VFF'},
                                'width': '3%'},
                                {'if': {'column_id': 'PVS'},
                                'width': '3%'},
                                {'if': {'column_id': '0-Serie'},
                                'width': '5%'},
                                {'if': {'column_id': 'Responsible'},
                                'width': '7%'},
                                {'if': {'column_id': 'Subgroup'},
                                'width': '6%'},
                                {'if': {'column_id': 'Supplier'},
                                'width': '10%'},
                            ],
                            style_data_conditional=[
                                {
                                    'if': {
                                        'column_id': 'Status',
                                        'filter_query': '{Status} = "yellow"'
                                    },
                                    'backgroundColor': 'yellow'
                                },
                                {
                                    'if': {
                                        'column_id': 'Status',
                                        'filter_query': '{Status} = "red"'
                                    },
                                    'backgroundColor': 'red'
                                },
                                {
                                    'if': {
                                        'column_id': 'Status',
                                        'filter_query': '{Status} = "green"'
                                    },
                                    'backgroundColor': 'green'
                                },
                                {
                                    'if': {
                                        'column_id': 'TEVON Status',
                                        'filter_query': '{TEVON Status} = "yellow"'
                                    },
                                    'backgroundColor': 'yellow'
                                },
                                {
                                    'if': {
                                        'column_id': 'TEVON Status',
                                        'filter_query': '{TEVON Status} = "green"'
                                    },
                                    'backgroundColor': 'green'
                                },
                                {
                                    'if': {
                                        'column_id': 'TEVON Status',
                                        'filter_query': '{TEVON Status} = "red"'
                                    },
                                    'backgroundColor': 'red'
                                }
                            ],
                            data=df.to_dict('records'),
                            export_format='xlsx',
                            export_headers='display',
                            merge_duplicate_headers=True,
                            page_action="native",
                            page_current= 0,
                            page_size= 10,
                            fixed_rows={'headers': True},
                            filter_action='native')

app.layout = html.Div(table)

if __name__ == '__main__':
    app.run_server(debug=True)