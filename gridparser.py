import json

f = open('housetest.json')

data = json.load(f)

#for i in data['blocks']:
    # print("X = " + str(i['pos'][0]) + ", " + "Y = " + str(i['pos'][1]) + ", " "Z = " + str(i['pos'][2]))

 #   x = str(i['pos'][0])
 # y = str(i['pos'][1])
  #  z = str(i['pos'][2])

def slicer(y):
    for i in data['blocks']:
        #print(str(i['pos'][1]))
        #print("y = " + str(y))
        if str(i['pos'][1]) == str(y):
            print("State = " + str(i['state']))

slicer(2)


f.close()