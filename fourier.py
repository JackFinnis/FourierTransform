import numpy as np

def integrand(path, t, n):
    return np.exp(n * -2j * np.pi * t/len(path)) * path[t]

def integral(path, n):
    integral = 0
    for t in range(len(path)):
        integral += integrand(path, t, n) * 1/len(path)
    return integral

def getCn(N, path):
    c = {}
    for n in range(-N, N+1):
        c[n] = integral(path, n)
    return c


def vector(cn, t, n):
    return cn * np.exp(n * 2j * np.pi * t)

def getApprox(N, path, c):
    approx = []
    for t in range(len(path)):
        vectorSum = 0
        for n in range(-N, N+1):
            vectorSum += vector(c[n], t/len(path), n)
        approx.append(vectorSum)
    return np.array(approx)


def transform(N, path):
    c = getCn(N, path)
    approx = getApprox(N, path, c)
    return approx.real, approx.imag