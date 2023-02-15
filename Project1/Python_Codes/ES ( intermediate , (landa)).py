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
def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

n = 4
li = []
bounds = [(-5.12, 5.12)] * n
dimensions = len(bounds)
def ES (pop_list,sigma1):
    global li
    pop_denorm = pop_list
    pop_denorm0 = copy.deepcopy(pop_denorm)
    #Parent Selection
    num = []
    for i in range(10):
        num.append(np.random.randint(0,19))
    ps = []
    for i in num:
        ps.append(pop_denorm[i])
    ch1 = []
    for i in range(len(ps)):
        if (i+1) != len(ps):
            ans1 = ps[i]
            ans2 = ps[i+1]
            ch = []
            for j in range(len(ans1)):
                ch.append((ps[i][j] + ps[i+1][j])/2)
            ch1.append(ch)

    for i in range(len(ch1)):
        pop_denorm.append(ch1[i])
    
    pop_denorm1 = copy.deepcopy(pop_denorm)
    #Mutation 
    for i in range(len(pop_denorm)):
        for j in range(4):
            x = pop_denorm[i][j]
            sig = sigma1
            mu = 0
            mut = gaussian(x,mu,sig)
            pop_denorm[i][j] = pop_denorm[i][j] + mut
    fitness1 = []
    for i in range(len(pop_denorm)):
        ans = sumfunc(pop_denorm[i])
        fitness1.append(ans)
    fitness2 = []
    for i in range(len(pop_denorm1)):
        ans = sumfunc(pop_denorm1[i])
        fitness2.append(ans)
    fitt = []
    for i in range(len(fitness1)):
        fitt.append(fitness1[i] - fitness2[i])
    negative = []
    for i in fitt:
        if i < 0 :
            negative.append(i)
    leng = float(len(negative)/len(fitt))
    print(min(fitness1))
    li.append(min(fitness1))
    return pop_denorm,leng,sigma1,li

        
        
pop = np.random.rand(20, dimensions)
min_b, max_b = np.asarray(bounds).T
diff = np.fabs(min_b - max_b)
pop_denorm = min_b + pop * diff
pop_denorm = list(pop_denorm)
sigma1 = 1
n2 = np.random.uniform(0.8,1)
for i in range(200):
    gen1,leng,sigma1,li = ES(pop_denorm,sigma1)
    if leng > 0.20 :
        sigma1 = float(sigma1 / n2)
    else :
        sigma1 = float(sigma1 * n2)   
    pop_denorm = gen1
    
import matplotlib.pyplot as plt
xl = []
for i in range(200):
    xl.append(i+1)
plt.plot(xl,li)
plt.ylabel('Fitness')
plt.xlabel('Iteration')
plt.title('Evolution Estrategies (Hossein Simchi, 98443119) >>> Cross:Intermediate , SS : (landa)')
plt.show()
