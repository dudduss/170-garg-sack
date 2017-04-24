import random

readFile = open("nameFinale.txt", 'r')
writeTest = open("input2.in", 'w')

items = readFile.readlines()

num_items = 65000
num_classes = num_items/2

items = items[0:num_items]
classes = []

for i in range(num_items):
	classes.append(int(i%num_classes))


writeTest.write("4000000\n") #pounds
writeTest.write("4000000\n") #dollars
writeTest.write(str(num_items) + "\n") #number_items
writeTest.write("199998\n") #number_constraints

cost = 0.0
weight = 0.0
resale = 0.0
#Listing all items in store 
for i in range(len(items)):
	cost_random = float(random.randint(1, 10)) * 0.1
	weight_random = float(random.randint(1, 10)) * 0.1
	resale_random = float(random.randint(1, 10)) * 0.1

	cost += cost_random
	weight += weight_random
	resale += resale_random

	writeTest.write(items[i].rstrip() + "; " + str(classes[i]) + "; " + "%.2f" % weight + "; " + "%.2f" % cost + "; " + "%.2f" % resale + "\n")

#Listing all constraints in store
for i in range(len(items) - 1):
	writeTest.write(str(classes[i]) + ", " + str(classes[i+1]) + "\n")
