import random 
import matplotlib.pyplot


#Agent class
class Agent():
        
        def __init__ (self, environment, agents):
            self.x = random.randint(0,220)
            self.y = random.randint(0,250)
            
            self.environment = environment
            self.store = 0
            
            self.agents = agents
            self.num_of_iterations = 100
            self.num_of_agents = 10 
            
            self.neighbourhood = list 
            self.distance = 0
            
            self.agents_row_a = [self.x, self.y]
            self.agents_row_b = [self.x, self.y]
            
            self.dead = False 
        
        def distance_between(self, agent):
                return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5 
            
        #def update(num_of_iterations):
            
            
            
        def move(self):
    #Agents Moving. Modulus operator = boundaries using torus method. 
           # for j in range (self.num_of_iterations):
           for i in range (self.num_of_agents):
               if random.random() < 0.5:
                   self.y = (self.y + 1) % 300
               else:
                   self.y = (self.y - 1) % 300
                        
               if random.random() < 0.5:
                   self.x = (self.x + 1) % 300
               else:
                   self.x = (self.x - 1) % 300 
                    
                        
            
        def eat(self): 
            if self.environment[self.y][self.x] > 10:
                self.environment[self.y][self.x] -= 100
                self.store += 1
              #  print(self.store)
         #   else:
              #  print('cats')
                
        def share_with_neighbours(self, neighbourhood:int, agents):
            for agent in agents:
                dist = self.distance_between(agent)
                if dist <= neighbourhood:
                    sum = self.store + agent.store
                    ave = sum /2
                    self.store = ave
                    agent.store = ave
                if agent.store < 2:
                    del agent
                  #  print(self.store)
                   # print("sharing " + str(dist) + " " + str(ave))
            
        #share information with agents 
        #def share_with_neighbours (neighbourhood):
         #   return (neighbourhood)

#def update(num_of_iterations):
    
#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)