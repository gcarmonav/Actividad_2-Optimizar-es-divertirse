# -*- coding: utf-8 -*-

import imageio
import numpy as np
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt

x=[-0.06,0.55,0.53,0.55,0.83,0.57,-0.19,0.08,0.60,0.42]
y=[1.82,2.40,2.38,2.40,2.71,2.44,1.36,1.75,2.59,2.53]

p_x=np.empty([6,2])
p_y=np.empty([6,2])
p_x[0,:]=[-0.1901380, -0.0624039]
p_x[1,:]=[ 0.4180140, 0.7062903]
p_x[2,:]=[0.09130077, 0.42442010]
p_x[3,:]=[-0.04963433, 0.83441312]
p_x[4,:]=[-0.1713510, 0.6166043]
p_x[5,:]=[-0.1777572,  0.8408193]

p_y[0,:]=[1.346394, 1.807585]
p_y[1,:]=[2.531522, 2.630169]
p_y[2,:]=[1.742348, 2.515081]
p_y[3,:]=[1.824553, 2.712375]
p_y[4,:]=[1.355981, 2.597287]
p_y[5,:]=[1.388863, 2.728816]

it=0
filenames = []
p = np.linspace(-0.19,2.048,10)
for i in range(0,6):
    for j in range(0,6):
        X=np.empty([2,1])
        g=np.empty([10,1])
        X[0],X[1]=p_x[i,0],p_x[i,1],
        Y=np.array(p_y[i,:])
        m=(Y[1]-Y[0])/(X[1]-(X[0]))
        c=Y[1]-(X[1]*m)
        r='y= '+ str(round(m[0], 2)) +'x + '+ str(round(c[0], 3))
        model = LinearRegression()
        model.fit(X,Y)
        g[:,0]=x
        predictions = model.predict(g)
        plt.xlim(-0.3, 0.9)
        plt.ylim(1.2 , 2.85)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.suptitle('X vs Y',fontsize=18)
        plt.title(r,loc='left')
        plt.plot(x,y,'o',color='black')
        plt.plot(x, predictions, '-',color='r')
        filename = f'{it}.png'
        filenames.append(filename)
        plt.savefig(filename)
        plt.clf()
        it=it+1
    
with imageio.get_writer('Al_ojo_1.gif', mode='I') as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)


