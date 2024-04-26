import random
import math
attractorData = op("Attractor_Parameters")
blobbyData = op("Blobby_Parameters")

#Change these global variables as needed
xSpeed = 2
ySpeed = 2
collisionRadius = 2

# Plug in the real values of the center
centerPointX = 250
centerPointY = 250

def find_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance 
    
def checkIfEaten(x, y):
	    for row_index in range(blobbyData.numRows):
	    	if find_distance(x, y, blobbyData[row_index, 1], blobbyData[row_index, 2]) < collisionRadius*2:
	    		return True
	    	else:
	    		return False
    
for row_index in range(attractorData.numRows):
  row_data = []
  for col_index in range(attractorData.numCols):
      cell_value = attractorData.cell(row_index, col_index).val
      row_data.append(cell_value)
 #print(f"Row {row_index}: {row_data}")
 #print(row_data[2])
  newX = int(row_data[1])
  newY = int(row_data[2])
  

  if find_distance(newX, newY, centerPointX, centerPointY) > 250:
    xSpeed *= -1
    ySpeed *= -1
   
  newX += xSpeed
  newY += ySpeed
  attractorData[row_index, 1] = newX
  attractorData[row_index, 2] = newY
  print(checkIfEaten(newX, newY))      
         