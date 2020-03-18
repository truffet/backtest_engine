from fetch_data import fetch_data
import pandas as pd


#fetch data
data = fetch_data()

#set max rows to display
pd.set_option('display.max_rows', 1000)

# convert to dataframe
df = pd.DataFrame(data, columns = ['timestamp', 'price', 'volume'])
df['timestamp'] = df.timestamp/100000000
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
df = df.set_index('timestamp')
df = df.resample('60Min').agg({'price': 'ohlc', 'volume': 'sum'})

print(df)