import plotly.express as px
import dash
import plotly.graph_objects as go
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import re
from getlyric import pull_lyric

# https://www.metrolyrics.com/thinking-about-you-lyrics-frank-ocean.html
app = dash.Dash(__name__)
app.layout = html.Div(style={'border':'double','height':'100vh','backgroundColor':'#111111'},children=[
    dcc.Input(id='artist-name', value='Frank Ocean', type='text'),
    dcc.Input(id='artist-song', value='Self Control', type='text'),
    html.Div(
    dcc.Graph(id="graph", style={"width": "40vw","height": "40vw",'margin':'auto'})),
    html.Div(
    dcc.RadioItems(id='stopword-choice',
    options=[
        {'label': 'Ignore Stopwords', 'value': 1 },
        {'label': 'ShowAll', 'value': 0},
    ],
    value=1
),style={'color':'white','align':'center','width':'40vw','margin':'auto','padding-top': '50px'})
])

@app.callback(
    Output('graph', 'figure'),
    [Input(component_id='artist-name', component_property='value'),
     Input(component_id='artist-song', component_property='value'),
     Input(component_id='stopword-choice', component_property='value')]
)

def update_graph(artist_name,artist_song,stopword_choice):
    url=f"https://www.metrolyrics.com/{artist_song.lower().replace(' ','-')}-lyrics-{artist_name.lower().replace(' ','-')}.html"
    df = pull_lyric(url,stopword_choice)
    fig=go.Figure(layout=go.Layout(
        title=f"{artist_song}",
        template='plotly_dark',
        width=800,
        height=800))
    fig.add_trace(
    go.Scattergl(
            x=df['x'],
            y=df['y'],
            text=df['words'],
            mode='markers',
            marker={'color':df['freq']},

    ))
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
