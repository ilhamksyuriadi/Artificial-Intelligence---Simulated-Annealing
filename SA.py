import random
from math import exp
Tmax = 10000000000
Tmin = 0.000001

a = 0.99
x1 = random.uniform(-10,10)
x2 = random.uniform(-10,10)

def f(x1,x2):
    return (4 - 2.1 * x1**2 + x1**4 / 3) * x1**2 + x1 * x2 + (-4 + 4 * x2**2) * x2**2

def prob(current, new, T):
    return exp((current - new)/T)

current = f(x1,x2)

while (Tmax > Tmin):
    for i in range (1,100):
        x1,x2 = random.uniform(-1,1), random.uniform(-1,1)
        new = f(x1,x2)
        if (prob(current,new,Tmax) > random.random()):
            current = new

    Tmax = Tmax * a

print("x1 = ",x1)
print("x2 = ",x2)
print("hasil = ",current)