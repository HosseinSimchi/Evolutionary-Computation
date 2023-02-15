import numpy as np
import math
import copy

def func(x):
    r = 1 + (x**2)/4000
    return r
def sumfunc (lis):
    summ = 0 
    cs = 1
    i = 1
    for x in lis:
        ans = func(x)
        cs = cs * (np.cos(x)/i)
        summ = summ + ans - cs
        i = i + 1
    return summ
def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

n = 4
li = []
bounds = [(-100, 100)] * n
dimensions = len(bounds)
def ES (pop_list,sigma1):
    global li
    pop_denorm = pop_list
    pop_denorm0 = copy.deepcopy(pop_denorm)
    #Recombination
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
    gen = []
    for i in range(len(pop_denorm)):
        ans1 = sumfunc(pop_denorm1[i])
        ans2 = sumfunc(pop_denorm[i])
        if ans1 > ans2:
            gen.append(pop_denorm[i])
        else :
            gen.append(pop_denorm1[i])
    fitness = []
    for i in range(len(gen)):
        ans = sumfunc(gen[i])
        fitness.append(ans)
    gen1 = []
    for i in range(20):
        mini = fitness.index(min(fitness))
        gen1.append(gen[mini])
        fitness[mini] = 20000000
    fitness1 = []
    fitness2 = []
    for i in range(len(pop_denorm0)):
        ans = sumfunc(pop_denorm0[i])
        fitness1.append(ans)
    for i in range(len(gen1)):
        ans = sumfunc(gen1[i])
        fitness2.append(ans)
    fitt = []
    for i in range(len(fitness1)):
        fitt.append(fitness1[i] - fitness2[i])
    positive = []
    for i in fitt:
        if i > 0 :
            positive.append(i)
    leng = float(len(positive)/len(fitt))
    fi = []
    for i in range(len(gen1)):
        ans = sumfunc(gen[i])
        fi.append(ans)
    print(min(fi))
    li.append(min(fi))
    return gen1,leng,sigma1,li

        
        
pop = np.random.rand(20, dimensions)
min_b, max_b = np.asarray(bounds).T
diff = np.fabs(min_b - max_b)
pop_denorm = min_b + pop * diff
pop_denorm = list(pop_denorm)
sigma1 = 1
n = np.random.uniform(0.8,1)
for i in range(200):
    gen1,leng,sigma1,li = ES(pop_denorm,sigma1)
    if leng > 0.20 :
        sigma1 = float(sigma1 / n)
    else :
        sigma1 = float(sigma1 * n)   
    pop_denorm = gen1
    
import matplotlib.pyplot as plt
xl = []
for i in range(200):
    xl.append(i+1)
plt.plot(xl,li)
plt.ylabel('Fitness')
plt.xlabel('Iteration')
plt.title('Evolution Estrategies (Hossein Simchi, 98443119) >>> Cross:Intermediate , SS : (Mu + landa)')
plt.show()
