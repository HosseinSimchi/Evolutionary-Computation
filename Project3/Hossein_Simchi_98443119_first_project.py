import math
import matplotlib.pyplot as plt
import random

populationSize = 33 	                                	            
iteration = 35	
k = 4        
bagSize = 300	
weightList = [] 
for i in range(20):
  n = random.randint(2,35)       
  weightList.append(n)
print("Random Weight List is : {0}".format(weightList))
randomList = []
for i in range(0,30):
  n = random.uniform(0,1)
  randomList.append(n)

valueList = []
for i in range(20):
  n = random.randint(5,100)       
  valueList.append(n)
print("Random value List is : {0}".format(valueList))
def initialise():  
  population = ""
  populationList = []
  random_index = []
  for x in range(populationSize):
    for r in range(len(weightList)):
      n1 = random.randint(0,29)
      random_index.append(n1)
    for z in range(len(weightList)):
      if (randomList[random_index[z]] < 0.5):
        population += "0"
      else: 
        population += "1"	
    populationList.append(population)
    population = ""
    random_index = []
  return populationList	

populationList = initialise()
print("The First generation of population list is  : {0}".format(populationList))

def evaluate(populationlist):
	sumWeight=0
	sumValue=0
	fitnessList = []
	for i in range(len(populationlist)):
		for j in range(len(populationlist[i])):
			if(populationlist[i][j] == "1"):
				sumWeight += int(weightList[j])
				sumValue += int(valueList[j])
		if(sumWeight <= bagSize):
			fitnessList.append(sumValue)
		else:
			fitnessList.append(0)
		sumWeight=0
		sumValue=0
	return fitnessList
fitnessList = evaluate(populationList)
print("Fitness list for each Chromosome in the population list is : {0}".format(fitnessList))

def parentSelect(fList,pop):
  tempList = []
  populationlist = []
  populationlist = pop
  parentSelectList = []
  for i in range(len(fList)):
    if fList[i] != 0 :
      tempList.append(fList[i])
      parentSelectList.append(populationList[i])
  return parentSelectList

selectedparent = parentSelect(fitnessList,populationList)
print("Selected parents with the most values are : {0}".format(selectedparent))

def recombine(pList):
  childList = []
  for i in range(len(pList)-1):
    index = random.randint(0,len(valueList))
    c1 = pList[i]
    c2 = pList[i+1]
    child1 = c1[:index] + c2[index:]
    child2 = c2[:index] + c1[index:]
    childList.append(child1)
    childList.append(child2)
  return childList
childrens = recombine(selectedparent)
print("children is generated with cross over operation : {0}".format(childrens))

def mutation(cList):
  mutationList = []
  for i in range(k):
    n = random.randint(0,len(cList)-1)
    E = cList[n]
    mutation_index = random.randint(1,len(valueList)-1)
    if E[mutation_index] == '1' :
      r = E[:mutation_index] + '0' + E[mutation_index+1:]
    else:
      r = E[:mutation_index]  + '1' + E[mutation_index+1:]
    mutationList.append(r)
  return mutationList
r = mutation(childrens)
print("random mutation on children is : {0}".format(r))
def new_population(list_n):
  new_pop = []
  if len(list_n) > 33 :
    for i in range (0,populationSize):
      r = random.randint(0,populationSize)
      new_pop.append(list_n[r])
    return new_pop
  else :
    return list_n
new_generation = childrens + r
new_parents = new_population(new_generation)

avg = []
max = []
min = []
i = 0
import numpy as np
while(i < 35):
  fitnn = []
  fitn = evaluate(new_parents)
  for t in fitn :
    if t != 0 :
      fitnn.append(t)
    else:
      continue
  sum = 0
  max.append(np.max(fitnn))
  min.append(np.min(fitnn)) 
  for j in fitnn:
    sum = sum + j
  avg.append(sum/populationSize)
  spa = parentSelect(fitnn,new_parents)
  recom = recombine(spa)
  mut = mutation(recom)
  ngen = recom + mut
  new_parents = new_population(ngen)
  i = i + 1
avg.sort()
max.sort()
min.sort()

it = []
for i in range(1,36):
  it.append(i)

plt.plot(it,min,'o-',c='blue')
plt.plot(it,avg,'s-',c='red')
plt.plot(it,max,'o-',c='brown')
plt.grid(True)		
plt.xlabel('Iterator')
plt.ylabel('Fitness')
plt.legend(["min","avg","max"])
plt.show()
