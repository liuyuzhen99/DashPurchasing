import dash
import time
import webbrowser
import threading
import sys
import signal
from dash import Dash, html, dcc
from pages.DashBoard import q6_painter

stop_event = threading.Event()

def open_browser():
    time.sleep(1)
    webbrowser.open_new('http://127.0.0.1:8050/')

def run_dash_server():
    app.run_server(debug=False)

def signal_handler(sig, frame):
    stop_event.set()
    sys.exit(0)


app = Dash(__name__, use_pages=True)

q6_painter.upload_filepath_painter.app = app
q6_painter.app = app

app.layout = html.Div([
    html.Div([
        html.Div(
            dcc.Link(f"{page['name']}", href=page["relative_path"])
        ) for page in dash.page_registry.values()
    ], style={
            'display': 'flex',
            'flexDirection': 'row', 
            'justifyContent': 'space-around',
            'color': '#007BFF',
            'textDecoration': 'none',
            'fontWeight': 'bold',
            'padding': '8px 16px',
            'border': '2px solid #007BFF',
            'borderRadius': '4px',
            'backgroundColor': 'transparent',
            'transition': 'color 0.3s, background-color 0.3s, border-color 0.3s',
        }),
    dash.page_container
])

q6_painter.model_callback()
q6_painter.filepath_callback()
q6_painter.upload_filepath_callback()

if __name__ == '__main__':
    # signal.signal(signal.SIGINT, signal_handler)
    # app_thread = threading.Thread(target=run_dash_server)
    # app_thread.daemon = True
    # app_thread.start()
    
    # open_browser()
    
    # app_thread.join()
    app.run_server(debug=True)