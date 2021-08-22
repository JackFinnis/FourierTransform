import os
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"
import matplotlib.pyplot as plt

from fourier import transform
from path import getPath

path = getPath('photos/run.jpg')


while True:
    N = int(input('\nNumber of epicycles:\n> '))
    approx_x, approx_y = transform(N, path)

    plt.clf()
    plt.plot(approx_x, approx_y)
    plt.gca().set_aspect('equal')
    plt.axis('off')
    plt.savefig('out.jpg', bbox_inches='tight')