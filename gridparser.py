# json for loading JSON data
import json
# numby for 3 dimensional array support
import numpy as np

# open and load the JSON file
f = open('housetest.json')
data = json.load(f)

# load block array dimensions
sizeX = data['size'][0]
sizeY = data['size'][1]
sizeZ = data['size'][2]

# initialize 3 dimensional array using limits
arayBlocks = np.zeros((sizeX,sizeY,sizeZ),int)

# load the array by iterating through the JSON file
def loadBlocks():
    for i in data['blocks']:
        # print("loading:" + str(i['pos'][0]) + " " + str(i['pos'][1]) + " " + str(i['pos'][2]) + "=" + str(i['state']))
        arayBlocks[int(i['pos'][0]),int(i['pos'][1]),int(i['pos'][2])] = str(i['state'])

# Dray out a layer (z)
def drawLayer(y):

    rowstr = ""

    x = 0
    z = 0
    # loop for each row in the layer
    while z  < sizeZ:
        #print ("row = " + str(z))
        # loop for each iten in the row
        while x < sizeX:
            rowstr = str(rowstr) + " " + str(arayBlocks[x,y,z])
            x += 1
        print(str(rowstr))
        rowstr = ""
            
        # start a the first item of the next row
        x = 0
        # move to the next row
        z += 1
    print("\n")

# Load block array
loadBlocks()

# Draw all layers
y = 0
while y < sizeY:
    print("drawing layer " + str(y))
    print("\n")
    drawLayer(y)
    y += 1

f.close()

#str(x) + " " + str(y) + " " + str(z) + "=" + 