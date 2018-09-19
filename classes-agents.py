import random 
#import operator 
import matplotlib.pyplot

#function for finding the difference 
def distance_between(agents_row_a, agents_row_b):
    answer = ((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2)**0.5
    return answer
    print (agents_row_a)
    print (agents_row_b)

#Agent class
class agent ():
    def __init__ (self, movement, distance):
        
        self.movement = movement 
        self.distance = distance
        
        def movement (self)
        #Agents Moving. Modulus operator = boundaries using torus method. 
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

#Variables 
num_of_agents = 10
num_of_interations = 100
agents = []

#Agents instanciating  
for i in range (num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])



#Distance
for i in range (0,num_of_agents):
    for j in range (i,num_of_agents):
        distance = distance_between(agents[i], agents[j])
        print (distance)
