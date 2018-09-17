import random 

#Set up variables 
y0 = 50
x0 = 500
y1 = 50
x1 = 500

#Random walk one step y0
if random.random() < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1
    
   #Random walk one step x0
if random.random() < 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1

#Random walk one step y1
if random.random() < 0.5:
    y1 = y1 + 1
else:
    y1 = y1 - 1
    
   #Random walk one step x1
if random.random() < 0.5:
    x1 = x1 + 5
else:
    x1 = x1 - 5
    

    
print (y0, y1)
print (x0, x1)

answer = ((y0-y1)**2) + ((x0-x1)**2)*0.5

print (answer)