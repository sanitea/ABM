import random
import operator
import matplotlib.pyplot
import agentframework
import csv 
import matplotlib.animation 

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) + 
    ((agents_row_a.y - agents_row_b.y)**2))**0.5

num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
#a = agentframework.Agent([])
agents = []
environment = []

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#Environment. Empty row, append rowlist to environment, append rowlist. 
f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:	
    rowlist = [] 
    environment.append(rowlist)
    for value in row:
        rowlist.append(value)					
f.close() 

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment))
    agents[i].share_with_neighbours(neighbourhood, agents)

# Move the agents.
for i in range (num_of_iterations):
    for j in range(num_of_agents):
        agents[j].move()
        agents[j].eat()
        agents[j].share_with_neighbours(neighbourhood, agents)
        
        animation = matplotlib.animation.FuncAnimation(fig, num_of_iterations, interval=1, repeat=False, frames=num_of_iterations)
        matplotlib.pyplot.show(animation)


#Find out the distances of the agents and don't compare same item to same item 
for agents_row_a in agents:
    for agents_row_b in agents:
        if agents_row_a != agents_row_b:
            distance = distance_between(agents_row_a, agents_row_b)
            print (agents_row_a, agents_row_b)
        else: 
            print ("Snap")

#Show environment 
matplotlib.pyplot.xlim(0, 100)
matplotlib.pyplot.ylim(0, 100)
matplotlib.pyplot.imshow(environment)
#for i in range(num_of_agents):
 #   matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
