import regli_assignment_ggen


def generate_graphs(min_size=5, max_size=30, increment=1, number_of_graphs=10) -> None:
    for size in range(min_size, max_size + 1, increment):
        for x in range(number_of_graphs):
            graph = regli_assignment_ggen.create_complete_symmetric_graphs(size)
            regli_assignment_ggen.create_final_output(graph, size, x)

#generate_graphs(5,9,1, 30)
