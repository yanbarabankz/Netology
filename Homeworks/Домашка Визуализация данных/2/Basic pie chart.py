import re
import matplotlib.pyplot as plt

from pylab import rcParams

rcParams['figure.figsize'] = 5,5

with plt.style.context('seaborn-bright'):
    with plt.xkcd():

        sizes=[]
        

        file =open('file.csv')

        for value in file:
            result = re.findall(r'\w+', value)
            sizes.append(int(result[0]))
           
            

        labels = 'Курят', 'Не курят'
        explode = (0.1, 0)
            

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes,explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=False, startangle=0)
            
        ax1.set(xlabel='', title='Потребление табака в Казахстане')
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    
plt.savefig("High resoltion.png",dpi=500)    
plt.show()


