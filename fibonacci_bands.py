import pandas as pd
import plotly.offline as py_offline
import plotly.graph_objs as go
import pandas_datareader as web
import datetime as datetime

def fibonacci_bollinger_bands(df, n=20, m=3):
    tp = (df['High'] + df['Low'] + df['Close']) / 3
    ma = tp.rolling(n).mean()
    sd = m * tp.rolling(n).std()
    df['FBB_mid'] = ma
    df['FBB_up1'] = ma + (0.236 * sd)
    df['FBB_up2'] = ma + (0.382 * sd)
    df['FBB_up3'] = ma + (0.5 * sd)
    df['FBB_up4'] = ma + (0.618 * sd)
    df['FBB_up5'] = ma + (0.764 * sd)
    df['FBB_up6'] = ma + (1 * sd)
    df['FBB_low1'] = ma - (0.236 * sd)
    df['FBB_low2'] = ma - (0.382 * sd)
    df['FBB_low3'] = ma - (0.5 * sd)
    df['FBB_low4'] = ma - (0.618 * sd)
    df['FBB_low5'] = ma - (0.764 * sd)
    df['FBB_low6'] = ma - (1 * sd)
    return df


def plot_fbb(df, fname, n=20, m=3):
    fibonacci_bollinger_bands(df, n, m)
    index = list(range(len(df['Close'])))
    trace = go.Candlestick(
                           x=index,
                           open=df['Open'],
                           high=df['High'],
                           low=df['Low'],
                           close=df['Close'],
                           name="OHLC")

    ls_up = dict(
        color='rgb(255, 0, 0, 0.5)'
    )
    ls_mid = dict(
        color='rgb(255,20,147, 0.5)'
    )
    ls_low = dict(
        color='rgb(34,139,34, 0.5)'
    )
    ls_fib = dict(
        color='rgb(169,169,169,0.5)',
        width="1"
    )

    t_mid = go.Scatter(x=index, y=df.FBB_mid, line=ls_mid, name="Middle Band")
    t_up1 = go.Scatter(x=index, y=df.FBB_up1, line=ls_fib, showlegend=False, hoverinfo='none')
    t_up2 = go.Scatter(x=index, y=df.FBB_up2, line=ls_fib, showlegend=False, hoverinfo='none')
    t_up3 = go.Scatter(x=index, y=df.FBB_up3, line=ls_fib, showlegend=False, hoverinfo='none')
    t_up4 = go.Scatter(x=index, y=df.FBB_up4, line=ls_fib, showlegend=False, hoverinfo='none')
    t_up5 = go.Scatter(x=index, y=df.FBB_up5, line=ls_fib, showlegend=False, hoverinfo='none')
    t_up6 = go.Scatter(x=index, y=df.FBB_up6, line=ls_up, name="Upper Band")
    t_low1 = go.Scatter(x=index, y=df.FBB_low1, line=ls_fib, showlegend=False, hoverinfo='none')
    t_low2 = go.Scatter(x=index, y=df.FBB_low2, line=ls_fib, showlegend=False, hoverinfo='none')
    t_low3 = go.Scatter(x=index, y=df.FBB_low3, line=ls_fib, showlegend=False, hoverinfo='none')
    t_low4 = go.Scatter(x=index, y=df.FBB_low4, line=ls_fib, showlegend=False, hoverinfo='none')
    t_low5 = go.Scatter(x=index, y=df.FBB_low5, line=ls_fib, showlegend=False, hoverinfo='none')
    t_low6 = go.Scatter(x=index, y=df.FBB_low5, line=ls_low, name="Lower Band")

    layout = go.Layout(
        title='OHLC with Fibonacci Bands',
        xaxis=go.XAxis(
            tickmode='array',
            nticks=90,
            tickvals=index,
            ticktext=df.index),
        yaxis=go.YAxis(
            title='Price'))

    data = go.Data([trace,
                    t_mid, t_up1, t_up2, t_up3, t_up4, t_up5, t_up6,
                    t_low1, t_low2, t_low3, t_low4, t_low5, t_low6])
    fig = go.Figure(data=data, layout=layout)
    py_offline.plot(fig, filename=fname+".html")


if __name__ == '__main__':
    start = datetime.datetime(2017, 1, 1)
    end = datetime.datetime.now()
    df = web.DataReader('AAL', 'google', start, end)
    plot_fbb(df, "Test")