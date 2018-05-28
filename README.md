# Fibonacci Bollinger Bands 

A simple script i wrote because i like Fibonacci Bollinger Bands and i couldn't find a version in python. 

Basic formula is MA +/- (fib*(m*stddev))

Where fib represents fibonacci ratio, m represents the standard bollinger multiplier and MA represents the moving average, which currently is SMA. 

Also contains a basic function to plot the fibonacci bands on a OHLC chart using plotly (offline). 

![alt text](https://i.gyazo.com/3ff05e3e333c7e17643cf83d81e9a4bd.png "Logo Title Text 1")

# Usage

Requirements: Pandas, Pandas_webreader, plotly, datetime 

```
df = fibonacci_bollinger_bands(df, n=20, m=3)
```
df = dataframe which must contain 'Close', 'Open', 'High', 'Low' columns

n  = Period for moving average

m  = multiplier for bollinger bands (m * standard deviation)

returns:
A dataframe with a new column for each band. 

```
plot_fbb(df, fname="Test", n=20, m=3)
```
df = dataframe which must contain 'Close', 'Open', 'High', 'Low' columns

fname = File name to store the output graph (.html)

n  = Period for moving average

m  = multiplier for bollinger bands (m * standard deviation)

returns:
A .html file containing the plotted graph. Will also open the graph in your default browser. 


The if __name__ == '__main__' shows example usage. 
