from os import posix_fadvise, readlink
from typing import Sized
import numpy as np
import matplotlib.pyplot as plt
import collections


with open('Part4.csv') as f:
    next(f) # Skip the first line
    # print("most 7 pair ip in network ==> " , collections.Counter(line for line in f).most_common(7) )
    pair_ips  = collections.Counter(line for line in f).most_common(6000)

# print(len(pair_ips))

array_ips  = []
for tpl in pair_ips:
    array_ips.append(tpl[0].split(',')[0])
    array_ips.append(tpl[0].split(',')[1].split('"\\"')[0])

array_ips = list(dict.fromkeys(array_ips))
x_array = []
y_array = []
for ip in array_ips:
    a = int(ip.split('.')[0])
    b = int(ip.split('.')[1])
    c = int(ip.split('.')[2])
    d = int(ip.split('.')[3])
    x = a*256 + b
    y = c*256 + d
    x_array.append(x)
    y_array.append(y)

for tpl in range(0 , len(pair_ips) , 20):
    # print(pair_ips[tpl])
    # print()

    src_index = array_ips.index(pair_ips[tpl][0].split(',')[0])
    dst_index = array_ips.index(pair_ips[tpl][0].split(',')[1].split('"\\"')[0])
    x = []
    y = []
    x.append(x_array[src_index])
    x.append(x_array[dst_index])
    y.append(y_array[src_index])
    y.append(y_array[dst_index])
    plt.plot(x, y, 'k--o' , linewidth=0.5 , markerfacecolor='red' , markersize=5 )
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Slammer Worm Detection')

# plt.grid(True)

plt.show()

# print(pair_ips[0][0].split(','))
# print(pair_ips[0][0].split(',')[1].split('"\\"')[0])