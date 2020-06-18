import plotly.express as px
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import re
from songsim import *
import pandas as pd


app = dash.Dash(
    __name__, external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"]
)


df=text_to_dataframe('song.txt')
app.layout = html.Div(
    [
        dcc.Graph(id="graph", style={"width": "40vw","height": "40vw",'border':'double','margin':'auto'},
        figure = px.scatter(df, x="x", y="y",hover_name="words",color='freq',template='plotly_dark'))
    ]
)


app.run_server(debug=True)