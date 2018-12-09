import random 
import matplotlib.pyplot


#Agent class
class Wolf():
        
        def __init__ (self, environment, agents, wolves):
            self.x = random.randint(0,250)
            self.y = random.randint(0,250)
            
            self.environment = environment
            self.store = 0
            
            self.agents = agents
            self.num_of_wolves = len(wolves) - 1

            self.num_of_iterations = 100
            self.num_of_agents = 10 
            
            self.neighbourhood = list 
            self.distance = 0
            
            self.agents_row_a = [self.x, self.y]
            self.agents_row_b = [self.x, self.y]
        
        def distance_between(self, agent):
                return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5 
            
   
            
        def move(self):
           for i in range (self.num_of_agents):
               if random.random() < 0.5:
                   self.y = (self.y + 1) % 295
               else:
                   self.y = (self.y - 1) % 295
                        
               if random.random() < 0.5:
                   self.x = (self.x + 1) % 295
               else:
                   self.x = (self.x - 1) % 295 
 
        def check_for_sheep(self, neighbourhood, agents):
            for agent in self.agents:
                dist = self.distance_between(agent)
                if dist <= neighbourhood:
                    agent.store = 0
                    print ("ate sheep")
                       
                
 