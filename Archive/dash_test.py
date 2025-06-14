import webbrowser
import threading
import time
import dash
from dash import dcc
from dash import html


def open_browser():
    time.sleep(1)
    webbrowser.open_new('http://127.0.0.1:8050/')

def run_dash_server():
    app.run_server(debug=False)

app = dash.Dash(__name__)

def create_cluster_bar_chart5():
    categories = ['Category A', 'Category B', 'Category C']
    data1 = [20, 30, 25]
    data2 = [15, 25, 20]
    trace1 = go.Bar(x=categories, y=data1, name='Data 1')
    trace2 = go.Bar(x=categories, y=data2, name='Data 2')
    fig = go.Figure(data=[trace1, trace2])
    fig.update_layout(barmode='relative', title='Clustered Bar Chart')
    return dcc.Graph(figure=fig)

app.layout = html.Div(children=[
    html.H1(children='test仪表板'),

    html.Div(children='''
        test
    '''),

    dcc.Graph(
        id='test-graph',
        figure={
            'data': [
                {
                    'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'
                },
                {
                    'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'NYC'
                }
            ],
            'layout':{
                'title': 'test'
            }
        }
    )
])

if __name__ == '__main__':
    app_thread = threading.Thread(target=run_dash_server)
    app_thread.daemon = True
    app_thread.start()

    open_browser()

    app_thread.join()