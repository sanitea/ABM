import random 
import matplotlib.pyplot


#Agent class
class Agent():
        
        def __init__ (self, environment):
            self.x = random.randint(0,250)
            self.y = random.randint(0,250)
            
            self.environment = environment
            self.store = 0
            
            self.agents_list = []

            self.num_of_iterations = 100
            self.num_of_agents = 10 
            
            self.neighbourhood = list 
            self.distance = 0
            
            self.agents_row_a = [self.x, self.y]
            self.agents_row_b = [self.x, self.y]
        
        def distance_between(self, agents):
                return (((self.x - agents.x)**2) + ((self.y - agents.y)**2))**0.5 
            
        #def update(num_of_iterations):
        
        def pop(self, agents):
            agents_list.append(agents)
            
            
        def move(self):
    #Agents Moving. Modulus operator = boundaries using torus method. 
            for j in range (self.num_of_iterations):
                for i in range (self.num_of_agents):
                    if random.random() < 0.5:
                        agents[i].y  = (agents[i].y + 1) % 99 
                    else:
                        agents[i].y  = (agents[i].y - 1) % 99
                    
                    if random.random() < 0.5:
                        agents[i].x  = (agents[i].x + 1) % 99 
                    else:
                        agents[i].x  = (agents[i].x - 1) % 99 
                        
            
        def eat(self): 
            if self.environment[self.y][self.x] > 10:
                self.environment[self.y][self.x] - 10
                self.store + 1
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
                  #  print(self.store)
                   # print("sharing " + str(dist) + " " + str(ave))
            
        #share information with agents 
        #def share_with_neighbours (neighbourhood):
         #   return (neighbourhood)

#def update(num_of_iterations):
    
#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
        