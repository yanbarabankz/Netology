import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm

from pylab import rcParams

rcParams['figure.figsize'] = 3.5,5


vegetables = [ "2009", '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
farmers = [





'Нур-Султан',#
'Алматы',#
'ЗКО',#
'Шымкент',#
'Алматинская',#
'Костанайская',#
'СКО',        # 
"Акмолинская",#
'Туркестанская', #   
'Мангистауская',#
'Атырауская',#
'Актюбинская',#
'Жамбылская',#
'ВКО',#
'Павлодарская',#
'Кызылординская',
'Карагандинская',#
'ЮКО'
           
           
           
           
           
           
           ]

harvest = np.array([

[32.2,	28.9,	31.5,	28.6,	29.1,	61.8,	46.0,	57.4,	54.4,	48.6,	55.1],#
[25.4,	30.2,	25.8,	25.4,	22.3,	33.9,	29.1,	33.7,	35.3,	40.1,	44.8],#
[26.9,	32.3,	12.6,	11.0,	13.6,	38.7,	39.9,	41.9,	40.1,	36.0,	37.3],#
[0,	0,	0,	0,	0,	0,	0,	0,	0,	25.6,	34.1],#
[27.8,	33.1,	25.9,	24.9,	23.7,	27.0,	25.1,	26.9,	26.4,	32.0,	33.6],#
[17.4,	21.0,	20.2,	17.7,	17.6,	23.3,	21.8,	23.2,	25.1,	29.4,	32.8],#
[22.6,	25.0,	25.3,	25.6,	25.6,	25.2,	23.9,	24.4,	25.4,	29.7,	30.3],#
[20.3,	24.0,	23.4,	20.1,	19.5,	23.1,	25.6,	26.1,	25.1,	30.8,	28.6],#
[0,	0,	0,	0,	0,	0,	0,	0,	0,	19.5,	23.1],#
[9.1,	16.1,	10.7,	10.2,	9.7,	17.6,	19.9,	22.9,	15.6,	16.8,	22.9],#
[10.2,	8.1,	6.9,	7.3,	5.8,	8.8,	14.2,	11.8,	16.8,	18.7,	22.0],#
[10.6,	17.7,	13.8,	14.1,	13.5,	17.8,	22.1,	19.4,	18.3,	20.7,	21.2],#
[17.6,	21.0,	18.1,	16.9,	19.3,	20.1,	19.9,	19.8,	18.8,	20.9,	20.9],#
[13.7,	16.2,	16.7,	15.4,	14.6,	14.2,	15.4,	16.9,	15.7,	18.0,	19.5],#
[9.3,	13.3,	11.8,	11.9,	12.1,	18.5,	19.7,	15.1,	17.4,	16.2,	18.6],#
[11.2,	14.3,	8.7,	11.3,	10.6,	12.0,	13.5,	13.2,	14.2,	16.9,	17.8],#
[7.6,	10.7,	10.7,	11.1,	11.1,	12.4,	12.7,	12.1,	12.7,	17.2,	16.8],#
[14.8,	21.2,	18.7,	16.6,	16.1,	19.7,	20.2,	22.9,	21.9,	0,	0]
                    
                  
                

                   ])


fig, ax = plt.subplots()
im = ax.imshow(harvest, cmap="RdYlGn")

# We want to show all ticks...
ax.set_xticks(np.arange(len(vegetables)))
ax.set_yticks(np.arange(len(farmers)))
# ... and label them with the respective list entries
ax.set_xticklabels(vegetables, size=5)
ax.xaxis.tick_top()
ax.set_yticklabels(farmers, size=6)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="left",
         rotation_mode="anchor", size=5)

# Loop over data dimensions and create text annotations.
for i in range(len(farmers)):
    for j in range(len(vegetables)):
        text = ax.text(j, i, harvest[i, j],
                       ha="center", va="center", color="black", size=5)


        


ax.set_title("Доля малого и среднего предпринимательства\nв валовом региональном продукте, %\n", size=7)
fig.tight_layout()

####

plt.savefig("High resoltion.png",dpi=1000)
plt.show()

