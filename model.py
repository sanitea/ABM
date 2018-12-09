import random
import operator
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import agentframework
import csv 
import matplotlib.animation 
import wolfclass

#Function to work out the distance between models 
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) + 
    ((agents_row_a.y - agents_row_b.y)**2))**0.5
            
#Variables 
num_of_sheep = 10
num_of_wolves = 2
frame_number = 50
neighbourhood = 10
kill_zone = int 
agents = []
environment = []
wolves = []
dead_sheep = []

#Output variables 
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

# Make the agents, append them to the environment, and then .
for i in range(num_of_sheep):
    agents.append(agentframework.Agent(environment, agents, wolves))
    agents[i].share_with_neighbours(neighbourhood, agents)
    
#Make Wolves
for i in range(num_of_wolves):
    wolves.append(wolfclass.Wolf(environment, agents, wolves))

# Move the agents.
def update (frame_number):

    for i in range (frame_number):
        fig.clear()
        matplotlib.pyplot.imshow(environment, vmin = 0, vmax = 250)
        
        for j in range(num_of_sheep):

            #Shuffle agents to prevent model artifacting 
            random.shuffle(agents)
            
            #Sheep move, eat, and check status 
            agents[len(agents) -1].move()
            agents[len(agents) -1].eat()
            agents[len(agents) -1].check_status()
            
            agents[len(agents) -1].share_with_neighbours(neighbourhood, agents)
            sort_dead(agents)
            
            #Wolves move and share information with neighbours
        for j in range(num_of_wolves):
            wolves[j - 1].move()
            wolves[j - 1].check_for_sheep(neighbourhood, agents)
            
            #Plot living sheep
        for k in range(0,len(agents)):
            matplotlib.pyplot.scatter(agents[k].x,agents[k].y, marker="o",  color='white', label = 'sheep')
            
            #Plot wolves
        for k in range(0,len(wolves)):
            matplotlib.pyplot.scatter(wolves[k].x,wolves[k].y, marker="o",  color='black', label = 'wolf')
            
            #Plot dead sheep
        for k in range(0,len(dead_sheep)):
            matplotlib.pyplot.scatter(dead_sheep[k].x,dead_sheep[k].y, marker="D",  color='red', alpha=0.4, label= 'dead')

            matplotlib.pyplot.show()


def sort_dead(self):
# Remove all dead agents from sheep list and append them into dead_sheep
    for item in agents:
        if item.status == 'dead':
            dead_sheep.append(item)
    agents[:] = [x for x in agents if x.status == 'alive']   
    print('Living sheep:' + str(len(agents)))
    print('Dead sheep:' + str(len(dead_sheep)))

animation = matplotlib.animation.FuncAnimation(fig, update, frames=frame_number, repeat=False)
#canvas.show() 

matplotlib.pyplot.legend(bbox_to_anchor=(1, 1), bbox_transform=pyplot.gcf().transFigure)


