# coding=UTF-8

import plotly.offline as py
import plotly.graph_objs as go
import numpy as np

def CreData():
    x = np.arange(-np.pi, np.pi, 0.0001)
    #y = np.sin(x)

    #(sqrt(cos(x)) * cos(200 * x) + sqrt(abs(x)) - 0.7) * (4 - x ^ 2) ^0.01
    y=(np.sqrt(np.cos(x))*np.cos(200*x)+np.sqrt(np.abs(x))-0.7)*pow((4-np.square(x)),0.1)
    dataD = dict(x=x, y=y)

    print(type(x))

    return dataD

def CreScatter():

     dataN=CreData()
     trace1=go.Bar(
         x=dataN["x"],
         y=dataN["y"],
         #  mode="lines",
         #  line=dict(
         #      color="#feb4d1"
         #  ),
         # yaxis="yaxis"

     )
     layout = go.Layout(
         yaxis=dict(showline=True,
                    autorange=True,
                    zeroline=True,
                    linecolor="#feb4d1",
                    anchor="x",
                    type="linear")

     )
     fig = go.Figure(data=[trace1])

     py.plot(fig, filename="heart.html", image_filename="heart", image="png")


if __name__ == '__main__':
    CreScatter()