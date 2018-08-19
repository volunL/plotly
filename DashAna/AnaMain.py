# coding=UTF-8

'''
Dash 示例程序
'''
import dash
import random
import dash_core_components as dcc
import dash_html_components as html
import plotly.offline as py
import plotly.graph_objs as go
import pandas as pd
from datetime import datetime as datetime


def struDate(edata):
    reData = []
    for i in edata:
        if (isinstance(i, str) == False):
            ri = i.strftime('%Y-%m-%d')
            reData.append(ri)
        else:
            ri = datetime.strptime(i.strip(), '%Y-%m-%d')
            reData.append(ri)
    return reData


def lowHs(data):
    reData = []
    for i in data:
        ri = i
        reData.append(ri)
    return reData


def DataScatter(edata):
    reData = []
    head = list(edata)
    dx = struDate(edata[head[0]])
    dy = []

    for h in range(1, len(head)):
        dy = edata[head[h]]
        if (head[h] == "收盘"):
            dy = lowHs(edata[head[h]])

        scatter1 = go.Scatter(
            name=head[h],
            x=dx,
            y=dy,
            mode='markers+lines',
            marker=go.Marker(color='#%s' % (random.randint(100000, 999999))),
            yaxis="y1"
        )
        if (head[h]=="收盘"):
            scatter1["yaxis"]="y2"
        reData.append(scatter1)
    return reData


# 读取Excel
excel_path = 'excel/Shibor2018.xls'
edata = pd.read_excel(excel_path, header=[0])

excel_path2 = 'excel/2018hs300.xlsx'
edata2 = pd.read_excel(excel_path2, header=[0], usecols=[0, 2])

alldata = DataScatter(edata2) + DataScatter(edata)

# 实例化一个Dash对象
app = dash.Dash()
'''
dash页面的布局结构为:
1 整个页面是一个div
2 div内设定一个h1型号的标题
3 div内包含一个子div,且内容为一行文本

'''
layout =html.Div(style={"width":"100%","height":"900","margin":"auto",
                        "top": "0",
                        "left": "10",
                        "right": "10",
                        "buttom": "0"


                        },children=[
    html.H1(children='Hello Dash',style={"width":"90%","margin":"auto","left": "10",
                        "right": "10"}),
    html.Div(style={"width":"90%","margin":"auto","left": "10",
                        "right": "10"},children='''
        Dash: A web application framework for Python.
    '''),
    dcc.Graph(
        # 唯一标识该图形，此属性并不显示在页面
        id='example-graph',
        # 图形的具体内容
        figure=go.Figure(
            data=alldata,
            layout=go.Layout(
                dragmode="zoom",
                hovermode="x",
                title='Shibor VS 沪深300指数 2018',
                showlegend=True,
                legend=go.Legend(orientation="h",x=0,y=1),
                #margin=go.Margin(t=100, b=100),
                xaxis={"autorange": True,
                       "range": ["2018-01-01", "2018-08-01"],
                       "rangeslider": {
                           "autorange": True,
                           "range": ["2018-01-01", "2018-08-01"]
                       },
                       "type": "date"
                       },
                yaxis1={"anchor": "x",
                       "autorange": True,
                       "domain": [0.0, 0.4],
                       "linecolor": "#607d8b",
                       "mirror": True,
                       "range": [1.0, 5.0],
                       "showline": True,
                       "side": "right",
                       "tickfont": {"color": "#607d8b"},
                       "tickmode": "auto",
                       "ticks": "",
                       "title": "shibor",
                       "titlefont": {"color": "#607d8b"},
                       "type": "linear",
                       "zeroline": False
                       },
                yaxis2={"anchor": "x",
                       "autorange": True,
                       "domain": [0.4, 0.8],
                       "linecolor": "#60008b",
                       "mirror": True,
                       "range": [1000.0, 3000.0],
                       "showline": True,
                       "side": "right",
                       "tickfont": {"color": "#60008b"},
                       "tickmode": "auto",
                       "ticks": "",
                       "title": "HS",
                       "titlefont": {"color": "#60008b"},
                       "type": "linear",
                       "zeroline": False}
            )
        ),
         style={"height": "100%",
                "width": "90%",
                 "margin":"auto",
                #"position":"absolute",
                 "top":"0",
                 "left":"0",
                 "right":"0",
                 "buttom":"0"
                }

    )
])


fig=figure=go.Figure(
            data=alldata,
            layout=go.Layout(
                dragmode="zoom",
                hovermode="x",
                title='Shibor VS 沪深300指数 2018',
                showlegend=True,
                legend=go.Legend(orientation="h",x=0,y=1),
                #margin=go.Margin(t=100, b=100),
                xaxis={"autorange": True,
                       "range": ["2018-01-01", "2018-08-01"],
                       "rangeslider": {
                           "autorange": True,
                           "range": ["2018-01-01", "2018-08-01"]
                       },
                       "type": "date"
                       },
                yaxis1={"anchor": "x",
                       "autorange": True,
                       "domain": [0.0, 0.4],
                       "linecolor": "#607d8b",
                       "mirror": True,
                       "range": [1.0, 5.0],
                       "showline": True,
                       "side": "right",
                       "tickfont": {"color": "#607d8b"},
                       "tickmode": "auto",
                       "ticks": "",
                       "title": "shibor",
                       "titlefont": {"color": "#607d8b"},
                       "type": "linear",
                       "zeroline": False
                       },
                yaxis2={"anchor": "x",
                       "autorange": True,
                       "domain": [0.4, 0.8],
                       "linecolor": "#60008b",
                       "mirror": True,
                       "range": [1000.0, 3000.0],
                       "showline": True,
                       "side": "right",
                       "tickfont": {"color": "#60008b"},
                       "tickmode": "auto",
                       "ticks": "",
                       "title": "HS",
                       "titlefont": {"color": "#60008b"},
                       "type": "linear",
                       "zeroline": False}
            )
        )


app.layout=layout




# 入口方法
if __name__ == '__main__':
    #app.run_server(debug=True)
    py.plot(fig,filename="shibor.html")
