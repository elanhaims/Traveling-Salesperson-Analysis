import sys
import Search
import random
import time
import timeit
import csv

line = sys.stdin.readlines()
numberOfVertices = int(line[0])

dict_numbers_to_letters = {}
for x in range(26):
    dict_numbers_to_letters[x] = chr(x + 65)
dict_numbers_to_letters[26] = 'AA'
dict_numbers_to_letters[27] = 'BB'
dict_numbers_to_letters[28] = 'CC'
dict_numbers_to_letters[29] = 'DD'



adjMatrix = []

for x in range(1, numberOfVertices + 1):
    adjMatrix.append(list(map(int, line[x].split(", "))))

graph_dict = {}

for i in range(len(adjMatrix)):
    tempDict = {}
    for j in range(len(adjMatrix[i])):
        if adjMatrix[i][j] != 0:
            tempDict[dict_numbers_to_letters[j]] = adjMatrix[i][j]
    graph_dict[dict_numbers_to_letters[i]] = tempDict

problem_graph = Search.UndirectedGraph(graph_dict)

ucs_prob = Search.GraphProblem('A', numberOfVertices, problem_graph, adjMatrix, 0)
random_edge_prob = Search.GraphProblem('A', numberOfVertices, problem_graph, adjMatrix, 0)
cheapest_edge_prob = Search.GraphProblem('A', numberOfVertices, problem_graph, adjMatrix, 0)
mst_prob = Search.GraphProblem('A', numberOfVertices, problem_graph, adjMatrix, 0)



random_edge_heuristic = random_edge_prob.random_edges
cheapest_edge_heuristic = cheapest_edge_prob.cheapest_edges
mst_heuristic = mst_prob.prim_mst_heuristic



def calc_cost(soln, graph):
    cost = 0
    for i in range(len(soln)-1):
        cost += graph.get(soln[i],soln[i+1])
    return cost

if __name__ == '__main__':
    size = numberOfVertices
    ucs_filename = "ucs.csv"
    rand_edge_filename = "random_edges.csv"
    cheapest_edge_filename = "cheapest_edges.csv"
    mst_filename = "mst.csv"

    fields = ['Size', 'Cost', 'Nodes Expanded', 'Real Time', 'CPU Time']

    ucs_stats = []
    random_edges_stats = []
    cheapest_edges_stats = []
    mst_stats = []

    ucs_cost = []
    ucs_realtime = []
    ucs_cpu_time = []
    ucs_num_nodes = []

    rand_cost = []
    rand_realtime = []
    rand_cpu_time = []
    rand_num_nodes = []

    cheapest_cost = []
    cheapest_realtime = []
    cheapest_cpu_time = []
    cheapest_num_nodes = []

    mst_cost = []
    mst_realtime = []
    mst_cpu_time = []
    mst_num_nodes = []

    start_time = time.time()
    start_process_time = time.process_time()
    ucs_solution = Search.uniform_cost_search(ucs_prob).solution()[size - 1]
    ucs_nodes_expanded = ucs_prob.nodes_expanded()
    elapsed_process_time = time.process_time() - start_process_time
    elapsed_time = time.time() - start_time

    ucs_stats.append([size, calc_cost(ucs_solution, problem_graph), ucs_nodes_expanded, elapsed_time, elapsed_process_time])

    start_time = time.time()
    start_process_time = time.process_time()
    random_edge_solution = Search.astar_search(random_edge_prob, random_edge_heuristic).solution()[size - 1]
    random_edge_nodes_expanded = random_edge_prob.nodes_expanded()
    elapsed_process_time = time.process_time() - start_process_time
    elapsed_time = time.time() - start_time

    random_edges_stats.append([size, calc_cost(random_edge_solution, problem_graph), random_edge_nodes_expanded, elapsed_time, elapsed_process_time])


    start_time = time.time()
    start_process_time = time.process_time()
    cheapest_edge_solution = Search.astar_search(cheapest_edge_prob, cheapest_edge_heuristic).solution()[size - 1]
    cheapest_edge_nodes_expanded = cheapest_edge_prob.nodes_expanded()
    elapsed_process_time = time.process_time() - start_process_time
    elapsed_time = time.time() - start_time

    cheapest_edges_stats.append([size, calc_cost(cheapest_edge_solution, problem_graph), cheapest_edge_nodes_expanded, elapsed_time, elapsed_process_time])


    start_time = time.time()
    start_process_time = time.process_time()
    mst_solution = Search.astar_search(mst_prob, mst_heuristic).solution()[size - 1]
    mst_nodes_expanded = mst_prob.nodes_expanded()
    elapsed_process_time = time.process_time() - start_process_time
    elapsed_time = time.time() - start_time

    mst_stats.append([size, calc_cost(mst_solution, problem_graph), mst_nodes_expanded, elapsed_time, elapsed_process_time])


    with open(ucs_filename, 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        print(ucs_stats)
        csvwriter.writerows(ucs_stats)

    with open(rand_edge_filename, 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(random_edges_stats)

    with open(cheapest_edge_filename, 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(cheapest_edges_stats)

    with open(mst_filename, 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(mst_stats)





