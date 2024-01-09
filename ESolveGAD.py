import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import pygad


import latticeGen
import latticeSolver

def euc_dist(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)


def mse_3d(y, y_h):
    Sum = 0
    for idx, p in enumerate(y):
        p_h = y_h[idx]
        e_d = euc_dist(p, p_h)
        Sum += e_d**2
    return Sum/len(y)

def list_to_x_y(List):
    x = []
    y = []
    for count, item in enumerate(List):
        x.append(count)
        y.append(item)
    x_arr = np.array(x)
    y_arr = np.array(y)
    return x_arr, y_arr


def solve_E_single_input_gad():
    """
    Solve for list of E_values such that MSE is less that minimum MSE value using a genetic algorithm with
    the following parameters:
    - Single input vector
    - Single output node
    - Single final displacement location
    :return: Optimized E_values list 
    """

    ### Lattice parameters
    m = 1  # number of input nodes
    n = 1  # number of lattice layers
    l = 200  # init distance between nodes
    ### End of lattice parameters

    nodes, node_ids, beams, beam_ids = latticeGen.hex_2d_v2(m, n, l, show=False)

    ### Model Parameters
    # List of E_vals to optimize
    E_def = 29000  # default starting E value
    E_values = [E_def] * len(beam_ids)
    print(str(len(E_values)) + ' E values of lattice')

    # Input vectors; len(input_vecs) = m; (x,y,z)
    input_vecs = [(4000, 0, 0)]

    # Output nodes; len(output_nodes) = m
    output_nodes = node_ids[:, node_ids.shape[0] - 1][node_ids[:, node_ids.shape[0] - 1] != 0]

    # Desired output node displacement; (x, y, z)
    fin_disp = [(2.5, 0, 0)]

    min_mse = 0
    ### End of Model parameters

    # Solve lattice and produce output node locations
    disp, pos, K = latticeSolver.solve_pynite_2d(
        nodes, node_ids, beams, beam_ids, E_values, input_vecs, output_nodes, show_vis=True, show=True
    )

    print('Initial MSE: ' + str(mse_3d(disp, fin_disp)))
    print('Minimum MSE: ' + str(min_mse))

    def lattice_func(e_vals):
        disp, pos, K = latticeSolver.solve_pynite_2d(
            nodes, node_ids, beams, beam_ids, e_vals, input_vecs, output_nodes
        )
        mse = mse_3d(disp, fin_disp)
        return mse

    def fitness_func(ga_instance, solution, solution_idx):
        mse = lattice_func(solution)
        fitness = 1.0/np.abs(mse - min_mse)
        return fitness

    # PyGAD settings
    fitness_function = fitness_func
    num_generations = 20
    num_parents_mating = 4
    sol_per_pop = 8
    num_genes = len(E_values)
    init_range_low = 0
    init_range_high = 29000
    parent_selection_type = "sss"
    keep_parents = 1
    crossover_type = "single_point"
    mutation_type = "random"
    mutation_percent_genes = 10

    # Create PyGAD Instance
    ga_instance = pygad.GA(num_generations=num_generations,
                           num_parents_mating=num_parents_mating,
                           fitness_func=fitness_function,
                           sol_per_pop=sol_per_pop,
                           num_genes=num_genes,
                           init_range_low=init_range_low,
                           init_range_high=init_range_high,
                           parent_selection_type=parent_selection_type,
                           keep_parents=keep_parents,
                           crossover_type=crossover_type,
                           mutation_type=mutation_type,
                           mutation_percent_genes=mutation_percent_genes)

    # Run PyGAD instance
    ga_instance.run()
    solution, solution_fitness, solution_idx = ga_instance.best_solution()

    # PyGAD results
    print("Parameters of the best solution : {solution}".format(solution=solution))
    print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
    prediction = lattice_func(solution)
    print("Predicted output based on the best solution : {prediction}".format(prediction=prediction))

    disp, pos, K = latticeSolver.solve_pynite_2d(
        nodes, node_ids, beams, beam_ids, solution, input_vecs, output_nodes, show_vis=True, show=True
    )

    print('Final MSE: ' + str(mse_3d(disp, fin_disp)))
    print('Output node final locations:')
    print(pos)
    print('Output node displacements:')
    print(disp)
    print('Optimized E_values:')
    print(E_values)

    return E_values


