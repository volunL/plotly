# coding=UTF-8

import plotly.offline as py
import plotly.graph_objs as go
import numpy as np


def Credata():

    datalist=[]
    #右上
    x = np.linspace(0, np.pi, 100)
    y=np.power(np.power(np.pi,2)-x*x,1/2)
    t=np.power(0,1/2)
    redata=dict(x=x,y=y)
    datalist.append(redata)

    #左上
    x=np.linspace(-np.pi,0,100)
    y=np.power(np.power(np.pi,2)-x*x,1/2)
    redata=dict(x=x,y=y)
    datalist.append(redata)


    #右下
    x = np.linspace(0, np.pi, 100)
    y = -np.power(np.power(np.pi,2) - x * x, 1 / 2)
    redata = dict(x=x, y=y)
    datalist.append(redata)

    # 左下
    x = np.linspace(-np.pi, 0, 100)
    y = -np.power(np.power(np.pi,2) - x * x, 1 / 2)
    redata = dict(x=x, y=y)
    datalist.append(redata)


    return datalist

def SinData():
    x = np.arange(-np.pi, np.pi, 0.001)
    y = np.sin(x)
    reData=dict(x=x,y=y)
    return reData
def oSinData():
    x=np.arange(-np.pi, np.pi, 0.001)
    y=-np.sin(x)
    reData=dict(x=x,y=y)
    return reData

def GetTrace(datalist):
    tracelist=[]
    for data in datalist:
        trace=go.Bar(
            x=data["x"],
            y=data["y"],
            width=0.03
            #mode="lines",
            #  line=dict(
            #      color="#feb4d1"
            #  ),


        )

        tracelist.append(trace)



    sinData=SinData()
    trace=go.Scatter(
        x=sinData['x'],
        y=sinData['y'],

        line=go.Line(color='#eeeeee')
    )
    tracelist.append(trace)

    osinData = oSinData()
    trace = go.Scatter(
        x=osinData['x'],
        y=osinData['y'],

        line=go.Line(color='#eeeeee')
    )
    tracelist.append(trace)


    return tracelist

def main():
    data=Credata()
    tracelist=GetTrace(data)
    layout = go.Layout(
        showlegend=False,
        width=700,
        height=740

    )
    fig = go.Figure(data=tracelist,layout=layout)


    py.plot(fig, filename="heart.html")


if __name__ == '__main__':
     main()