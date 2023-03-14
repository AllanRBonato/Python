import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output

app = Dash(__name__)

df = pd.read_excel('relatorio.xlsx')

fig = px.bar(df, x='Usuário', y='Chamado', barmode="group")
fig2 = px.bar(df, x='Técnico', y='Quantidade', barmode='group')
fig3 = px.bar(df, x='Regional', y='Quantidade', barmode='group')

opecoes = list(df['Usuário'].unique())
opecoes.append('Todos os usuarios')

relatorioTecnico = list(df['Técnico'].unique())
relatorioTecnico.append('Todos os técnicos')

relatorioRegional = list(df['Regional'].unique())
relatorioRegional.append('Todas as Regionais')

app.layout = html.Div(children=[
    # Relátorio atendimento
    html.H1(children='Relatório de Desempenho', style={'color': 'white',
                                                       'fontsize': 12,
                                                       'background': 'black',
                                                       'border-radius': 10,
                                                       'padding': 5
                                                       }),
    html.P('Janeiro', style={'color': 'white',
                             'background': 'black',
                             'border-radius': 5,
                             'padding': 10,
                             'opacity': 0.5
                             }),

    dcc.Dropdown(opecoes, value='Todos os usuarios', id='lista_usuario'),

    dcc.Graph(
        id='relatorioDesempenho',
        figure=fig
    ),

    # Relátori técnico

    html.P('Relátorio Técnico', style={'color': 'white',
                                       'fontsize': 12,
                                       'background': 'black',
                                       'border-radius': 5,
                                       'padding': 10
                                       }),

    dcc.Dropdown(relatorioTecnico, value='Todos os técnicos', id='lista_tecnicos'),

    dcc.Graph(
        id='relatorioTecnico',
        figure=fig2
    ),

    # Relátori regionais

    html.P('Relátorio Regional', style={'color': 'white',
                                        'fontsize': 12,
                                        'background': 'black',
                                        'border-radius': 5,
                                        'padding': 10
                                        }),

    dcc.Dropdown(relatorioRegional, value='Todas as Regionais', id='lista_regional'),

    dcc.Graph(
        id='relatorioRegional',
        figure=fig3
    )

])


# Relátori atendimento
@app.callback(
    Output('relatorioDesempenho', 'figure'),
    Input('lista_usuario', 'value')
)
def update_output(value):
    if value == "Todos os usuarios":
        fig = px.bar(df, x='Usuário', y='Quantidade', color='Chamado', barmode="group")
    else:
        tabela_filtrada = df.loc[df['Usuário'] == value, :]
        fig = px.bar(tabela_filtrada, x='Usuário', y='Quantidade', color='Chamado', barmode="group")
    return fig


# Relátorio Técnico
@app.callback(
    Output('relatorioTecnico', 'figure'),
    Input('lista_tecnicos', 'value')
)
def update_output(value):
    if value == "Todos os Técnicos":
        fig2 = px.bar(df, x='Técnico', y='Quantidade', color='Chamado', barmode='group')
    else:
        tabela_filtrada2 = df.loc[df['Técnico'] == value, :]
        fig2 = px.bar(tabela_filtrada2, x='Técnico', y='Quantidade', color='Chamado', barmode='group')
    return fig2


if __name__ == '__main__':
    app.run_server(debug=False)