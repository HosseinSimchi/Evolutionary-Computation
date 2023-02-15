import numpy as np
import math
import copy

def func(x,n):
    r = 10*n + (x**2 - 10 * np.cos(2 * math.pi * x))
    return r
def sumfunc (lis):
    summ = 0 
    for x in lis:
        ans = func(x,n)
        summ = summ + ans
    return summ
def velocity(x,y,z,v,ph1,ph2):
    v = ( 0.4 * v ) + (ph1*0.3*(y-x)) + (ph2*0.7*(z-x))
    return v
n = 20
bounds = [(-5.12, 5.12)] * n
dimensions = len(bounds)
li = []
def PSO (pop_list,z):
    global li
    pop_denorm = pop_list
    pop_denorm2 = copy.deepcopy(pop_denorm)
    fit0 = []
    for i in range(len(pop_denorm)):
        ans = sumfunc(pop_denorm[i])
        fit0.append(ans)
    ind = fit0.index(min(fit0))
    ph1 = np.random.randint(0,3)
    ph2 = np.random.randint(0,3)
    y = pop_denorm[ind]
    c = 0
    for i in z:
        if i == 1:
            c = c + 1
    if c == 4 :
        z = y.copy()
    for i in range(len(pop_denorm)):
        for j in range(20):
            pop_denorm[i][j] = pop_denorm[i][j] + velocity(pop_denorm[i][j],y[j],z[j],1,ph1,ph2)
    pop_denorm3 = []
    for i in range(len(pop_denorm2)):
        pop_denorm3.append(pop_denorm2[i])
    for i in range(len(pop_denorm)):
        pop_denorm3.append(pop_denorm[i])
    fit1 = []
    for i in range(len(pop_denorm3)):
        ans = sumfunc(pop_denorm3[i])
        fit1.append(ans)
    gen = []
    for i in range(20):
        index = fit1.index(min(fit1))
        gen.append(pop_denorm3[index])
        fit1[index] = 100000000
    fit2 = []
    for i in range(len(gen)):
        ans = sumfunc(gen[i])
        fit2.append(ans)
    idx = fit2.index(min(fit2))
    best = gen[idx]
    bs = min(fit2)
    li.append(bs)
    return best,gen,bs,li

z = [1,1,1,1]
pop = np.random.rand(20, dimensions)
min_b, max_b = np.asarray(bounds).T
diff = np.fabs(min_b - max_b)
pop_denorm = min_b + pop * diff
for i in range(200):
    best,gen,bs,li = PSO(pop_denorm,z)
    z = best
    pop_denorm = gen
    if i == 199:
        print("The best parameters are : {0} and the best solution is {1}".format(best,bs))
        
import matplotlib.pyplot as plt
xl = []
for i in range(200):
    xl.append(i+1)
plt.plot(xl,li)
plt.ylabel('Fitness')
plt.xlabel('Iteration')
plt.title('PSO (Hossein Simchi, 98443119)')
plt.show()
