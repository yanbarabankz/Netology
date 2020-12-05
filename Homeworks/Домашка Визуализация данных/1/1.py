import pandas as pd
import matplotlib.pyplot as plt
from pylab import rcParams
rcParams['figure.figsize'] = 6,6

df=pd.read_csv('file.csv', encoding='cp1251')

data=df[['Малые']+['Средние']+['Крупные']+['Год']].groupby('Год').sum()

data[['Малые']+['Средние']+['Крупные']].plot(kind='bar', stacked=True, title='Количество действующих юридических лиц в Казахстане\n', ylabel='Количество, тыс.ед.', grid=True)

plt.savefig("High resoltion.png",dpi=1000)    
plt.legend(data)
plt.show()

