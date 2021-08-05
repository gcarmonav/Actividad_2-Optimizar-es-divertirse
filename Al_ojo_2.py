# -*- coding: utf-8 -*-

import imageio
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

datos=pd.read_csv('datos_2.csv',sep=';')

x=datos['x']
y=datos['y']
b_0=[-8,-6,-1,-2,-7,-8]
b_1=[5,7,5,9,11,14]
it=0
filenames = []
for i in range(0,6):
    for j in range(0,6):
        eq=1/(1+np.exp(-(b_0[i]+(b_1[i]*x))))
        plt.xlabel('x')
        plt.ylabel('P(Y=1|X=1)')
        plt.title('Curva logística con {} corresponde a [B_0,B_1]'.format([b_0[i],b_1[i]]),fontsize=14)
        plt.plot(x,eq, 'ro')
        filename = f'{it}.png'
        filenames.append(filename)
        plt.savefig(filename)
        plt.clf()
        it=it+1
    
with imageio.get_writer('Al_ojo_2.gif', mode='I') as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)



