import numpy as np
from collections import Counter

ct = []
for i in range(17):
    ct.append(i+1)
city = ct.copy()

#making distances
dist =[  [1 ,633 ,257  ,91 ,412 ,150  ,80 ,134 ,259 ,505 ,353 ,324  ,70 ,211 ,268 ,246 ,121],
[633 ,  1 ,390 ,661 ,227, 488, 572, 530 ,555, 289, 282, 638, 567 ,466 ,420 ,745 ,518],
[257 ,390 ,  1 ,228 ,169, 112, 196 ,154 ,372 ,262 ,110 ,437 ,191  ,74  ,53 ,472 ,142],
[ 91 ,661 ,228 ,  1 ,383, 120,  77 ,105 ,175 ,476 ,324 ,240  ,27 ,182 ,239 ,237  ,84],
[412 ,227 ,169 ,383 ,  1, 267, 351 ,309 ,338 ,196  ,61 ,421 ,346 ,243 ,199 ,528 ,297],
[150 ,488 ,112 ,120 ,267,   1,  63 , 34 ,264 ,360 ,208 ,329,  83 ,105 ,123 ,364  ,35],
[ 80 ,572 ,196 , 77 ,351 , 63,   1 , 29 ,232 ,444 ,292 ,297  ,47 ,150 ,207 ,332  ,29],
[134 ,530 ,154 ,105 ,309 , 34,  29 ,  1 ,249 ,402 ,250 ,314 ,68 ,108 ,165 ,349  ,36],
[259 ,555 ,372 ,175 ,338 ,264, 232 ,249 ,  1 ,495 ,352 , 95 ,189 ,326 ,383 ,202 ,236],
[505 ,289 ,262 ,476 ,196 ,360, 444 ,402 ,495 ,  1 ,154 ,578, 439 ,336 ,240 ,685 ,390],
[353 ,282 ,110 ,324 , 61 ,208, 292 ,250 ,352 ,154 ,  1 ,435, 287 ,184 ,140 ,542 ,238],
[324 ,638 ,437 ,240 ,421 ,329, 297 ,314 , 95 ,578 ,435 ,  1, 254 ,391 ,448 ,157 ,301],
 [70 ,567 ,191 , 27 ,346 , 83,  47 , 68 ,189 ,439 ,287 ,254,   1 ,145 ,202 ,289  ,55],
[211 ,466 , 74 ,182 ,243 ,105, 150 ,108 ,326 ,336 ,184 ,391, 145  , 1  ,57 ,426  ,96],
[268 ,420 , 53 ,239 ,199 ,123, 207 ,165 ,383 ,240 ,140 ,448, 202  ,57  , 1 ,483 ,153],
[246 ,745 ,472 ,237 ,528 ,364, 332 ,349 ,202 ,685 ,542 ,157, 289 ,426 ,483  , 1 ,336],
[121 ,518 ,142 , 84 ,297 , 35 , 29 , 36 ,236 ,390 ,238 ,301,  55 , 96 ,153 ,336  , 1 ]]

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
        new_ph = 0.9*phr + (phr/dis)
        ph[num-1][num1-1] = new_ph
    num = road[len(road) - 1]
    num1 = road[0]
    phr = ph[num-1][num1-1]    
    dis = dist[num-1][num1-1]
    new_ph = 0.9 * phr + (phr/dis)
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
print("GR17 On First algorithm")
print(T_cost)