def solve_E_multi_input_gad():
    """
    Solve for list of E_values such that MSE is less that minimum MSE value using a genetic algorithm and the
    following boundary conditions:
    - Single set of input vectors
    - Single set of output nodes = m
    - Singe set of final displacement locations
    :return: Optimized E_values list
    """

    ### Lattice parameters
    m = 4  # number of input nodes
    n = 4  # number of lattice layers
    l = 200  # init distance between nodes
    ### End of lattice parameters

    nodes, node_ids, beams, beam_ids = latticeGen.hex_2d_v2(m, n, l, show=False)

    ### Model parameters
    # List of E_vals to optimize
    E_def = 29000  # default starting E value
    E_values = [E_def] * len(beam_ids)
    print(str(len(E_values)) + ' E values of lattice')

    # Input vectors; len(input_vecs) = m; (x,y,z)
    input_vecs = [(4000, 0, 0), (4000, 0, 0), (4000, 0, 0), (4000, 0, 0)]

    # Output nodes; len(output_nodes) = m
    output_nodes = node_ids[:, node_ids.shape[0] - 1][node_ids[:, node_ids.shape[0] - 1] != 0]

    # Desired output node displacement; (x, y, z)
    fin_disp = [(-3, 0, 0), (0, 0, 0), (3, 0, 0), (0, 0, 0)]

    des_mse = 1  # Desired MSE value
    ### End of model parameters

    # Solve lattice and produce output node locations
    disp, pos, K = latticeSolver.solve_pynite_2d(
        nodes, node_ids, beams, beam_ids, E_values, input_vecs, output_nodes, show_vis=True, show=True
    )
    print('Initial MSE: ' + str(mse_3d(disp, fin_disp)))
    print('Minimum MSE: ' + str(des_mse))


    def lattice_func(e_vals):
        disp, pos, K = latticeSolver.solve_pynite_2d(
            nodes, node_ids, beams, beam_ids, e_vals, input_vecs, output_nodes
        )
        mse = mse_3d(disp, fin_disp)
        return mse

    # PyGAD Tracing plots
    mse_ouputs = []
    fitness_ouputs = []

    def fitness_func(ga_instance, solution, solution_idx):
        mse = lattice_func(solution)
        fitness = (1.0/np.abs(mse - des_mse)+0.00000001)
        mse_ouputs.append(mse)
        fitness_ouputs.append(fitness)
        print('MSE:' + str(mse) + ' Fitness:' + str(fitness))
        return fitness

    # PyGAD parameters
    fitness_function = fitness_func
    num_generations = 20
    num_parents_mating = 6
    sol_per_pop = 8
    num_genes = len(E_values)
    init_range_low = 0
    init_range_high = 500000
    parent_selection_type = "sss"
    keep_parents = 1
    crossover_type = "single_point"
    mutation_type = "random"
    mutation_percent_genes = 10

    # Create PyGAD instance:
    ga_instance = pygad.GA(num_generations=num_generations,
                           num_parents_mating=num_parents_mating,
                           fitness_func=fitness_function,
                           sol_per_pop=sol_per_pop,
                           num_genes=num_genes,
                           init_range_low=init_range_low,
                           init_range_high=init_range_high,
                           parent_selection_type=parent_selection_type,
                           keep_parents=keep_parents,
                           crossover_type=crossover_type,
                           mutation_type=mutation_type,
                           mutation_percent_genes=mutation_percent_genes
                           )

    print('Running Genetic Algorithm...')
    ga_instance.run()

    solution, solution_fitness, solution_idx = ga_instance.best_solution()
    print("Parameters of the best solution : {solution}".format(solution=solution))
    print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

    prediction = lattice_func(solution)
    print("Predicted output based on the best solution : {prediction}".format(prediction=prediction))

    # Create mse and fitness plots
    x_mse, y_mse = list_to_x_y(mse_ouputs)
    x_fit, y_fit = list_to_x_y(fitness_ouputs)
    plt.scatter(x_mse, y_mse, color='red')
    plt.scatter(x_fit, y_fit, color='blue')
    plt.show()

    # Display the optimized lattice structure under load
    E_values = solution
    disp, pos, K = latticeSolver.solve_pynite_2d(
        nodes, node_ids, beams, beam_ids, E_values, input_vecs, output_nodes, show_vis=True, show=False
    )

    print('Final MSE:')
    print(mse_3d(disp, fin_disp))
    print('Output node final locations:')
    print(pos)
    print('Output node displacements:')
    print(disp)
    print('Optimized E_values:')
    print(E_values)

    return E_values


def solve_E_multi_gacnn():
    ### Lattice parameters
    m = 4  # number of input nodes
    n = 4  # number of lattice layers
    l = 200  # init distance between nodes
    ### End of lattice parameters

    nodes, node_ids, beams, beam_ids = latticeGen.hex_2d_v2(m, n, l, show=False)

    ### Model parameters
    # List of E_vals to optimize
    E_def = 29000  # default starting E value
    E_values = [E_def] * len(beam_ids)
    print(str(len(E_values)) + ' E values of lattice')

    # Input vectors; len(input_vecs) = m; (x,y,z)
    input_vecs = [(4000, 0, 0), (4000, 0, 0), (4000, 0, 0), (4000, 0, 0)]

    # Output nodes; len(output_nodes) = m
    output_nodes = node_ids[:, node_ids.shape[0] - 1][node_ids[:, node_ids.shape[0] - 1] != 0]

    # Desired output node displacement; (x, y, z)
    fin_disp = [(5, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]

    des_mse = 1  # Desired MSE value
    ### End of model parameters




if __name__ == '__main__':
    #solve_E_single_input_gad()
    solve_E_multi_input_gad()

