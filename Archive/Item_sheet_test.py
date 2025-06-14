import dash
import time
import webbrowser
from dash import dcc, html, dash_table, callback_context
from milestone_test import Config
import pandas as pd
from dash.dependencies import Input, Output, State

# <table border="1">
#     <tr>
#         <th>姓名<th>
#         <th>年龄<th>
#     </tr>
#     <tr>
#         <td>张三<td>
#         <td>25<td>
#     </tr>
# </table>

def open_browser():
    time.sleep(1)
    webbrowser.open_new('http://127.0.0.1:8050/')
    
def run_dash_server():
    app.run_server(debug=False)

app = dash.Dash(__name__)

config = Config()

data = pd.DataFrame({
    'Category': ['VFF', 'PVS', '0-Serie'],
    'Delivery Assembly/directed parts': [config.get_VFF_milestone1(), config.get_PVS_milestone1(), config.get_0Serie_milestone1()],
    'ZP8 Ramp up 1': [config.get_VFF_milestone2(), config.get_PVS_milestone2(), config.get_0Serie_milestone2()]
})

# table = html.Table(
#     [html.Tr([
#         html.Th('Category'),
#         html.Th('Delivery Assembly/directed parts'),
#         html.Th('ZP8 Ramp up 1')
#     ])] +  [
#         html.Tr([
#             html.Td('张三'),
#             html.Td(25)
#         ])
#     ]
# )



app.layout = html.Div([
    html.Table([
        html.Tbody(
            [html.Tr([html.Th(col) for col in data.keys()] + [html.Th("Action")])] +
            [html.Tr([html.Td(data[col][i]) for col in data.keys()] + [html.Td(html.Button('edit', id=f'edit_button_{i}'))]) for i in range(len(data['ZP8 Ramp up 1']))]
        )]
    ),
    html.Div(id='output')
])

@app.callback(
    Output('output', 'children'),
    [Input({
        'type': 'edit-button',
        'index': 'all'
    }, 'n_clicks')],
    prevent_initial_call=True
)
def edit_row(edit_buttons):
    ctx = callback_context
    if not ctx.triggered:
        return ""
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        clicked_row_index = int(button_id.split('_')[-1])
        return dcc.Input(id=f'edit_input_{clicked_row_index}', type='text', value=data['ZP8 Ramp up 1'][clicked_row_index])



if __name__ == '__main__':
    # app_thread = threading.Thread(target=run_dash_server)
    # app_thread.daemon = True
    # app_thread.start()
    #
    # open_browser()
    #
    # app_thread.join()
    app.run_server(debug=True)