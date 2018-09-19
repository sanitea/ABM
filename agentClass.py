import random 

#Agent class
class Agent ():
    def __init__ (self, environment):
        
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)   
        self.environment = environment
        self.store = 0
        
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
            
    def eat(self): # can you make it eat what is left?
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10