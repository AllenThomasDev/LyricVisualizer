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
    dcc.Graph(id="graph", style={"width": "40vw","height": "40vw",'margin':'auto'}),
])

@app.callback(
    Output('graph', 'figure'),
    [Input(component_id='artist-name', component_property='value'),
     Input(component_id='artist-song', component_property='value')]
)

def update_graph(artist_name,artist_song):
    url=f"https://www.metrolyrics.com/{artist_song.lower().replace(' ','-')}-lyrics-{artist_name.lower().replace(' ','-')}.html"
    df = pull_lyric(url)
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
