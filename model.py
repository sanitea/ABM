import random
import operator
import matplotlib.pyplot
import agentframework

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
    ((agents_row_a.y - agents_row_b.y)**2))**0.5

environment = []
agents = list
a = agentframework.Agent(environment, agents)
a.num_of_agents = 10
num_of_agents = 10
a.num_of_iterations = 100
num_of_iterations = 100

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
    agents.append(environment)

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()



matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b) 