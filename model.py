import random 
import operator 
import matplotlib.pyplot

#function 
def distance_between(agents_row_a, agents_row_b):
    answer = ((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2)**0.5
    return answer
    print (agents_row_a)
    print (agents_row_b)

#Variables 
num_of_agents = 10
num_of_interations = 100
agents = []

#Agents instanciating  
for i in range (num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])

#Agents Moving 
for j in range (num_of_interations):
    for i in range (num_of_agents):
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100
            
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100 

#Distance. Put this in function distance_between 
for i in range (0,num_of_agents):
    for j in range (i,num_of_agents):
        distance = distance_between(agents[i], agents[j])
        print (distance)