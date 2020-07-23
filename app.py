import plotly.express as px
import dash
import plotly.graph_objects as go
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import re
from getlyric import pull_lyric
from songs import songs
import time

themes=[{'label':'default','value':[[0.0, '#0d0887'], [0.1111111111111111,
                                  '#46039f'], [0.2222222222222222, '#7201a8'],
                                  [0.3333333333333333, '#9c179e'],
                                  [0.4444444444444444, '#bd3786'],
                                  [0.5555555555555556, '#d8576b'],
                                  [0.6666666666666666, '#ed7953'],
                                  [0.7777777777777778, '#fb9f3a'],
                                  [0.8888888888888888, '#fdca26'], [1.0,
                                  '#f0f921']]},
{'label': 'aggrnyl', 'value': 'aggrnyl'} ,
{'label': 'agsunset', 'value': 'agsunset'} ,
{'label': 'blackbody', 'value': 'blackbody'} ,
{'label': 'bluered', 'value': 'bluered'} ,
{'label': 'blues', 'value': 'blues'} ,
{'label': 'blugrn', 'value': 'blugrn'} ,
{'label': 'bluyl', 'value': 'bluyl'} ,
{'label': 'brwnyl', 'value': 'brwnyl'} ,
{'label': 'bugn', 'value': 'bugn'} ,
{'label': 'bupu', 'value': 'bupu'} ,
{'label': 'burg', 'value': 'burg'} ,
{'label': 'burgyl', 'value': 'burgyl'} ,
{'label': 'cividis', 'value': 'cividis'} ,
{'label': 'darkmint', 'value': 'darkmint'} ,
{'label': 'electric', 'value': 'electric'} ,
{'label': 'emrld', 'value': 'emrld'} ,
{'label': 'gnbu', 'value': 'gnbu'} ,
{'label': 'greens', 'value': 'greens'} ,
{'label': 'greys', 'value': 'greys'} ,
{'label': 'hot', 'value': 'hot'} ,
{'label': 'inferno', 'value': 'inferno'} ,
{'label': 'jet', 'value': 'jet'} ,
{'label': 'magenta', 'value': 'magenta'} ,
{'label': 'magma', 'value': 'magma'} ,
{'label': 'mint', 'value': 'mint'} ,
{'label': 'orrd', 'value': 'orrd'} ,
{'label': 'oranges', 'value': 'oranges'} ,
{'label': 'oryel', 'value': 'oryel'} ,
{'label': 'peach', 'value': 'peach'} ,
{'label': 'pinkyl', 'value': 'pinkyl'} ,
{'label': 'plasma', 'value': 'plasma'} ,
{'label': 'plotly3', 'value': 'plotly3'} ,
{'label': 'pubu', 'value': 'pubu'} ,
{'label': 'pubugn', 'value': 'pubugn'} ,
{'label': 'purd', 'value': 'purd'} ,
{'label': 'purp', 'value': 'purp'} ,
{'label': 'purples', 'value': 'purples'} ,
{'label': 'purpor', 'value': 'purpor'} ,
{'label': 'rainbow', 'value': 'rainbow'} ,
{'label': 'rdbu', 'value': 'rdbu'} ,
{'label': 'rdpu', 'value': 'rdpu'} ,
{'label': 'redor', 'value': 'redor'} ,
{'label': 'reds', 'value': 'reds'} ,
{'label': 'sunset', 'value': 'sunset'} ,
{'label': 'sunsetdark', 'value': 'sunsetdark'} ,
{'label': 'teal', 'value': 'teal'} ,
{'label': 'tealgrn', 'value': 'tealgrn'} ,
{'label': 'viridis', 'value': 'viridis'} ,
{'label': 'ylgn', 'value': 'ylgn'} ,
{'label': 'ylgnbu', 'value': 'ylgnbu'} ,
{'label': 'ylorbr', 'value': 'ylorbr'} ,
{'label': 'ylorrd', 'value': 'ylorrd'} ,
{'label': 'algae', 'value': 'algae'} ,
{'label': 'amp', 'value': 'amp'} ,
{'label': 'deep', 'value': 'deep'} ,
{'label': 'dense', 'value': 'dense'} ,
{'label': 'gray', 'value': 'gray'} ,
{'label': 'haline', 'value': 'haline'} ,
{'label': 'ice', 'value': 'ice'} ,
{'label': 'matter', 'value': 'matter'} ,
{'label': 'solar', 'value': 'solar'} ,
{'label': 'speed', 'value': 'speed'} ,
{'label': 'tempo', 'value': 'tempo'} ,
{'label': 'thermal', 'value': 'thermal'} ,
{'label': 'turbid', 'value': 'turbid'} ,
{'label': 'armyrose', 'value': 'armyrose'} ,
{'label': 'brbg', 'value': 'brbg'} ,
{'label': 'earth', 'value': 'earth'} ,
{'label': 'fall', 'value': 'fall'} ,
{'label': 'geyser', 'value': 'geyser'} ,
{'label': 'prgn', 'value': 'prgn'} ,
{'label': 'piyg', 'value': 'piyg'} ,
{'label': 'picnic', 'value': 'picnic'} ,
{'label': 'portland', 'value': 'portland'} ,
{'label': 'puor', 'value': 'puor'} ,
{'label': 'rdgy', 'value': 'rdgy'} ,
{'label': 'rdylbu', 'value': 'rdylbu'} ,
{'label': 'rdylgn', 'value': 'rdylgn'} ,
{'label': 'spectral', 'value': 'spectral'} ,
{'label': 'tealrose', 'value': 'tealrose'} ,
{'label': 'temps', 'value': 'temps'} ,
{'label': 'tropic', 'value': 'tropic'} ,
{'label': 'balance', 'value': 'balance'} ,
{'label': 'curl', 'value': 'curl'} ,
{'label': 'delta', 'value': 'delta'} ,
{'label': 'edge', 'value': 'edge'} ,
{'label': 'hsv', 'value': 'hsv'} ,
{'label': 'icefire', 'value': 'icefire'} ,
{'label': 'phase', 'value': 'phase'} ,
{'label': 'twilight', 'value': 'twilight'} ,
{'label': 'mrybm', 'value': 'mrybm'} ,
{'label': 'mygbm', 'value': 'mygbm'} ,
]   

