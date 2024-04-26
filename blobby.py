import random
import math

blobbyData = op("Blobby_Parameters")
attractorData = op("Attractor_Parameters")



def find_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance 

def unit_vector(x1, y1, x2, y2):
	legX = x2 - x1
	legY = y2 - y1
	theta = math.atan2(legY, legX)        
	return [math.cos(theta), math.sin(theta)]
	
def closest_food(blobby_index):
	closestFood = [int(attractorData[0, 1]), int(attractorData[0, 2])] 
	for row_index in range(attractorData.numRows):
		 if find_distance(blobbyData[blobby_index, 1], blobbyData[blobby_index, 2], attractorData[row_index, 1], attractorData[row_index, 2]) < find_distance(blobbyData[blobby_index, 1], blobbyData[blobby_index, 2], closestFood[0],closestFood[1]):
		 	closestFood = [int(attractorData[row_index, 1]), int(attractorData[row_index, 2])]
	return closestFood
		
def furthest_segment(index, closestFood):
	furthestSegment = 1
	for i in range(1, 11):
		if i % 2 != 0:
			if find_distance(blobbyData[index, i], blobbyData[index, i+1], closestFood[0], closestFood[1]) > find_distance(blobbyData[index, furthestSegment], blobbyData[index, furthestSegment+1], closestFood[0], closestFood[1]):
				furthestSegment = i
	return furthestSegment
		 
#All looped events should be indented past the for loop. 
def main_loop():
	for index in range(blobbyData.numRows):
		closestFood = closest_food(index)
		direction = unit_vector(blobbyData[index, 1], blobbyData[index, 2], closestFood[0], closestFood[1])
		furthestSeg = furthest_segment(index, closestFood)
		
		blobbyData[index, furthestSeg] += direction[0]*2
		blobbyData[index, furthestSeg + 1] += direction[1]*2


main_loop()
