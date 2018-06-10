import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

df = pd.read_csv('E:\ZILLOW-C25709_ZRISFRR.csv')
print(df.head())

#df.set_index('Date', inplace=True)
df.to_csv('Test1.csv')
print(df.head())
df=pd.read_csv('Test1.csv')
df.set_index('Date', inplace=True)
df=pd.read_csv('Test1.csv', index_col=0)
df.set_index('Date', inplace=True)
print(df.head())

df.plot()
#df['Visitors'].plot()
plt.legend()
plt.show()

df = pd.read_csv('Test18.csv', index_col=0)
print(df.head())

df.columns = ['Real Date', 'Arlington_HPI', 'Dallas_HPI', 'A&M_HPI']
print(df.head())
df.set_index('Real Date', inplace=True)
print(df.head())
df.to_csv('Test19.csv', header=False, index=False)
print(pd.read_csv('Test19.csv', index_col=0))
print(df.rename(columns={'Dallas_HPI' : '77706_HPI'}).head())
