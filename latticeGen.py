"""
latticeGen.py
Desc: Functions to create various lattice patterns in 2D and 3D
"""
import math
import numpy as np
import matplotlib.pyplot as plt

import mathUtils


"""
# 2D GEN FUNCTIONS
"""

def square_2d(m, n):
    """
    Generates a square lattice pattern    
    :param m: rows of nodes
    :param n: columns of nodes
    """
    pass


def hex_2d(m, n, l, show=False):
    """
    Generates a hex lattice pattern of m by n nodes with constant beam length, l.
    Smallest setting of (1,1,1) will generate a diamond shape.
    :param m: rows of nodes
    :param n: columns of nodes
    :param l: length of lattice beam
    :param show: if enabled, will show console output
    """

    print('Running lattice gen hex_2d')

    grid_x = 2*n + 1
    grid_y = 2*m + 1
    grid = np.zeros((grid_y, grid_x))

    # create grid
    for x in range(grid_x):
        for y in range(grid_y):
            grid[y, x] = x+y
    for x in range(grid_x):
        for y in range(grid_y):
            if grid[y, x] % 2 == 0:
                grid[y, x] = 0
    grid[grid != 0] = 1

    # create value grid
    val_grid = np.zeros(grid.shape)
    primes = mathUtils.first_n_primes(grid_x, 0, 100) # TODO make sure max value is updated
    for y in range(grid_y):
        for x in range(grid_x):
            if y == 0:
                val_grid[y, x] = primes[x]
            elif x == 0:
                val_grid[y, x] = val_grid[y-1, x]*val_grid[y-1, x+1]
            elif x == grid_x-1:
                val_grid[y, x] = val_grid[y-1, x-1]*val_grid[y-1, x]
            else:
                val_grid[y, x] = val_grid[y-1, x-1]*val_grid[y-1, x+1]

    lattice_x = l*math.cos(math.radians(60))
    lattice_y = l*math.sin(math.radians(60))

    # Contains the lattice node X Y location tuples
    nodes = np.empty((grid_y, grid_x), dtype=object)
    node_ids = np.ones((grid_y, grid_x)) * -1

    for x in range(grid_x):
        for y in range(grid_y):
            if grid[y, x] == 1:
                nodes[y, x] = (x*lattice_x, y*lattice_y)
                node_ids[y, x] = val_grid[y, x]

    # turn arbitrary large numbers from value grid into sequence of unique numbers from 1
    node_ids_reduced = node_ids.copy()
    node_count = 0
    for x in range(node_ids.shape[0]):
        for y in range(node_ids.shape[1]):
            node_id = node_ids[x, y]
            if node_id != -1:
                node_ids_reduced[x, y] = node_count+1
                node_count += 1

    # list of node pairings to define a beam: [(node_id1, node_id2), (), ...]
    beams = []
    beam_ids = []

    # generate node parings resulting in lattice pattern
    for y in range(nodes.shape[0]):
        for x in range(nodes.shape[1]):
            node_id = node_ids[y, x]
            if node_id > 0:
                if y >= 1:
                    for X in range(nodes.shape[1]):
                        comp_node_id = node_ids[y-1, X]
                        if comp_node_id > 0:
                            if node_id % comp_node_id == 0:
                                node_location = np.where(node_ids == node_id)
                                comp_node_location = np.where(node_ids == comp_node_id)
                                beams.append((int(node_ids_reduced[node_location]), int(node_ids_reduced[comp_node_location])))

    for y in range(nodes.shape[0]):
        for x in range(nodes.shape[1]):
            node_id = node_ids[y, x]
            if node_id > 0:
                if y >= 1:
                    if x >= 2:
                        comp_node_id = node_ids[y, x-2]
                        if comp_node_id > 0:
                            node_location = np.where(node_ids == node_id)
                            comp_node_location = np.where(node_ids == comp_node_id)
                            beams.append((int(node_ids_reduced[node_location]), int(node_ids_reduced[comp_node_location])))

    # assign beam IDs
    for n in range(len(beams)):
        beam_ids.append(n+1)

    if show:
        print('Node value grid')
        print(val_grid)

        print('Node locations:')
        print(nodes)
        print('Node IDs:')
        print(node_ids_reduced)

        print('Beams:')
        print(beams)
        print('Beam IDs:')
        print(beam_ids)

        plot_2d(nodes, node_ids_reduced, beams, beam_ids)

    return nodes, node_ids_reduced, beams, beam_ids


