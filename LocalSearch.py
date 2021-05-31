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

def calc_cost(soln, graph):
    cost = 0
    for i in range(len(soln)-1):
        cost += graph[soln[i]][soln[i+1]]
    return cost


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

all_cities = []
for city in graph_dict.keys():
    all_cities.append(city)

problem_graph = Search.UndirectedGraph(graph_dict)
simulated_annealing_graph = Search.UndirectedGraph(graph_dict)
hill_climbing_tsp = Search.TSP_problem(all_cities, graph_dict)
simulated_annealing_tsp = Search.TSP_problem(all_cities, graph_dict)



if __name__ == '__main__':
    size = numberOfVertices
    hill_climbing_filename = "csv_files/hill_climbing.csv"
    simulated_annealing_filename = "csv_files/simulated_annealing.csv"
    genetic_algorithm_filename = "csv_files/genetic_algorithm.csv"


    fields = ['Size', 'Cost', 'Real Time', 'CPU Time']

    hill_climbing_stats = []
    simulated_annealing_stats = []
    genetic_algorithm_stats = []

    hill_climbing_cost = []
    hill_climbing_realtime = []
    hill_climbing_cpu_time = []


    simulated_annealing_cost = []
    simulated_annealing_realtime = []
    simulated_annealing_cpu_time = []


    genetic_algorithm_cost = []
    genetic_algorithm_realtime = []
    genetic_algorithm_cpu_time = []



    start_time = time.time()
    start_process_time = time.process_time()
    hill_climbing_solution = Search.hill_climbing(hill_climbing_tsp)
    hill_climbing_solution.append(hill_climbing_solution[0])
    print(hill_climbing_solution)
    elapsed_process_time = time.process_time() - start_process_time
    elapsed_time = time.time() - start_time

    hill_climbing_stats.append([size, calc_cost(hill_climbing_solution, graph_dict), elapsed_time, elapsed_process_time])


    start_time = time.time()
    start_process_time = time.process_time()
    simulated_annealing_solution = Search.simulated_annealing(simulated_annealing_tsp)
    simulated_annealing_solution.append(simulated_annealing_solution[0])
    elapsed_process_time = time.process_time() - start_process_time
    elapsed_time = time.time() - start_time

    simulated_annealing_stats.append([size, calc_cost(simulated_annealing_solution, graph_dict), elapsed_time, elapsed_process_time])


    genetic_algo = Search.GeneticAlgorithm(numberOfVertices, adjMatrix, dict_numbers_to_letters)
    genetic_initial_pop = genetic_algo.init_population(100, numberOfVertices)
    genetic_fitness = Search.GeneticAlgorithm.fitness_fn
    gene_pool = []
    for x in range(numberOfVertices):
        gene_pool.append(dict_numbers_to_letters[x])

    start_time = time.time()
    start_process_time = time.process_time()
    genetic_algo_solution = genetic_algo.genetic_algorithm(genetic_initial_pop, genetic_fitness, gene_pool, None, 200)
    genetic_algorithm_solution = genetic_algo_solution
    genetic_algorithm_solution.append(genetic_algorithm_solution[0])
    elapsed_process_time = time.process_time() - start_process_time
    elapsed_time = time.time() - start_time

    genetic_algorithm_stats.append([size, calc_cost(genetic_algorithm_solution, graph_dict), elapsed_time, elapsed_process_time])



    with open(hill_climbing_filename, 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(hill_climbing_stats)

    with open(simulated_annealing_filename, 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(simulated_annealing_stats)

    with open(genetic_algorithm_filename, 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(genetic_algorithm_stats)

