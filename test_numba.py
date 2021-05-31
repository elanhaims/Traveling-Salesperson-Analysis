from Generate_graphs import generate_graphs
import Search
import csv
import time
import numba



def perform_A_Star_Search(min_graph_size, max_graph_size, increment, number_of_graphs):


    for graph_size in range(min_graph_size, max_graph_size + 1, increment):
        for graph_number in range(1, number_of_graphs + 1):

            print("graph number: " +  str(graph_number) + ', graph size:' + str(graph_size))

            problem_graph, ucs_prob, random_edge_prob, cheapest_edge_prob, mst_prob = \
                generate_graph_problems(graph_size, graph_number)
        
            random_edge_heuristic = random_edge_prob.random_edges
            cheapest_edge_heuristic = cheapest_edge_prob.cheapest_edges
            mst_heuristic = mst_prob.prim_mst_heuristic
            """
            size = graph_size

            # fields = ['Size', 'Cost', 'Nodes Expanded', 'Real Time', 'CPU Time']

            ucs_stats = []
            random_edges_stats = []
            cheapest_edges_stats = []
            mst_stats = []

            ucs_stats = compute_ucs_stats(ucs_prob, ucs_stats, size, problem_graph)

            random_edges_stats = compute_random_edges_stats(random_edge_prob, random_edge_heuristic,
                                                            random_edges_stats, size, problem_graph)

            cheapest_edges_stats = compute_cheapest_edges_stats(cheapest_edge_prob, cheapest_edge_heuristic,
                                                                cheapest_edges_stats, size, problem_graph)

            mst_stats = compute_mst_stats(mst_prob, mst_heuristic, mst_stats, size, problem_graph)

            with open("csv_files/ucs.csv", 'a') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerows(ucs_stats)

            with open("csv_files/random_edges.csv", 'a') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerows(random_edges_stats)

            with open("csv_files/cheapest_edges.csv", 'a') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerows(cheapest_edges_stats)

            with open("mst.csv", 'a') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerows(mst_stats)
                """


def generate_graph_problems(graph_size, graph_number):

    graph_file_name = "graphs/infile{graph_size:02}_{graph_number:02}.txt".format(graph_size=graph_size, graph_number=graph_number)
    graph_file = open(graph_file_name, "r").read()
    graph_file = graph_file.split("\n")

    number_of_vertices = graph_size

    dict_numbers_to_letters = {}
    for x in range(26):
        dict_numbers_to_letters[x] = chr(x + 65)
    dict_numbers_to_letters[26] = 'AA'
    dict_numbers_to_letters[27] = 'BB'
    dict_numbers_to_letters[28] = 'CC'
    dict_numbers_to_letters[29] = 'DD'

    adj_matrix = []

    for x in range(1, number_of_vertices + 1):
        adj_matrix.append(list(map(int, graph_file[x].split(", "))))

    graph_dict = {}

    for i in range(len(adj_matrix)):
        temp_dict = {}
        for j in range(len(adj_matrix[i])):
            if adj_matrix[i][j] != 0:
                temp_dict[dict_numbers_to_letters[j]] = adj_matrix[i][j]
        graph_dict[dict_numbers_to_letters[i]] = temp_dict

    problem_graph = Search.UndirectedGraph(graph_dict)

    ucs_prob = Search.GraphProblem('A', number_of_vertices, problem_graph, adj_matrix, 0)
    random_edge_prob = Search.GraphProblem('A', number_of_vertices, problem_graph, adj_matrix, 0)
    cheapest_edge_prob = Search.GraphProblem('A', number_of_vertices, problem_graph, adj_matrix, 0)
    mst_prob = Search.GraphProblem('A', number_of_vertices, problem_graph, adj_matrix, 0)

    return problem_graph, ucs_prob, random_edge_prob, cheapest_edge_prob, mst_prob


def calc_cost(solution, graph):
    cost = 0
    for i in range(len(solution) - 1):
        cost += graph.get(solution[i], solution[i + 1])
    return cost


@numba.jit
def compute_ucs_stats(ucs_prob, ucs_stats, size, problem_graph):
    start_time = time.time()
    start_process_time = time.process_time()
    ucs_solution = Search.uniform_cost_search(ucs_prob).solution()[size - 1]
    ucs_nodes_expanded = ucs_prob.nodes_expanded()
    elapsed_process_time = time.process_time() - start_process_time
    elapsed_time = time.time() - start_time

    ucs_stats.append(
        [size, calc_cost(ucs_solution, problem_graph), ucs_nodes_expanded, elapsed_time, elapsed_process_time])
    return ucs_stats

@numba.jit
def compute_random_edges_stats(random_edge_prob, random_edge_heuristic, random_edges_stats, size, problem_graph):
    start_time = time.time()
    start_process_time = time.process_time()
    random_edge_solution = Search.astar_search(random_edge_prob, random_edge_heuristic).solution()[size - 1]
    random_edge_nodes_expanded = random_edge_prob.nodes_expanded()
    elapsed_process_time = time.process_time() - start_process_time
    elapsed_time = time.time() - start_time

    random_edges_stats.append(
        [size, calc_cost(random_edge_solution, problem_graph), random_edge_nodes_expanded, elapsed_time,
         elapsed_process_time])
    return random_edges_stats

@numba.jit
def compute_cheapest_edges_stats(cheapest_edge_prob, cheapest_edge_heuristic, cheapest_edges_stats, size,
                                 problem_graph):
    start_time = time.time()
    start_process_time = time.process_time()
    cheapest_edge_solution = Search.astar_search(cheapest_edge_prob, cheapest_edge_heuristic).solution()[
        size - 1]
    cheapest_edge_nodes_expanded = cheapest_edge_prob.nodes_expanded()
    elapsed_process_time = time.process_time() - start_process_time
    elapsed_time = time.time() - start_time

    cheapest_edges_stats.append(
        [size, calc_cost(cheapest_edge_solution, problem_graph), cheapest_edge_nodes_expanded, elapsed_time,
         elapsed_process_time])
    return cheapest_edges_stats

@numba.jit
def compute_mst_stats(mst_prob, mst_heuristic, mst_stats, size, problem_graph):
    start_time = time.time()
    start_process_time = time.process_time()
    mst_solution = Search.astar_search(mst_prob, mst_heuristic).solution()[size - 1]
    mst_nodes_expanded = mst_prob.nodes_expanded()
    elapsed_process_time = time.process_time() - start_process_time
    elapsed_time = time.time() - start_time

    mst_stats.append(
        [size, calc_cost(mst_solution, problem_graph), mst_nodes_expanded, elapsed_time, elapsed_process_time])

    return mst_stats


def cleanup_old_analysis():
    ucs_file = open("csv_files/ucs.csv", 'w+')
    ucs_file.close()

    random_edge_file = open("csv_files/random_edges.csv", 'w+')
    random_edge_file.close()

    cheapest_edge_file = open("csv_files/cheapest_edges.csv", 'w+')
    cheapest_edge_file.close()

    mst_file = open("csv_files/mst.csv", 'w+')
    mst_file.close()


# Generate Graphs to perform A Star Search on
generate_graphs(5, 10, 1, 5)
# Clean up old csv files to perform new analysis
cleanup_old_analysis()
perform_A_Star_Search(5, 10, 1, 5)
