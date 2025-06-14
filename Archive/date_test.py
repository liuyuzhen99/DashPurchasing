import datetime
import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output, State
import pandas as pd
from milestone_test import Config
from cluster_bar_plot import create_ml_sum_cluster_barplot, create_VFF_milestone_sum, create_PVS_milestone_sum, create_0Serie_milestone_sum
from tevon_test import get_milestone_summary

app = dash.Dash(__name__)

config = Config()

data = pd.DataFrame({
    'Delivery Assembly/directed parts': [config.get_VFF_milestone1(), config.get_PVS_milestone1(), config.get_0Serie_milestone1()],
    'ZP8 Ramp up 1': [config.get_VFF_milestone2(), config.get_PVS_milestone2(), config.get_0Serie_milestone2()]
},
index=['VFF', 'PVS', '0-Serie'])

data_dict = data.to_dict('index') 
for key, value in data_dict.items(): value[' '] = key

# print(data_dict.values)

table = dash_table.DataTable(id='editable-table', columns=[{'name': ' ', 'id': ' ', 'editable': False}] +
                                                           [{'name': col, 'id': col} for col in data.columns], 
                                                           data=[value for value in data_dict.values()], 
                                                           editable=False, 
                                                           merge_duplicate_headers=True)

edit_button  = html.Button('编辑', id='edit-button', n_clicks=0)
confrim_button = html.Button('确认', id='confirm-button', n_clicks=0, style={'display': 'none'})
green_VFF, yellow_VFF, red_VFF, green_PVS, yellow_PVS, red_PVS, green_0Serie, yellow_0Serie, red_0Serie = get_milestone_summary()
# print(green_VFF, yellow_VFF, red_VFF, green_PVS, yellow_PVS, red_PVS, green_0Serie, yellow_0Serie, red_0Serie)
app.layout = html.Div([
    html.Div(create_VFF_milestone_sum(green_VFF, yellow_VFF, red_VFF), style={'width': '15%'}),
    html.Div(create_PVS_milestone_sum(green_PVS, yellow_PVS, red_PVS), style={'width': '15%'}),
    html.Div(create_0Serie_milestone_sum(green_0Serie, yellow_0Serie, red_0Serie), style={'width': '15%'}),
    html.Div(create_ml_sum_cluster_barplot(), style={'width': '25%'}),
    html.Div([
        html.Div([edit_button, confrim_button]),
        table
], style={'width': '25%', 'display': 'flex', 'justify-content': 'center', 'flex-direction': 'column'})
], style={'display': 'flex'})

@app.callback(
    [Output('editable-table', 'editable'),
     Output('edit-button', 'style'),
     Output('confirm-button', 'style')],
    [Input('edit-button', 'n_clicks'),
     Input('confirm-button', 'n_clicks')],
    [State('editable-table', 'editable')]
)
def toggle_editable_mode(edit_clicks, confirm_clicks, current_editable):
    ctx = dash.callback_context
    if not ctx.triggered:
        return False, {'display': 'inline-block'}, {'display': 'none'}
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    if button_id == 'edit-button':
        return True, {'display': 'none'}, {'display': 'inline-block'}
    elif button_id == 'confirm-button':
        return False, {'display': 'inline-block'}, {'display': 'none'}

@app.callback(
    Output('editable-table', 'data'),
    [Input('confirm-button', 'n_clicks')],
    [State('editable-table', 'data')]
)
def update_data(confirm_clicks, table_data):
    ctx = dash.callback_context
    if not ctx.triggered:
        return dash.no_update
    new_data = pd.DataFrame(table_data)
    # print(new_data)
    config.set_VFF_milestone1(new_data.loc[0, 'Delivery Assembly/directed parts'])
    config.set_VFF_milestone2(new_data.loc[0, 'ZP8 Ramp up 1'])
    config.set_PVS_milestone1(new_data.loc[1, 'Delivery Assembly/directed parts'])
    config.set_PVS_milestone2(new_data.loc[1, 'ZP8 Ramp up 1'])
    config.set_0Serie_milestone1(new_data.loc[2, 'Delivery Assembly/directed parts'])
    config.set_0Serie_milestone2(new_data.loc[2, 'ZP8 Ramp up 1'])
    return table_data


if __name__ == '__main__':
    app.run_server(debug=True)

# # current_date = datetime.datetime.now()

# # year, week_num, _ = current_date.isocalendar()

