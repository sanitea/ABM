import random 

#share information with agents 
def share_with_nbh ():
    return ("cats")

#function to find the distance between agents using Pythagous 
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) + 
    ((agents_row_a.y - agents_row_b.y)**2))**0.5

#Agent class
class Agent ():
        
    def __init__ (self, environment, agents):
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)   
        self.environment = environment
        self.store = 0
        self.agents = agents     
        self.share_with_nbh = share_with_nbh

        
    def move(self):
            
#Agents Moving. Modulus operator = boundaries using torus method. 
    #    for j in range (num_of_interations):
     #       for i in range (num_of_agents):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100
            
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100  
            
    def eat(self): 
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
            

        