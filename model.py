import random
import operator
import matplotlib
matplotlib.use('TkAgg')
import tkinter
import matplotlib.pyplot
import agentframework
import csv 
import matplotlib.animation 
import wolfclass


def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) + 
    ((agents_row_a.y - agents_row_b.y)**2))**0.5
            
def remove_dead(self):
# Remove all dead agents
    self.agents[:] = [x for x in self.agents if x.type != 'Dead']

num_of_agents = 10
frame_number = 50
neighbourhood = 20
agents = []
environment = []
wolves = []
g = 'Sheep'

fig = matplotlib.pyplot.figure(figsize=(7, 7))
#ax = fig.add_axes([0, 0, 1, 1])


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
    agents.append(agentframework.Agent(environment, agents, wolves))
    wolves.append(wolfclass.Wolf(environment, agents, wolves))
    
    agents[i].share_with_neighbours(neighbourhood, agents)

# Move the agents.
def update (frame_number):

    for i in range (frame_number):
        fig.clear()
        for j in range(num_of_agents):

            random.shuffle(agents)
            remove_dead(agents)
            
            agents[j].move()
            wolves[j].move()
            
            agents[j].eat()
            
            agents[j].check_status()
            
            agents[j].share_with_neighbours(neighbourhood, agents)
            wolves[j].share_with_neighbours(neighbourhood, agents)
            matplotlib.pyplot.imshow(environment, vmin = 0, vmax = 250)
            
        for k in range(0,len(agents)):
                        
            matplotlib.pyplot.scatter(agents[k].x,agents[k].y, marker="D",  color='white')

            
        for k in range(0,len(wolves)):
            matplotlib.pyplot.scatter(wolves[k].x,wolves[k].y, marker="D",  color='grey')

            matplotlib.pyplot.show()

   

animation = matplotlib.animation.FuncAnimation(fig, update, frames=frame_number, repeat=False)
#canvas.show() 