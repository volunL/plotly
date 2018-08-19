# coding=UTF-8

import plotly.offline as plot
import plotly.graph_objs as go
import numpy as np
def CreData():
    x = np.arange(-np.pi,np.pi,0.01)
    y = np.sin(x)
    # 使成为二维数组
    #dataD = np.column_stack((x, y))
    dataD=dict(x=x,y=y)


    print(type(x))


    return dataD


#def CircleData():
    # x=np.arange(-1,1,0.01)
    # for i in x:
    # #r=np.pow(x,2)+np.pow(y,2)

def main():
    dataN=CreData()
    #生成trace
    trace=go.Scatter(
        x=dataN["x"],
        y=dataN["y"],
        #mode="lines",
        # line=dict(
        #     color="#45aa89"
        # ),
        yaxis="y"
    )
    layout=go.Layout(
        yaxis=dict(showline=False,
                   autorange=True,
                   zeroline=True,
                   linecolor="#450089",
                   anchor="x",
                   type="linear")

    )


    fig=go.Figure(data=[trace])

    plot.plot(fig,filename="nddata.html")



if __name__ == '__main__':
   main()