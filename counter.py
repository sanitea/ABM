# Toy raster GIS in MicroPython
# Andy Evans http://www.geog.leeds.ac.uk/people/a.evans/

from microbit import *
import sys 

# Hill altitude (small area of the Lake District).
# In theory you should be able to read local files, but 
# couldn't get it working; it deletes the filesystem with 
# each program install, which doesn't help.
data = []
data.append([220,221,222,223,226,230,234,238,241,241,242,243,243,243,244,244])
data.append([221,222,223,224,227,231,234,238,241,241,242,243,243,243,244,244])
data.append([222,223,223,224,228,232,235,239,241,242,242,243,243,243,244,244])
data.append([223,224,224,225,228,232,235,239,242,242,243,243,243,243,243,244])
data.append([226,227,228,228,231,234,237,240,242,243,243,243,243,243,243,244])
data.append([230,231,232,232,235,237,238,240,242,243,243,243,243,243,243,243])
data.append([233,234,235,236,238,239,239,241,242,242,243,243,243,242,243,243])
data.append([237,238,239,240,241,241,241,241,242,242,243,243,242,242,242,243])
data.append([241,242,242,243,243,243,242,242,242,243,243,243,243,242,242,242])
data.append([242,243,243,244,244,243,243,242,243,243,244,243,243,242,242,242])

# Centre of current view
x = 2
y = 2


while True:
    
    # Gesture control slides the map in the direction you tilt it.
    gesture = accelerometer.current_gesture()
    if gesture == "up":
        y = y - 1
    if gesture == "down":
        y = y + 1
    if gesture == "left":
        x = x - 1
    if gesture == "right":
        x = x + 1

    # Buttons scan through map.
    if button_a.is_pressed():
        x = x + 1

    if button_b.is_pressed():
        y = y + 1

    # Wrap as torus. Not ideal for real data, but 
    # given only two buttons...
    if y < 2:
        y = len(data) - 3
    elif y > len(data) - 3:
        y = 2

    if x < 2:
        x = len(data[0]) - 3
    elif x > len(data[0]) - 3:
        x = 2

    # Construct current view.
    imglist=[
        [data[y-2][x-2],data[y-1][x-2],data[y][x-2],data[y+1][x-2],data[y+2][x-2]],
        [data[y-2][x-1],data[y-1][x-1],data[y][x-1],data[y+1][x-1],data[y+2][x-1]],
        [data[y-2][x],data[y-1][x],data[y][x],data[y+1][x],data[y+2][x]],
        [data[y-2][x+1],data[y-1][x+1],data[y][x+1],data[y+1][x+1],data[y+2][x+1]],
        [data[y-2][x+2],data[y-1][x+2],data[y][x+2],data[y+1][x+2],data[y+2][x+2]]
        ]
    strlist = ""
    
    for line in imglist:
        for cell in line:
            cell = (cell / 255) * 9
            cell = str(cell)    
            strlist = strlist + cell
        strlist = strlist + ":"
            
    img = Image(strlist)
    
    display.show(img)


