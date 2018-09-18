import random
import operator
import matplotlib.pyplot

num_of_agents = 10
num_of_iterations = 100
agents = []

# Instanciate 
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])
    
print ("Start", agents)
_ = agents

# Moving 
for j in range(num_of_iterations):
    for i in range(num_of_agents):

        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100

max_co = (max(agents, key=operator.itemgetter(1)))

print ("End", agents)
print (max_co)

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()