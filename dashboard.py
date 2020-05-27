import pandas as pd
import plotly.graph_objs as go
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output,Input
data=pd.read_csv('gapminder.csv')
app=dash.Dash()
app.layout=html.Div([
    html.Div(children=[html.H1("My First Dashboard",style={'color':'red','text-align':'center','font-size': '26px'})],
             style={'border':'1px black solid','float':'left','width':'99.83%','height':'50px'}),
    html.Div(children=[
                    dcc.Graph(id='scatter-plot',
                              figure={'data':[go.Scatter(x=data['population'],
                                                         y=data['gdp_cap'],
                                                         mode='markers')],
                                      'layout':go.Layout(title='Scatter Plot')}

                            )
                     ],style={'border':'1px black solid','float':'left','width':'49.9%'}),
    html.Div(children=[
                    dcc.Graph(id='box-plot',
                              figure={'data':[go.Box(x=data['gdp_cap'])],
                                      'layout':go.Layout(title='Box Plot')}

                            )
                     ],style={'border':'1px black solid','float':'left','width':'49.8%'})
])
if __name__=='__main__':
    app.run_server()