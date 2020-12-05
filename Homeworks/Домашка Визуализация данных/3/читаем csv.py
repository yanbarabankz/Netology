
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pylab import rcParams

rcParams['figure.figsize'] = 6,6

df=pd.read_csv('file.csv')

data=df[['value2']+['value3']+['year']]



plt.plot(data.year, data.value2,linewidth=5, color='r' )
plt.plot(data.year, data.value3,linewidth=5, color='b' )

plt.title('Динамика продаж видеоигр')

plt.xlabel('Год')

plt.ylabel('Продажи, млн.')

plt.grid(True)

plt.legend(data)

plt.savefig("High resoltion.png",dpi=1000)
plt.show()


