import os
import numpy as np


def create_final_output(graph, v_num, x):
	fo_new = open("./graphs/infile%02d_%02d.txt" % (v_num, x+1), "w+")
	fo_new.write(str(v_num) + "\n")
	z = 0
	while(z < v_num):
		temp_s = ""
		i = 0
		while(i < v_num):
			if(i == 0):
				temp_s = temp_s + str(int(graph[z, i]))
			else:
				temp_s = temp_s + ", " + str(int(graph[z, i]))
			i += 1
		temp_s = temp_s + '\n'
		fo_new.write(temp_s)
		z += 1
	fo_new.close()

def create_complete_symmetric_graphs(n):
	points = []
	i = 0
	while(i < n):
		#make point on unit square for each vertex
		point = [np.random.randint(1000), np.random.randint(1000)]
		points.append(point)
		i += 1

	euclidian_graph = np.zeros((n, n))

	i = 0
	while(i < n):
		ii = 0
		while(ii < n): #doing this the dumb and fast way
			euclidian_graph[i,ii] = np.sqrt(((points[i][0]-points[ii][0])*(points[i][0]-points[ii][0])) + ((points[i][1]-points[ii][1])*(points[i][1]-points[ii][1])))
			ii += 1
		i += 1

	return euclidian_graph

def eat_plantri_output(fname, x_temp, graphs):
	fo = open(fname, "r")
	x = 0 + x_temp
	v_num = 0

	for line in fo:

		t0 = line.split(" ")
		t1 = (t0[1].replace('\n', '')).split(",")

		v_num = int(t0[0])
		#print(v_num)

		points = []
		i = 0
		while(i < v_num):
			#make point on unit square for each vertex
			point = [np.random.randint(1000), np.random.randint(1000)]
			points.append(point)
			i += 1

		euclidian_graph = np.zeros((v_num, v_num))

		i = 0
		while(i < v_num):
			ii = 0
			while(ii < v_num): #doing this the dumb and fast way
				euclidian_graph[i,ii] = np.sqrt(((points[i][0]-points[ii][0])*(points[i][0]-points[ii][0])) + ((points[i][1]-points[ii][1])*(points[i][1]-points[ii][1])))
				ii += 1
			i += 1

		graph = np.zeros((v_num, v_num))
		z = 0
		while(z < v_num):
			for c in t1[z]:
				#print(ord(c) - 97)
				if(graph[z, ord(c) - 97] == 0):
					graph[z, ord(c) - 97] = 1
					graph[z, ord(c) - 97] = euclidian_graph[z, ord(c) - 97]
					#add connection, set to distance in euclidian graph
			#print(t1[z])
			z += 1
		graphs.append(graph)
		x += 1
	print(x)
	fo.close()
	if(x < 30):
		eat_plantri_output(fname, x, graphs)
		#recurse until we have 30 to make up the five missing for the 5-node example
	else:
		#create the final outputs
		picks = []
		pick = 0
		i = 0
		while(i < 30):
			pick = np.random.randint(x) #pick a random graph from our selection
			while(pick in picks):
				pick = np.random.randint(x)
			create_final_output(graphs[pick], v_num, i)
			picks.append(pick)
			i += 1

'''
if(False):
	orders = []

	orders.append("make plantri")

	i = 1
	while(i <= 6):
		n = i * 5
		orders.append("rm ./regli_assignment_output/" + "plantri_out_" + str(n) +".txt")
		orders.append("touch ./regli_assignment_output/" + "plantri_out_" + str(n) +".txt")
		ii = 0
		while(ii < 10):
			orders.append("./plantri -pm1c1 -a " + str(n) + " " + str(ii) + "/10 | head -n100 >> ./regli_assignment_output/plantri_out_" + str(n) +".txt")
			orders.append("./plantri -pm4c4 -a " + str(n) + " " + str(ii) + "/10 | head -n100 >> ./regli_assignment_output/plantri_out_" + str(n) +".txt")
			ii += 1
		i += 1


	i = 0
	while(i < len(orders)):
		print(orders[i])
		os.system(orders[i])
		i += 1
	#./plantri -pm1c1 -a 30 | head -n1000 > out.txt

	i = 1
	while(i <= 6):
		n = i * 5
		eat_plantri_output("./regli_assignment_output/plantri_out_" + str(n) +".txt", 0, [])
		i += 1
else:
	i = 1
	while(i <= 6):
		n = i * 5
		ii = 0
		while(ii < 30):
			create_final_output(create_complete_symmetric_graphs(n), n, ii)
			ii += 1
		i += 1


#os.system("zip -r ./regli_assignment_output/input_graphs.zip ./regli_assignment_output/final")

'''















