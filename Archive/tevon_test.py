from datetime import datetime, timedelta
import pandas as pd 
from milestone_test import Config

def get_date_from_week(year, week_number):
    first_monday = datetime(year, 1, 1) + timedelta(days=(0 - datetime(year, 1, 1).weekday() + 7) % 7)
    week_date = first_monday + timedelta(weeks=week_number - 1)
    return week_date

def get_date_from_week_string(week_string):
    year, week_number = map(int, week_string.split('/'))
    return get_date_from_week(year, week_number)

def get_milestone_summary():
    file_path = r'C:\Users\eqhw2il\OneDrive - 奥迪一汽新能源汽车有限公司\桌面\项目相关\Aydin purchasing requirement\ProMon 240327 - 副本.xlsx'
    df = pd.read_excel(file_path, skiprows=6)
    green_VFF = 0
    yellow_VFF = 0
    red_VFF = 0
    green_PVS = 0
    yellow_PVS = 0
    red_PVS = 0
    green_0Serie = 0
    yellow_0Serie = 0
    red_0Serie = 0
    config = Config()
    for i in range(len(df)):
        if not isinstance(df.loc[i, 'series tooling date'], str):
            green_VFF += 1
        elif(get_date_from_week_string(df.loc[i, 'series tooling date']) <= get_date_from_week_string(config.get_VFF_milestone1())):
            green_VFF += 1
        elif(get_date_from_week_string(df.loc[i, 'series tooling date']) > get_date_from_week_string(config.get_VFF_milestone2())):
            red_VFF += 1
        else:
            yellow_VFF += 1
        if not isinstance(df.loc[i, 'Series Tooling Grade 3'], str):
            green_PVS += 1
        elif(get_date_from_week_string(df.loc[i, 'Series Tooling Grade 3']) <= get_date_from_week_string(config.get_VFF_milestone1())):
            green_PVS += 1
        elif(get_date_from_week_string(df.loc[i, 'Series Tooling Grade 3']) > get_date_from_week_string(config.get_VFF_milestone2())):
            red_PVS += 1
        else:
            yellow_PVS += 1
        if not isinstance(df.loc[i, 'series tool Grade1'], str):
            green_0Serie += 1
        elif(get_date_from_week_string(df.loc[i, 'series tool Grade1']) <= get_date_from_week_string(config.get_VFF_milestone1())):
            green_0Serie += 1
        elif(get_date_from_week_string(df.loc[i, 'series tool Grade1']) > get_date_from_week_string(config.get_VFF_milestone2())):
            red_0Serie += 1
        else:
            yellow_0Serie += 1
    return green_VFF, yellow_VFF, red_VFF, green_PVS, yellow_PVS, red_PVS, green_0Serie, yellow_0Serie, red_0Serie

# data = [
#     go.Bar(
#         x=['G', 'Y', 'R'],
#         y=[green_VFF,yellow_VFF,red_VFF],
#         marker=dict(color=['green', 'yellow', 'red'])
#     )
# ]

# layout = go.Layout(
#     title='Bar Chart Example',
#     xaxis=dict(title='X Axis'),
#     yaxis=dict(title='Y Axis'),
# )

# fig = go.Figure(data=data, layout=layout)


# app.layout = html.Div(
#     dcc.Graph(
#         id='example-graph',
#         figure=fig
#     )
# )

# if __name__ == '__main__':
#     app.run_server(debug=True)