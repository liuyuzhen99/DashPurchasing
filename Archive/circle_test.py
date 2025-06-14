import dash
import pandas as pd
from dash import dcc, html
import plotly.graph_objs as go
from dash import dash_table
import webbrowser
import threading
import time
from config_handler import Config
from cluster_bar_plot import create_ml_sum_cluster_barplot


def open_browser():
    time.sleep(1)
    webbrowser.open_new('http://127.0.0.1:8050/')


def run_dash_server():
    app.run_server(debug=False)


app = dash.Dash(__name__)


def create_pie_graph1():
    figure1 = go.Figure(go.Pie(labels=['A', 'B', 'C'], values=[40, 30, 30], hole=0.3))
    return dcc.Graph(figure=figure1)


def create_pie_graph2():
    figure2 = go.Figure(go.Pie(labels=['X', 'Y', 'Z'], values=[50, 25, 25], hole=0.3))
    return dcc.Graph(figure=figure2)


def create_pie_graph3():
    figure3 = go.Figure(go.Pie(labels=['Alpha', 'Beta', 'Gamma'], values=[20, 50, 30], hole=0.3))
    return dcc.Graph(figure=figure3)


def create_stacked_bar_chart4():
    x_data_ = ['Category A', 'Category B', 'Category C']
    y_data_1 = [20, 30, 25]
    y_data_2 = [10, 25, 20]
    y_data_3 = [15, 20, 10]
    return dcc.Graph(
        figure={
            'data': [
                {'x': x_data_, 'y': y_data_1, 'type': 'bar', 'name': 'Data_1'},
                {'x': x_data_, 'y': y_data_2, 'type': 'bar', 'name': 'Data_2'},
                {'x': x_data_, 'y': y_data_3, 'type': 'bar', 'name': 'Data_3'}
            ],
            'layout': {
                'title': 'Stacked Bar Chart'
            }
        }
    )


def create_cluster_bar_chart5():
    categories = ['Category A', 'Category B', 'Category C']
    data1 = [20, 30, 25]
    data2 = [15, 25, 20]
    trace1 = go.Bar(x=categories, y=data1, name='Data 1')
    trace2 = go.Bar(x=categories, y=data2, name='Data 2')
    fig = go.Figure(data=[trace1, trace2])
    fig.update_layout(barmode='relative', title='Clustered Bar Chart')
    return dcc.Graph(figure=fig)


def create_bar_chart6():
    x_data = ['Category A', 'Category B', 'Category C']
    y_data = [50, 40, 40]
    return dcc.Graph(
        figure={
            'data': [
                {'x': x_data, 'y': y_data, 'type': 'bar', 'name': 'Bars'}
            ],
            'layout': {
                'title': 'Simple Bar Chart'
            }
        }
    )


def create_table():
    config = Config()
    df = config.get_df()
    return html.Div([
        dash_table.DataTable(
            id='my-table',
            columns=[{'name': col, 'id': col} for col in df.columns],
            data=df.to_dict('records')
        )
    ])


def create_table1():
    config = Config()
    df = config.get_df()
    return html.Table(
        [html.Tr([html.Th(col, style={
            'position': 'sticky',
            'top': '0',
            'height': '10px',
            'background-color': 'white',
            'z-index': '1',
            'border': '1px solid #000000'
        }) for col in df.columns])] +
        [
            html.Tr(
                [
                    html.Td(style=generate_circle(row[config.get_color_column()]))
                    if col == 'Color' else
                    html.Td(df.iloc[i][col], style={'width': '300px', 'height': '80px', 'text-align': 'center',
                                                    'border': '1px solid #000000'})
                    for col in df.columns
                ]
            ) for i, row in df.iterrows()
        ]
    )


def generate_circle(color):
    return {
        'width': '250px',
        'background-color': color,
        'border-left': '1px solid #000000',
        'border-top': '1px solid #000000'
    }


def create_layout():
    return html.Div([
        html.Div([
            html.Div(create_pie_graph1(), style={
                'width': '16%',
                'display': 'inline-block'
            }),
            html.Div(create_pie_graph2(), style={
                'width': '16%',
                'display': 'inline-block'
            }),
            html.Div(create_pie_graph3(), style={
                'width': '16%',
                'display': 'inline-block'
            }),
            html.Div(create_stacked_bar_chart4(), style={
                'width': '16%',
                'display': 'inline-block'
            }),
            html.Div(create_ml_sum_cluster_barplot(), style={
                'width': '16%',
                'display': 'inline-block'
            }),
            html.Div(create_bar_chart6(), style={
                'width': '16%',
                'display': 'inline-block'
            }),
        ]),
        html.Div([
            html.Div([
                html.Div(create_table(),
                         style={'width': '600px', 'height': '150px', 'overflowX': 'auto', 'text-align': 'center'}),
                html.Br(),
                html.Div(create_table1(), style={'width': '1200px', 'height': '330px', 'overflowX': 'auto',
                                                 'border': '1px solid #000000', 'boarder-collapse': 'collapse',
                                                 'text-align': 'center'}),
            ], style={
                'width': '70%',
                'display': 'inline-block'
            })
        ])
    ])


app.layout = create_layout()

if __name__ == '__main__':
    # app_thread = threading.Thread(target=run_dash_server)
    # app_thread.daemon = True
    # app_thread.start()
    #
    # open_browser()
    #
    # app_thread.join()
    app.run_server(debug=True)
