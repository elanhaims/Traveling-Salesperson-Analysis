from Calculate_A_Star_Stats_New import calculate_stats
from AStar import perform_A_Star_Search


if __name__ == "__main__":
    min_graph_size = int(input("Enter the starting graph size:"))
    max_graph_size = int(input("Enter the maximum graph size (Uniform Cost Search can only handle graphs up to size 8 "
                               "in reasonable time):"))
    increment = int(input("Enter the increment between graphs sizes:"))
    number_of_graphs = int(input("Enter the number of graphs that should be tested for each graph size:"))

    # Generates all of the graphs and solves the traveling salesperson problem on all of them
    perform_A_Star_Search(min_graph_size, max_graph_size, increment, number_of_graphs)

    print("Now performing analysis on the data from the graphs")

    calculate_stats()
