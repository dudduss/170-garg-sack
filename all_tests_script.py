import os

for i in range(1, 22): #Specify Range Here
	input_file = 'problem' + str(i) + '.in'
	output_file = 'problem' + str(i) + '.out'
	command = 'python sample_solver.py ' + input_file + " " + output_file

	os.system(command)