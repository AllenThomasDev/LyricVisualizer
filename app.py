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

# https://www.metrolyrics.com/thinking-about-you-lyrics-frank-ocean.html
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
                        dcc.Input(id='song-url', value='',type='text',style={'width':'70%'})],style={'width':'100%'})
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
     Input(component_id='stopword-choice', component_property='value')]
)
def update_graph(song_url,stopword_choice):
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
