import re
import matplotlib.pyplot as plt
import numpy as np

google_trends = open('multiTimeline(14).csv')
list=[]

for value in google_trends:
    result = re.findall(r'\w+$', value)
    list.append(int(result[0]))

xlabel = np.arange(0, len(list), 1)
plt.plot(xlabel, list, linewidth=2.0, color='g')
plt.ylabel('Количество людей')
plt.xlabel('Год')
plt.title('Эмиграция из Казахстана')
plt.show()