def hex_2d_v2(m, n, l, show=False):
    """
    Version 2 of hex_2d()... actually works for lattice grids larger than mxn = 4x4
    Generates a hex lattice pattern of m by n nodes with constant beam length, l.
    Smallest setting of (1,1,1) will generate a diamond shape.
    :param m: rows of nodes
    :param n: columns of nodes
    :param l: length of lattice beam
    :param show: if enabled, will show console output
    """
    
    print('Running lattice gen hex_2d')

    grid_x = 2*n + 1
    grid_y = 2*m + 1
    grid = np.zeros((grid_y, grid_x))

    # create grid
    for x in range(grid_x):
        for y in range(grid_y):
            grid[y, x] = x+y
    for x in range(grid_x):
        for y in range(grid_y):
            if grid[y, x] % 2 == 0:
                grid[y, x] = 0
    grid[grid != 0] = 1

    # set node ids
    node_ids = grid.copy()
    node_count = 0
    for x in range(node_ids.shape[0]):
        for y in range(node_ids.shape[1]):
            node_id = node_ids[x, y]
            if node_id != 0:
                node_ids[x, y] = node_count+1
                node_count += 1

    # set node locations
    lattice_x = l*math.cos(math.radians(60))
    lattice_y = l*math.sin(math.radians(60))
    nodes = np.empty((grid_y, grid_x), dtype=object)
    for x in range(grid_x):
        for y in range(grid_y):
            if grid[y, x] == 1:
                nodes[y, x] = (x*lattice_x, y*lattice_y)

    # Set node pairings for beams
    beams = []
    for x in range(node_ids.shape[0]):
        for y in range(node_ids.shape[1]):
            node_id = node_ids[x, y]
            if node_id != 0:
                if y == 0: #create top row connections
                    beams.append((node_id, node_ids[x - 1, y + 1]))
                    beams.append((node_id, node_ids[x + 1, y + 1]))
                    beams.append((node_id, node_ids[x, y + 2]))
                elif y == node_ids.shape[1]-1:
                    beams.append((node_id, node_ids[x - 1, y - 1]))
                    beams.append((node_id, node_ids[x + 1, y - 1]))
                    beams.append((node_id, node_ids[x, y - 2]))
                elif y % 2 == 0:
                    beams.append((node_id, node_ids[x - 1, y + 1]))
                    beams.append((node_id, node_ids[x + 1, y + 1]))
                    beams.append((node_id, node_ids[x, y + 2]))
                    beams.append((node_id, node_ids[x - 1, y - 1]))
                    beams.append((node_id, node_ids[x + 1, y - 1]))
                    beams.append((node_id, node_ids[x, y - 2]))
                elif y < node_ids.shape[1]-2:
                    if 0 < x < node_ids.shape[0]-1:
                        beams.append((node_id, node_ids[x, y+2]))

    # remove duplicates from beam pairings:
    beams = list(set(beams))

    # Set beam IDs for each pairing
    beam_ids = []
    for n in range(len(beams)):
        beam_ids.append(n+1)
   
   
    # display read out 
    if show:
        print('Node locations:')
        print(nodes)
        print('Node IDs:')
        print(node_ids)
        print(node_ids.shape)
        print('Input Nodes:')
        print(node_ids[:, 0])
        print('Output Nodes:')
        print(node_ids[:, node_ids.shape[0]-1])

        print('Beams:')
        print(beams)
        print('Beam IDs:')
        print(beam_ids)

        plot_2d(nodes, node_ids, beams, beam_ids)

    return nodes, node_ids, beams, beam_ids



"""
# 3D GEN FUNCTIONS
"""

