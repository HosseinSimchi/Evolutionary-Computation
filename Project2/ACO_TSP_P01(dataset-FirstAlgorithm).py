import numpy as np
from collections import Counter

ct = []
for i in range(15):
    ct.append(i+1)
city = ct.copy()

#making distances
dist = [[1  ,29 ,82 ,46 ,  68 ,52   , 72 ,   42    ,    51   ,     55    ,    29,        74,     23 , 72 ,  46],
        [29 , 1 , 55,46 , 42,  43  ,  43    ,  23    ,    23  ,      31   ,     41 ,       51  ,      11 ,     52  ,21],
        [82 , 55,   1 , 68   ,     46     ,   55   ,     23  ,      43  ,      41  ,      29  ,      79 ,       21 ,       64   ,   31 ,51],
        [46 ,  46  , 68,     1    ,    82  ,      15 ,       72   ,     31  ,      62  ,      42 ,       21 ,       51,        51 ,     43, 64],
        [68 ,  42  ,  46, 82     ,    1     ,   74    ,    23  ,      52    ,    21    ,    46    ,    82  ,      58 ,       46 ,     65 ,23],
        [52 ,  43  ,  55,  15  ,74   , 1   , 61 ,23   , 55  ,31   , 33 , 37 ,       51   ,     29, 59],
        [72,   43  ,   23  ,  72   ,     23  ,      61 ,        1  ,      42  ,      23  ,      31 ,       77,       37  ,      51     ,   46 ,  33],
        [42,   23  ,   43  ,   31  ,      52  ,      23  ,      42  ,       1 ,       33  ,      15 ,       37 ,       33 ,       33   ,     31 ,  37],
        [51,   23  ,  41,  62     ,   21     ,   55     ,   23    ,    33      ,   1    ,    29     ,   62    ,    46   ,     29,        5 ,   11],
        [55,    31 ,   29  ,   42  ,      46 ,       31 ,       31 ,       15  ,      29  ,       1  ,      51,        21  ,      41  ,      23 ,   37],
        [29,     41 ,    79 ,     21   ,     82 ,       33  ,      77 ,       37  ,      62   ,     51 ,        1   ,     65 ,       42,        59,    61],
        [74 ,   51 ,   21    , 51   ,     58    ,    37  ,      37    ,    33   ,     46    ,    21    ,    65 ,        1 ,       61  ,      11 ,    55],
        [23 , 11,  64   , 51     ,   46       , 51    ,    51   ,     33      ,  29     ,   41    ,    42,        61    ,     1,        62 ,   23],
        [72 ,  52  ,    31  , 43  ,      65,        29   ,     46 ,       31  ,      51  ,      23     ,   59   ,     11,        62  ,       1 ,  59],
       [46 ,  21,   51  , 64   ,     23    ,    59   ,     33    ,    37     ,   11  ,      37 ,       61  ,      55     ,   23 ,       59  ,   1]]

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
print("P01 On First algorithm")
print(T_cost)
