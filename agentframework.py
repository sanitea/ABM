import random 

#Agent class
class Agent():
        
        def __init__ (self, environment, agents):

            self.environment = []
            self.store = 0
            self.agents = list
            self.x = random.randint(0,99)
            self.y = random.randint(0,99)
            self.num_of_iterations = 100
            self.num_of_agents = 10 
        
        
        def move(self):
                
    #Agents Moving. Modulus operator = boundaries using torus method. 
            for j in range (self.num_of_iterations):
                for i in range (self.num_of_agents):
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
            
        #share information with agents 
        #def share_with_neighbours (neighbourhood):
         #   return (neighbourhood)


        