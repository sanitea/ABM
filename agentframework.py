import random 

#Agent class
class Agent():
        
        def __init__ (self, environment, agents):
            self.x = random.randint(0,199)
            self.y = random.randint(0,199)
            
            self.environment = environment
            self.store = 0
            
            self.agents = list

            self.num_of_iterations = 100
            self.num_of_agents = 10 
        
        
        def move(self):
                
    #Agents Moving. Modulus operator = boundaries using torus method. 
            for j in range (self.num_of_iterations):
                for i in range (self.num_of_agents):
                    if random.random() < 0.5:
                        self.y = (self.y + 1) % 199
                    else:
                        self.y = (self.y - 1) % 199
                        
                    if random.random() < 0.5:
                        self.x = (self.x + 1) % 199
                    else:
                        self.x = (self.x - 1) % 199  
            
        def eat(self): 
            if self.environment[self.y][self.x] > 10:
                self.environment[self.y][self.x] -= 10
                self.store += 10
            else:
                print(cats)
            
        #share information with agents 
        #def share_with_neighbours (neighbourhood):
         #   return (neighbourhood)


        