app = dash.Dash(__name__,assets_external_path="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css",  
                    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ])
server=app.server
app.layout = html.Div(style={'height':'95vh','width':'99vw','text-align':'center','backgroundColor':'#111111'},
children=[
    html.Div(
        children=
            [
                    html.P('Popular Examples-',style={'color':'white','font-family':'Verdana'}),
                    dcc.Dropdown(id='song-dropdown',
                        options=songs,
                        clearable=False,
                        value='https://www.metrolyrics.com/we-will-rock-you-lyrics-queen.html'),
                    html.P('Search Song by Name-',style={'color':'white','font-family':'Verdana'}),
                    dcc.Input(id='artist-name', value='',placeholder='Artist Name', type='text'),
                    dcc.Input(id='artist-song', value='',placeholder='Name of Song' ,type='text'),
                    html.Div(
                        children=[
                        html.P('Search Song by URL(Only MetroLyrics)-',style={'color':'white','font-family':'Verdana'}),
                        dcc.Input(id='song-url', value='',type='text',style={'width':'70%'})
                                ],style={'width':'100%'}),
                     html.P('Color Scheme-',style={'color':'white','font-family':'Verdana'}),
                    dcc.Dropdown(id='theme',
                        options=themes,
                        clearable=False,
                        value='default',style={'color':'black'}),
            ],style={'max-width':'250','float':'left','text-align':'left'}),

    html.Div(children=[
        dcc.Graph(id="graph",responsive=True,style={'height':'100%','width':'100%'}),
        html.Div(
        dcc.RadioItems(id='stopword-choice',
                        options=[
                                {'label': 'Show All', 'value': 1 },
                                {'label': 'Ignore Stopwords', 'value': 0},
                                ],
                        value=1),style={'float':'left','color':'white'})
    ],style={'width':'100vw','height':'100vw','max-height':'850px','float':'left','max-width':'850px', 'display': 'inline-block'}),
    html.Div(html.P('Placeholder Text Placeholder Text Placeholder Text Placeholder Text Placeholder Text Placeholder Text Placeholder Text Placeholder Text',style={'float':'left'}),style={'max-width':'500px','padding-top':'20px','float':'right'})
    

])

@app.callback(
    Output('graph', 'figure'),
    [
     Input(component_id='song-url', component_property='value'),
     Input(component_id='stopword-choice', component_property='value'),
     Input(component_id='theme', component_property='value')]
)
def update_graph(song_url,stopword_choice,theme):
    url = song_url
    if stopword_choice==1:
        df = pull_lyric(url,False)
    else:
        df = pull_lyric(url,True)
    fig=go.Figure(layout=go.Layout(
        hovermode='closest',
        template='plotly_dark',
        xaxis =  {                                     
                    'ticks':'',
                    'zeroline':False,
                    'showticklabels':False,
                    'showline':False,
                    'showgrid':False,
                    'tickmode':"array",
                    'ticktext':df['words'],
                    'tickvals':[x for x in range(len(df['words']))],
                  },
        yaxis = {                              
                'ticks':'',
                'zeroline':False,
                'showticklabels':False,
                'showline':False,
                'showgrid':False,
                'tickmode':"array",
                'ticktext':df['words'],
                'tickvals':[x for x in range(len(df['words']))],


              })
              )

    fig.add_trace(
    go.Heatmap(
            z=df['z'],
            colorscale=theme,
            hoverongaps = False

    ))
    return fig



@app.callback(
    Output('song-url', 'value'),
    [
     Input(component_id='song-dropdown', component_property='value'),
     Input(component_id='artist-name', component_property='value'),
     Input(component_id='artist-song', component_property='value')]
)
def update_url_on_text(dropdown_url,artist_name,artist_song):
    if artist_name!='' and artist_song!='':
        time.sleep(0.5)
        url=f"https://www.metrolyrics.com/{artist_song.lower().replace(' ','-')}-lyrics-{artist_name.lower().replace(' ','-')}.html"
    else:
        url=dropdown_url
    return url

@app.callback(
    Output('artist-song','value'),
    [
     Input(component_id='song-dropdown', component_property='value')
     ]
)
def clearsearchsong(value):
    if value!=None:
        return ''

@app.callback(
    Output('artist-name','value'),
    [
     Input(component_id='song-dropdown', component_property='value')
     ]
)
def clearsearchname(value):
    if value!=None:
        return ''

if __name__ == '__main__':
    app.run_server(debug=False)
