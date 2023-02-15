import numpy as np
from collections import Counter

ct = []
for i in range(26):
    ct.append(i+1)
city = ct.copy()

#making distances
dist = [ [1 , 83,  93 ,129 ,133 ,139 ,151 ,169 ,135 ,114, 110 ,98 , 99,  95 , 81 ,152, 159, 181 ,172 ,185, 147 ,157 ,185 ,220, 127 ,181],
  [83 ,  1,  40 , 53,  62,  64,  91 ,116,  93,  84,  95,  98,  89 , 68 , 67 ,127 ,156 ,175, 152, 165, 160 ,180 ,223, 268 ,179, 197],
  [93 , 40 ,  1 , 42 , 42,  49,  59,  81,  54,  44,  58,  64 , 54 , 31  ,36  ,86 ,117 ,135, 112 ,125 ,124, 147, 193, 241 ,157, 161],
 [129,  53 , 42 ,  1 , 11 , 11,  46,  72,  65,  70,  88, 100  ,89  ,66  ,76 ,102, 142 ,156 ,127 ,139, 155, 180, 228, 278, 197, 190],
 [133  ,62 , 42  ,11  , 1  , 9 , 35 , 61 , 55 , 62 , 82  ,95 , 84  ,62 , 74 , 93, 133, 146, 117, 128 ,148 ,173, 222 ,272 ,194, 182],
 [139  ,64,  49 , 11 ,  9 ,  1,  39,  65 , 63,  71,  90, 103 , 92 , 71 , 82, 100 ,141, 153 ,124, 135, 156, 181, 230, 280 ,202, 190],
 [151  ,91 , 59 , 46 , 35  ,39  , 1  ,26,  34 , 52 , 71 , 88  ,77  ,63  ,78,  66 ,110, 119 , 88 , 98 ,130 ,156, 206,257 ,188, 160],
 [169 ,116,  81,  72 , 61 , 65 , 26 ,  1 , 37,  59,  75,  92  ,83  ,76  ,91  ,54 , 98 ,103  ,70 , 78 ,122 ,148 ,198, 250 ,188, 148],
 [135 , 93 , 54,  65 , 55 , 63 , 34 , 37  , 1 , 22  ,39 , 56  ,47 , 40  ,55  ,37  ,78  ,91  ,62  ,74  ,96, 122, 172 ,223 ,155 ,128],
 [114 , 84,  44  ,70 , 62 , 71  ,52 , 59 , 22,   1  ,20  ,36  ,26 , 20 , 34 , 43  ,74 , 91 , 68,  82,  86, 111 ,160 ,210 ,136, 121],
 [110 , 95,  58 , 88 , 82  ,90 , 71,  75 , 39 , 20,   1 , 18  ,11 , 27 , 32  ,42 , 61  ,80  ,64 , 77  ,68 , 92 ,140 ,190 ,116 ,103],
  [98  ,98,  64, 100 , 95, 103,  88,  92,  56 , 36 , 18,   1,  11  ,34  ,31 , 56 , 63 , 85 , 75 , 87 , 62 , 83 ,129, 178, 100  ,99],
  [99 , 89,  54,  89 , 84,  92 , 77 , 83,  47,  26,  11,  11  , 1 , 23,  24 , 53,  68 , 89  ,74,  87 , 71 , 93 ,140 ,189, 111 ,107],
  [95  ,68 , 31,  66 , 62,  71 , 63,  76 , 40 , 20,  27 , 34 , 23 ,  1 , 15 , 62 , 87, 106 , 87 ,100,  93, 116 ,163 ,212, 132 ,130],
  [81 ,67 , 36,  76 , 74,  82 , 78  ,91  ,55 , 34 , 32 , 31 , 24 , 15,   1 , 73 , 92 ,112 , 96, 109 , 93, 113, 158,205 ,122 ,130],
 [152, 127 , 86 ,102 , 93, 100 , 66 , 54  ,37  ,43  ,42 , 56  ,53,  62 , 73,   1 , 44 , 54 , 26 , 39 , 68 , 94, 144 ,196, 139,  95],
 [159 ,156 ,117 ,142, 133 ,141 ,110  ,98 , 78 , 74  ,61  ,63,  68 , 87  ,92,  44  , 1  ,22,  34 , 38,  30,  53 ,102, 154 ,109  ,51],
 [181 ,175 ,135 ,156 ,146 ,153 ,119 ,103  ,91  ,91  ,80  ,85  ,89 ,106 ,112  ,54  ,22 ,  1  ,33 , 29  ,46 , 64 ,107 ,157 ,125 , 51],
 [172 ,152 ,112 ,127 ,117 ,124 , 88 , 70 , 62  ,68  ,64 , 75  ,74,  87  ,96  ,26 , 34,  33 ,  1  ,13 , 63  ,87 ,135, 186, 141,  81],
 [185 ,165 ,125 ,139 ,128 ,135 , 98  ,78 , 74  ,82 , 77 , 87 , 87, 100, 109 , 39,  38 , 29  ,13   ,1  ,68  ,90 ,136, 186 ,148  ,79],
 [147 ,160 ,124 ,155 ,148 ,156 ,130 ,122 , 96  ,86  ,68 , 62  ,71,  93 , 93,  68  ,30 , 46 , 63 , 68  , 1 , 26  ,77, 128 , 80,  37],
 [157 ,180 ,147 ,180 ,173 ,181 ,156 ,148 ,122 ,111  ,92  ,83  ,93 ,116 ,113,  94 , 53 , 64 , 87 , 90,  26 ,  1 , 50, 102 , 65 , 27],
 [185 ,223 ,193, 228 ,222 ,230 ,206 ,198 ,172 ,160 ,140 ,129, 140, 163 ,158, 144, 102, 107, 135, 136,  77,  50,   1,  51,  64,  58],
 [220 ,268 ,241 ,278, 272 ,280 ,257 ,250 ,223 ,210 ,190 ,178 ,89 ,212, 205, 196, 154, 157, 186, 186, 128, 102,  51,   1,  93, 107],
 [127 ,179 ,157 ,197 ,194 ,202 ,188 ,188 ,155 ,136 ,116 ,100, 111, 132, 122, 139, 109, 125, 141, 148,  80,  65,  64,  93,   1,  90],
 [181 ,197 ,161 ,190 ,182 ,190 ,160 ,148 ,128 ,121 ,103  ,99, 107, 130, 130,  95 , 51,  51,  81,  79,  37,  27,  58, 107,  90,   1]]

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
        new_ph = 0.8*phr + (phr/dis)
        ph[num-1][num1-1] = new_ph
    num = road[len(road) - 1]
    num1 = road[0]
    phr = ph[num-1][num1-1]    
    dis = dist[num-1][num1-1]
    new_ph = 0.8 * phr + (phr/dis)
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
