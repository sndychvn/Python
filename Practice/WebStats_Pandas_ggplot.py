import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,34,65,56,29,76],
             'Bounce Rate':[65,67,78,65,45,52],
             'Country' : ["USA", "FR", "IN", "TG", "GM", "ID"]}

df=pd.DataFrame(web_stats)
#print(web_stats.dtype())
print(df)
df.plot()
#df['Visitors'].plot()
plt.legend()
plt.show()

print(df.head(3))
print(df[['Bounce Rate','Day']].head(3))
print(df.tail(3))
print(df.set_index('Day').sort_index(ascending=False))
df.set_index('Day', inplace=True)
print(df.head(11111120))
print(df)

df.plot()
#df['Visitors'].plot()
plt.legend()
plt.show()
print(np.array(df)) # pandas df to np arrays with index as Date
df=pd.DataFrame(web_stats)
print(np.array(df))  # pandas df to np arrays