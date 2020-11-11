#Задание 1
#Создайте numpy array с элементами от числа N до 0
#(например, для N = 10 это будет array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])).

import numpy as np
N=int(input())
x=np.arange(N-1, -1, -1)
print(x)

#Задание 2
#Создайте диагональную матрицу с элементами от N до 0.
#Посчитайте сумму ее значений на диагонали.

N=int(input())
mat=np.diag(np.arange(N-1, -1, -1)) 
print(mat)

#Решите систему уравнений:
#4x + 2y + z = 4
#x + 3y = 12
#5y + 4z = -3

from numpy import linalg
a=np.array([[4, 2, 1], [2, 3, 1], [0, 5, 4]])
b=np.array([4, 12, -3])
print(linalg.solve(a, b))

##Найдите самого похожего пользователя.
##Т. е. посчитайте косинусное сходство между этим пользователем
##и всеми пользователями из массива user_stats

from scipy import spatial
import numpy as np

users_stats = np.array(
    [
        [2, 1, 0, 0, 0, 0],
        [1, 1, 2, 1, 0, 0],
        [2, 0, 1, 0, 0, 0],
        [1, 1, 2, 1, 0, 1],
        [0, 0, 1, 2, 0, 0],
        [0, 0, 0, 0, 0, 5],
        [1, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 3],
        [1, 0, 0, 2, 1, 4]
    ], 
    np.int32
)

next_user_stats = np.array([0, 1, 2, 0, 0, 0])

for number_users_stats in users_stats:
    result = 1 - spatial.distance.cosine(next_user_stats, number_users_stats)
    print(result)
