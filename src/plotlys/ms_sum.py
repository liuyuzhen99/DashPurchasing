import plotly.graph_objs as go
from dash import dcc

# green_VFF, yellow_VFF, red_VFF, green_PVS, yellow_PVS, red_PVS, green_0Serie, yellow_0Serie, red_0Serie = get_milestone_summary()
class Ms_Painter:
    def __init__(self) -> None:
        pass

    def create_milestone_sum(self,green,yellow,red, milestone1, milestone2, type):
        # colors = ['green', 'yellow', 'red']
        # figure1 = go.Figure(go.Pie(labels=['Green', 'Yellow', 'Red'], values=[green, yellow, red], hole=0.3))
        # figure1.update_traces(
        # hoverinfo='label+percent',
        # textinfo='value',
        # showlegend=False,
        # domain=dict(x=[0, 1], y=[0, 1]),
        # marker=dict(colors=colors))
        # figure1.update_layout(title=f'{type}')
        # return dcc.Graph(figure=figure1)
        data = [
            go.Bar(
                x=['G', 'Y', 'R'],
                y=[green,yellow,red],
                marker=dict(color=['green', 'yellow', 'red'])
            )
        ]
        fig = go.Figure(data=data)
        fig.update_layout(title=f'{type} - {milestone1} - {milestone2}')
        return dcc.Graph(figure=fig)