import random
import matplotlib.pyplot as plt
import sheepClass
import csv 
import matplotlib.animation 
import wolfclass
import matplotlib.lines as mlines

#Function to work out the distance between models 
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) + 
    ((agents_row_a.y - agents_row_b.y)**2))**0.5
            
#Intial Variables 
num_of_sheep = 10
num_of_wolves = 2
frame_number = 50
neighbourhood = 10 
sheep = []
environment = []
wolves = []
dead_sheep = []

#Output variables 
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])



#Environment. Empty row, append rowlist to environment, append rowlist. 
f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:	
    rowlist = [] 
    environment.append(rowlist)
    for value in row:
        rowlist.append(value)		
f.close() 

# Make the agents, append them to the environment, and then .
for i in range(num_of_sheep):
    sheep.append(sheepClass.Sheep(environment, sheep, wolves))
    sheep[i].share_with_neighbours(neighbourhood, sheep)
    
#Make Wolves
for i in range(num_of_wolves):
    wolves.append(wolfclass.Wolf(environment, sheep, wolves))
  
#Labels 
sheep_label = mlines.Line2D([], [], color='white', marker='o',
                          markersize=8, label='Sheep')

wolf_label = mlines.Line2D([], [], color='black', marker='o',
                          markersize=8, label='Wolf')

dead_label = mlines.Line2D([], [], color='red', marker='x',
                          markersize=8, label=' Dead Sheep')



# Move the agents.
def update (frame_number):

    for i in range (frame_number):
        fig.clear()
        plt.imshow(environment, vmin = 0, vmax = 300)
        plt.xticks([], [])
        plt.yticks([], [])
        plt.title('Agent Based Model', loc='left')
        plt.legend(handles=[sheep_label, wolf_label, dead_label], bbox_to_anchor=(1, 1), loc='upper right')
        
        for j in range(num_of_sheep):

            #Shuffle agents to prevent model artifacting 
            random.shuffle(sheep)
            
            #Sheep move, eat, and check status 
            sheep[len(sheep) -1].move()
            sheep[len(sheep) -1].eat()
            sheep[len(sheep) -1].check_status()
            
            sheep[len(sheep) -1].share_with_neighbours(neighbourhood, sheep)
            sort_dead(sheep)
            
            #Wolves move and share information with neighbours
        for j in range(num_of_wolves):
            wolves[j - 1].move()
            wolves[j - 1].check_for_sheep(neighbourhood, sheep)
            
            
            #Plot living sheep
        for k in range(0,len(sheep)):
            plt.scatter(sheep[k].x,sheep[k].y, marker="o",  color='white', label = 'sheep')
            
            #Plot wolves
        for k in range(0,len(wolves)):
            plt.scatter(wolves[k].x,wolves[k].y, marker="o",  color='black', label = 'wolf')
            
            #Plot dead sheep
        for k in range(0,len(dead_sheep)):
            plt.scatter(dead_sheep[k].x,dead_sheep[k].y, marker="x",  color='red', alpha=0.65, label= 'dead')



            plt.show()


def sort_dead(self):
# Remove all dead agents from sheep list and append them into dead_sheep
    for item in sheep:
        if item.status == 'dead':
            dead_sheep.append(item)
    sheep[:] = [x for x in sheep if x.status == 'alive']   
    #print('Living sheep:' + str(len(sheep)))
    #print('Dead sheep:' + str(len(dead_sheep)))
    

animation = matplotlib.animation.FuncAnimation(fig, update, frames=frame_number, repeat=False)

animation.save('animation1.gif', writer='imagemagick', fps=1)
