import random 
#import operator 
#import matplotlib.pyplot

#function for finding the difference 
def distance_between(agents_row_a, agents_row_b):
    answer = (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5
    return answer
    print (agents_row_a)
    print (agents_row_b)


#Variables 
num_of_agents = 10
num_of_interations = 100
agents = []

#Agents instanciating  
for i in range (num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

#Agents Moving. Modulus operator 
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


#At the moment this loops through the agents, compares them with each other to make sure they aren't the same, then works out the distance        
for agents_row_a in agents:
    for agents_row_b in agents:
        if agents_row_a != agents_row_b:
            distance = distance_between(agents_row_a, agents_row_b)
            print (agents_row_a, agents_row_b)
        else: 
            print ("Snap")
        print (distance)