def hex_3d(m, n, j, l, show=False):

    print('Running lattice gen hex_3d')

    grid_x = 2*n + 1
    grid_y = 2*m + 1
    grid_z = 2*j + 1
    grid = np.zeros((grid_y, grid_x, grid_z))

    # create grid
    for x in range(grid_x):
        for y in range(grid_y):
            for z in range(grid_z):
                grid[x, y, z] = x+y+z+1
    for x in range(grid_x):
        for y in range(grid_y):
            for z in range(grid_z):
                if grid[x, y, z] % 2 == 0:
                    grid[y, x, z] = 0
    grid[grid != 0] = 1

    # Set node IDs:
    node_ids = grid.copy()
    node_count = 0
    for x in range(node_ids.shape[0]):
        for y in range(node_ids.shape[1]):
            for z in range(node_ids.shape[2]):
                node_id = node_ids[x, y, z]
                if node_id != 0:
                    node_ids[x, y, z] = node_count+1
                    node_count += 1

    # Set node locations (x, y, z)
    lattice_x = l*math.cos(math.radians(60))
    lattice_y = l*math.sin(math.radians(60))
    lattice_z = lattice_y
    nodes = np.empty((grid_x, grid_y, grid_z), dtype=object)
    for x in range(grid_x):
        for y in range(grid_y):
            for z in range(grid_z):
                if grid[x, y, z] == 1:
                    nodes[x, y, z] = (x*lattice_x, y*lattice_y, z*lattice_z)

    # Set node pairings for beams
    beams = [(6,9),(6,7),(6,8),(9,7),(9,8),(1,3),(3,4),(2,3),(3,5),(10,12),(11,12),(12,13),(12,14),(1,6),(2,6),(10,6),
             (11,6),(4,9),(5,9),(13,9),(14,9),(3,7),(3,8),(7,12),(8,12)]
    for x in range(node_ids.shape[0]):
        for y in range(node_ids.shape[1]):
            for z in range(node_ids.shape[2]):
                node_id = node_ids[x, y, z]
                if node_id != 0:
                    print(x, y, z)
                    #TODO: fix this
                    pass

    # remove duplicates from beam pairings:
    beams = list(set(beams))

    # Set beam IDs for each pairing
    beam_ids = []
    for n in range(len(beams)):
        beam_ids.append(n+1)

    # display read out
    if show:
        print('Node locations:')
        print(nodes)
        print('Node IDs:')
        print(node_ids)
        print(node_ids.shape)
        print('Input Nodes:')
        print(node_ids[:, 0, :])
        print('Output Nodes:')
        print(node_ids[:, node_ids.shape[0] - 1, :])

        #print('Beams:')
        #print(beams)
        #print('Beam IDs:')
        #print(beam_ids)

        plot_3d(nodes, node_ids, beams, beam_ids)

"""
# MISC FUNCTIONS
"""

def plot_2d(nodes, node_ids, beams=[], beam_ids=[]):
    # plot nodes:
    nodes_plot = np.empty((np.count_nonzero(nodes), 2))
    y_idx = 0
    for y in range(nodes.shape[0]):
        for x in range(nodes.shape[1]):
            node = nodes[y, x]
            node_id = node_ids[y, x]
            if node is not None:
                nodes_plot[y_idx, 0] = node[0]
                nodes_plot[y_idx, 1] = node[1]
                y_idx += 1
    x, y = nodes_plot.T
    plt.scatter(x, y)

    for beam in beams:
        n1 = nodes[np.where(node_ids == beam[0])]
        n2 = nodes[np.where(node_ids == beam[1])]
        x_val = [n1[0][0], n2[0][0]]
        y_val = [n1[0][1], n2[0][1]]
        plt.plot(x_val, y_val, 'bo', linestyle='-')

    plt.show()

def plot_3d(nodes, node_ids, beams=[], beam_ids=[]):
    # Plot nodes
    nodes_plot = np.empty((np.count_nonzero(nodes), 3))
    idx = 0
    for x in range(nodes.shape[0]) :
        for y in range(nodes.shape[1]):
            for z in range(nodes.shape[2]):
                node = nodes[x, y, z]
                node_id = node_ids[x, y, z]
                if node is not None:
                    nodes_plot[idx, 0] = node[0]
                    nodes_plot[idx, 1] = node[1]
                    nodes_plot[idx, 2] = node[2]
                    idx += 1
    x, y, z = nodes_plot.T
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(x, y, z)
    
    for beam in beams:
        n1 = nodes[np.where(node_ids == beam[0])]
        n2 = nodes[np.where(node_ids == beam[1])]
        x_val = [n1[0][0], n2[0][0]]
        y_val = [n1[0][1], n2[0][1]]
        z_val = [n1[0][2], n2[0][2]]
        plt.plot(x_val, y_val, z_val, 'bo', linestyle='-')

    plt.show()

if __name__ == '__main__':
    print('latticeGen.py debug...')
    #hex_2d(4, 4, 1, show=True)
    #hex_2d_v2(4, 4, 1, show=True)
    hex_3d(1, 1, 1, 1, show=True)
