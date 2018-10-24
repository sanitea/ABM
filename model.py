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
frame_number = 50
neighbourhood = 5
agents = []
environment = []

fig = matplotlib.pyplot.figure(figsize=(15, 15))
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
    random.shuffle(agents)
    agents[i].share_with_neighbours(neighbourhood, agents)

# Move the agents.
def update (frame_number):
    for i in range (frame_number):
        for j in range(num_of_agents):
            fig.clear()
            random.shuffle(agents)
            agents[j].move()
            agents[j].eat()
            agents[j].share_with_neighbours(neighbourhood, agents)
            matplotlib.pyplot.imshow(environment)
        for k in range(0,len(agents)):
            matplotlib.pyplot.scatter(agents[k].x,agents[k].y)


#Find out the distances of the agents and don't compare same item to same item 
for agents_row_a in agents:
    for agents_row_b in agents:
        if agents_row_a != agents_row_b:
            distance = distance_between(agents_row_a, agents_row_b)
           # print (agents_row_a, agents_row_b)
       # else: 
           # print ("Snap")


animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, frames=frame_number, repeat=False)
#matplotlib.pyplot.show()
