import numpy as np
from collections import Counter

ct = []
for i in range(5):
    ct.append(i+1)
city = ct.copy()

#making distances
dist = [[1 , 3 , 4 , 2 , 7],[3 , 1 , 4 , 6 , 3],[4 , 4 , 1 , 5 , 8],[2 , 6 , 5 ,1 , 6],[7 , 3 , 8 , 6 , 1]]

#phromone
ph = []
for i in range(len(city)):
    ds = []
    for j in range(len(city)):
        ds.append(1)
    ph.append(ds)

    
def g_r_path(City,City1,road):
    i = 0
    city1 = City1
    city = City
    froad = []
    b = len(city)/2
    while(i<b):
        n1 = np.random.randint(len(city)) 
        if i == 0 :
            if len(city1) == 1:
                n2 = city1[0]
                froad.append(n2)
                city.remove(n2)
                i = i + 1
            else : 
                n2 = np.random.randint(len(city1))
                froad.append(city1[n2])
                city1.remove(city1[n2])
                city.remove(city[n2])
                i = i + 1
        else :
            froad.append(city[n1])
            city.remove(city[n1])
            i = i + 1
    return froad,city1
roads = ['Roads']
def run():
    global ct
    city = ct.copy()
    city1 = ct.copy()
    for k in range(len(ct)):
        path,city1 = g_r_path(city,city1,roads)
        city = ct.copy()
        roads.append(path)
    return roads
roads = run()
paths = []
def run1(): #Article_ACO_TSP
    global roads,ct
    city = ct.copy()
    for i in range(10000):
        n3 = np.random.randint(1,len(roads))
        n4 = np.random.randint(1,len(roads))
        r3 = []
        r1 = roads[n3]
        r2 = roads[n4]
        c = 0
        while (c<len(r1)):
            r3.append(r1[c])
            c = c + 1
        c = 0
        while (c < len(r2)):
            r3.append(r2[c])
            c = c + 1
        l = Counter(r3).keys()
        if len(l) == len(city):
            paths.append(r3)
    if len(paths) > 3 :
        return paths
    else : 
        for u in range(1,len(roads)):
            city = ct.copy()
            list1 = roads[u]
            city = list(set(city) - set(list1))
            r = 0
            while (r<len(city)):
                n = np.random.randint(len(city))
                roads[u].append(city[n])
                city.remove(city[n])
            city2 = ct.copy()
            l = Counter(roads[u]).keys()
            if len(l) == len(city2):
                paths.append(roads[u])
        return paths
                

def Road(roads,distance,phromone):
    road = roads
    dist = distance
    ph = phromone
    for i in range(len(road)-1):
        num = road[i]
        num1 = road[i+1]
        phr = ph[num-1][num1-1]
        dis = dist[num-1][num1-1]
        new_ph = 0.5*phr + (phr/dis)
        ph[num-1][num1-1] = new_ph
    num = road[len(road) - 1]
    num1 = road[0]
    phr = ph[num-1][num1-1]    
    dis = dist[num-1][num1-1]
    new_ph = 0.5 * phr + (phr/dis)
    ph[num-1][num1-1] = new_ph
    return ph

for q in range(3):
    paths = []
    roads = run()
    paths = run1()
    for i in range(len(paths)):
        ph = Road(paths[i],dist,ph)
for i in range(len(ph)):
    ph[i][i] = 0



def Ph(phromone,b):
    ph = phromone
    paths = []
    path = []
    for n in range(1,len(ph)):
        path.append(n)
        li = ph[n-1] 
        index = li.index(max(li))
        for j in range(b-1):
            for z in range(2,len(li)):
                if (index+1) in path:
                    index = li.index(sorted(set(li))[-z])
                else :
                    path.append(index+1)
                    li = ph[index]
        paths.append(path)
        path = []
    return paths

ro = []
path = Ph(ph,b=int(len(ph)/2))
for i in path :
    l = Counter(i).keys()
    if len(l) == int(len(ct)/2):
        ro.append(i)

for i in range(len(ro)):
    ph = Road(ro[i],dist,ph)
path = Ph(ph,b=int(len(ph)))
ro1 = []
for i in path :
    l = Counter(i).keys()
    if len(l) == int(len(ct)):
        ro1.append(i)
print(ro1)         
def costs(roads,distance):
    road = roads
    dist = distance
    t_cost = 0
    for i in range(len(road)-1):
        num = road[i]
        num1 = road[i+1]
        cost = dist[num-1][num1-1]
        t_cost = t_cost + cost
    num = road[len(city) - 1]
    num1 = road[0]
    cost = dist[num-1][num1-1]
    t_cost = t_cost + cost
    return t_cost
T_cost = []
for i in ro1:
    cost = costs(i,dist)
    T_cost.append(cost)
print(T_cost)
