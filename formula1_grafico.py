import pandas as pd
import plotly.express as px

local = 'C:\\Dev\\faculdade\\formula1.xlsx'
arquivo = pd.read_excel(local, engine='openpyxl')

# print(arquivo['PILOTO'])

pilotos = arquivo['PILOTO']
pontos = arquivo['PONTOS']

grafico = px.bar(x=pilotos, y=pontos, width=1000, height=500)

grafico.update_layout(
    title='PONTOS DOS PILOTOS',
    xaxis_title='PILOTOS',
    yaxis_title='PONTOS',
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="RebeccaPurple"
    )
)

grafico.show()