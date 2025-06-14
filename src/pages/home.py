import dash
from dash import html

dash.register_page(__name__, path='/')

layout = html.Div([
    html.Img(src='/assets/q6l.png', style={
        'width': '99vw',
        'height': '90vh',
        'borderRadius': '4px',
        'margin': '2px 0px'
    })
])