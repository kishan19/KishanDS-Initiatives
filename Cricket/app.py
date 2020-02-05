import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')
# Add colours, alignment of text
##Some text can also be inserted by using Markdown


colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}


app.layout = html.Div(style={'backgroundColor': ''}, children=[
    html.H1(children='Decoding the DRS', style={'textAlign': 'center',
                                                'color': colors['text']}),

    html.Div(style={'textAlign': 'center', 'color': ''}, children='''
        Statistical study of the Decision Review System used by teams, players and umpires
    '''),

 html.Label('Format'),
 
 
    dcc.Dropdown(id='dr',
                 
        options=[
            {'label': 'Test', 'value': 'Test'},
            {'label': 'ODI', 'value': 'ODI'},
            {'label': 'T20I', 'value': 'T20I'}
        ],
        value='Test'
    ),
    
    html.Br(),
    html.Br(),
    
    html.Label('Commentary Search'),
    
    dcc.Input(id='com-box',value='Search for referral events in Commentary', type='text'),
    
    html.Div(id='com-output'),
    
    html.Div(id='com-output2')
    
    
    # dcc.Graph(
    #     id='example-graph',
    #     figure={
    #         'data': [
    #             {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
    #             {'x': [1, 2, 3], 'y': [2, 4, 5],
    #                 'type': 'bar', 'name': u'Montréal'},
    #         ],
    #         'layout': {
    #             'title': 'Dash Data Visualization',
    #             'plot_bgcolor': '',
    #             'paper_bgcolor':'',
    #             'font':{'color':colors['text']}
    #         }
    #     }
    # ),
    
    # dcc.Graph(
    #     id='life-exp-vs-gdp',
    #     figure={
    #         'data': [
    #             dict(
    #                 x=df[df['continent'] == i]['gdp per capita'],
    #                 y=df[df['continent'] == i]['life expectancy'],
    #                 text=df[df['continent'] == i]['country'],
    #                 mode='markers',
    #                 opacity=0.7,
    #                 marker={
    #                     'size': 15,
    #                     'line': {'width': 0.5, 'color': 'white'}
    #                 },
    #                 name=i
    #             ) for i in df.continent.unique()
    #         ],
    #         'layout': dict(
    #             xaxis={'type': 'log', 'title': 'GDP Per Capita'},
    #             yaxis={'title': 'Life Expectancy'},
    #             margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
    #             legend={'x': 0, 'y': 1},
    #             hovermode='closest'
    #         )
    #     }
    # )
])


##Callbacks are added after the Layout

@app.callback(
    Output(component_id='com-output', component_property='children'),
    [Input(component_id='dr', component_property='value')]
)
##This is the callback function associated with this callback
def update_output_div(input_value):
    return 'You\'ve entered {}'.format(input_value)


if __name__ == '__main__':
    app.run_server(debug=True)
