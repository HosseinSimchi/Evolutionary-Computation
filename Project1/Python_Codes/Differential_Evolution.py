import numpy as np
import math
def func(x,n):
    r = 10*n + (x**2 - 10 * np.cos(2 * math.pi * x))
    return r
def sumfunc (lis):
    summ = 0 
    for x in lis:
        ans = func(x,n)
        summ = summ + ans
    return summ
n = 2
li = []
bounds = [(-5.12, 5.12)] * n
dimensions = len(bounds)
def DE (pop_list):
    global li
    pop_denorm = pop_list
    n1 = np.random.randint(len(pop_denorm))
    n2 = np.random.randint(len(pop_denorm))
    v1 = pop_denorm[n1]
    v2 = pop_denorm[n2]
    v3 = v1 - v2
    mut = 0.1 * v3
    pop_denorm2 = []
    for i in range(len(pop_denorm)):
            pop_denorm2.append(pop_denorm[i] + mut)
    #--------------------------------------------------------------------------
    num = []
    for i in range(8):
        nn = np.random.randint(0,19)
        num.append(nn)
    n3 = np.random.randint(0,n)
    pop_denorm0 = pop_denorm.copy()
    for i in num:
        pop_denorm[i][n3] = pop_denorm2[i][n3]
    #----------------------------------------------------
    fitness1 = []
    fitness2 = []
    for i in range(len(pop_denorm)):
        ans = sumfunc(pop_denorm[i])
        fitness1.append(ans)
    for i in range(len(pop_denorm0)):
        ans = sumfunc(pop_denorm0[i])
        fitness2.append(ans)
    fit = []
    for i in range(len(fitness1)):
        fit.append(fitness1[i] - fitness2[i])
    pop_denorm3 = pop_denorm.copy()
    for i in fit:
        if i != 0 :
            if i > 0 :
                index = fit.index(i)
                pop_denorm[index] = pop_denorm0[index].copy()
    fitness3 = []
    for i in range(len(pop_denorm)):
        ans = sumfunc(pop_denorm[i])
        fitness3.append(ans)
    print(min(fitness3))
    li.append(min(fitness3))
    return pop_denorm,li


pop = np.random.rand(20, dimensions)
min_b, max_b = np.asarray(bounds).T
diff = np.fabs(min_b - max_b)
pop_denorm = min_b + pop * diff

for i in range(200):
    pop_denorm,li = DE(pop_denorm)
import matplotlib.pyplot as plt
xl = []
for i in range(200):
    xl.append(i+1)
plt.plot(xl,li)
plt.ylabel('Fitness')
plt.xlabel('Iteration')
plt.title('Differential Evolution (Hossein Simchi, 98443119)')
plt.show()
