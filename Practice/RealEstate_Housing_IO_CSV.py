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