import random

wordFile = open("nameFinale.txt", "r")
writeFile = open("input1.in", "w")


class_cnt = 50000
arr_item = wordFile.readlines()
arr = arr_item[:87750]


writeFile.write("4000000\n")
writeFile.write("4000000\n")
writeFile.write("{}\n".format(len(arr)))
writeFile.write("99999\n")

for i in range(0, len(arr)):
	writeFile.write("{}; {}; {}; {}; {}\n".format(arr_item[i].rstrip(), (i % class_cnt), random.randint(0, 30),(i + 1) * random.randint(2, 10), i))

for i in range(0, class_cnt - 1):
	writeFile.write("{}, {}\n".format(i, i + 1))



