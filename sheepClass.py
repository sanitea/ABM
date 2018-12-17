import random 
import matplotlib.pyplot


#Agent class
class Sheep():
        
    #Variables created on initialization, spawn location
        def __init__ (self, environment, sheep, wolves):
            self.x = random.randint(50,220)
            self.y = random.randint(30,250)
            
            self.environment = environment
            self.store = 10
            
            self.sheep = sheep
            self.num_of_iterations = 100
            self.num_of_agents = len(sheep) 
            
            self.neighbourhood = list 
            self.distance = 0
            
            self.agents_row_a = [self.x, self.y]
            self.agents_row_b = [self.x, self.y]
            
            self.status = 'alive'
 
 #Function to calculate the distance between agents      
        def distance_between(self, agent):
                return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5 
                    
            
        def move(self):
 #Agents Moving. Modulus operator = boundaries using torus method. 
           for i in range (self.num_of_agents):
               if random.random() < 0.5:
                   self.y = (self.y + 1) % len(self.environment[0])
               else:
                   self.y = (self.y - 1) % len(self.environment[0])
                        
               if random.random() < 0.5:
                   self.x = (self.x + 1) % len(self.environment[0])
               else:
                   self.x = (self.x - 1) % len(self.environment[0])
                    
                        
#Check if there's still 'grass' left in the environment data-set, if there is the environment is 
# decreased by ten and the sheep's store goes up by one. 
        def eat(self): 
            if self.environment[self.y][self.x] > 100:
                self.environment[self.y][self.x] -= 40
                self.store += 1
              #  print(self.store)
         #   else:
              #  print('Troubleshooting Eat. Store = ' + str(self.store))

                
        def share_with_neighbours(self, neighbourhood, sheep):
            for agent in self.sheep:
                dist = self.distance_between(agent)
                if dist <= neighbourhood:
                    sum = self.store + agent.store
                    ave = sum /2
                    self.store = ave
                    agent.store = ave
                    #print("sharing " + str(dist) + " " + str(ave))
                    
              #  if self.store > 100:
                  #  print(self.store)
                   # print("sharing " + str(dist) + " " + str(ave))
            
#Check if the sheep's store has been depleted by wolf, if so mark change status to dead 
        def check_status(self):
        # Check for death    
            if self.store < 5:
                self.status = 'dead'

            
#def update(num_of_iterations):
    
#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)