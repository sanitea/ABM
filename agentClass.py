import random 

#function to find the distance between agents using Pythagous 
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) + 
    ((agents_row_a.y - agents_row_b.y)**2))**0.5

#Agent class
class Agent ():
        
        def __init__ (self):
            self.environment = environment
            self.store = 0
            self.agents = list
            self.share_with_neighbours = list 
            self.num_of_iterations = int
        
        #@property
       # def x(self):
           # return self._x

       # @x.setter
       # def x(self, value):
        #    self._x = value

     #   @x.deleter
      #  def x(self):
       #     del self._x  
        
        #@property
        #def y(self):
          #  return self.y

        #@y.setter
        #def y(self, value):
         #   self._y = value

        #@y.deleter
        #def y(self):
         #   del self._y
            

            pass

        
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
        def share_with_neighbours (neighbourhood):
            return (neighbourhood)


        