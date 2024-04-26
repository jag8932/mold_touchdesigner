import random
import math
blobbyData = op('Blobby_Parameters')
attractorData = op('Attractor_Parameters')
sporeData = op('Spore_Parameters')

blobRadius = 1


def initialize_blobby():
	maxNum = 10
	
	for i in range(maxNum):
		cX = random.randint(1, 500)
		cY = random.randint(1, 500)
		blobbyData.appendRow(["blobby_" + str(i), cX, cY, cX + 1, cY + 1, cX + 2, cY + 2, cX + 3, cY + 3, cX + 4, cY + 4])

def initialize_attractor():
	maxNum = 100
	
	for i in range(maxNum):
		cX = random.randint(1, 500)
		cY = random.randint(1, 500)
		attractorData.appendRow(["attractor_" + str(i), cX, cY])
	

blobbyData.clear()
attractorData.clear()

initialize_blobby()
initialize_attractor()




