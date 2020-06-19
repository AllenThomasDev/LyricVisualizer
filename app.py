import plotly.express as px
import dash
import plotly.graph_objects as go
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import re
from getlyric import pull_lyric

# https://www.metrolyrics.com/thinking-about-you-lyrics-frank-ocean.html
app = dash.Dash(__name__,    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ])
app.layout = html.Div(style={'border':'double','height':'90vh','width':'100vw','text-align':'center','backgroundColor':'#111111'},children=[
    html.Div(children=[
        html.Div(children=[
            dcc.Input(id='artist-name', value='Frank Ocean', type='text'),
            dcc.Input(id='artist-song', value='Self Control', type='text')],style={'text-align':'left'}),
        dcc.Graph(id="graph",responsive=True,style={'height':'100%','width':'100%'}),
        html.Div(
            dcc.RadioItems(id='stopword-choice',
                options=[
                        {'label': 'Ignore Stopwords', 'value': 1 },
                        {'label': 'ShowAll', 'value': 0},
                        ],
                value=1
                          ),style={'color':'white','text-align':'left','padding-up':'210px'})
    ],style={'width':'70vh','height':'70vh','text-align':'left', 'display': 'inline-block','border':'double'}),
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
        title=f"{artist_song.capitalize()}",
        template='plotly_dark',
        xaxis =  {                                     
                    'ticks':'',
                    'zeroline':False,
                    'showticklabels':False,
                    'showline':False,
                    'showgrid':True
                  },
        yaxis = {                              
                'ticks':'',
                'zeroline':False,
                'showticklabels':False,
                'showline':False,
                'showgrid':True,


              }))

    fig.add_trace(
    go.Scattergl(
            x=df['x'],
            y=df['y'],
            text=df['words'],
            mode='markers',
            marker_symbol=1,
            marker_size=5,
            marker={'color':df['freq']},

    ))
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
