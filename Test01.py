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
