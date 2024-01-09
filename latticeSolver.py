import numpy as np

import trusspy as tp
from PyNite import FEModel3D
from PyNite.Visualization import Renderer

import latticeGen


def solve_trusspy_2d(nodes, node_ids, beams, beam_ids, E_vals, I, output_nodes, show=False):
    """
    Given a node beam pattern, young moduli, and Input force vectors, solve for the
    
    :param nodes: array of node locations
    :param node_ids: array of node IDs in position
    :param beams: array of beam node to node connctions
    :param beam_ids: list of beam ICs
    :param E_vals: list of Young moduli of each beam
    :param I: input list of force vectors
    :param show: show console output and plots
    :return: displacement of output nodes
    """
    
    M = tp.Model()
    E = 10           # Young's modulus
    A = 10           # Beam (element) area


    # Set nodes in trusspy solver
    with M.Nodes as MN:
        if show:
            print('Creating Nodes...')
        for y in range(nodes.shape[0]):
            for x in range(nodes.shape[1]):
                node = nodes[y, x]
                node_id = node_ids[y, x]
                if node is not None:
                    MN.add_node(int(node_id), (node[0], 0, node[1]))
                    if show:
                        print('Created node ' + str(node_id) + " at " + str(node))
        if show:
            print('Node Creation Complete')
            print()

    # create elements (beams)
    with M.Elements as ME:
        if show:
            print('Creating Beams...')
        for beam_id in beam_ids:
            beam = beams[beam_id-1]
            ME.add_element(beam_id, conn=(beam[0], beam[1]), gprop=[1])
            if show:
                print('Created beam ' + str(beam_id) + " from node " + str(beam[0]) + " to noode " + str(beam[1]))
        ME.assign_material("all", [E])
        ME.assign_geometry("all", [A])
        if show:
            print('Beam Creation Complete')
            print()

    # create displacement boundary conditions
    with M.Boundaries as MB:
        if show:
            print('Setting Node Boundaries...')
        for y in range(nodes.shape[0]):
            for x in range(nodes.shape[1]):
                #node = nodes[x, y]
                node_id = node_ids[y, x]

                if node_id > 0:
                    if y == 0:
                        MB.add_bound_U(node_id, (0, 0, 0))
                        if show:
                            print('Set node ' + str(node_id) + " to locked node")
                    elif y == nodes.shape[1]-1:
                        MB.add_bound_U(node_id, (0, 0, 0))
                        if show:
                            print('Set node ' + str(node_id) + " to locked node")
                    else:
                        MB.add_bound_U(node_id, (1, 0, 1))
                        if show:
                            print('Set node ' + str(node_id) + " to free node")

        if show:
            print('Boundary Setting Complete')
            print()

    # create external forces
    with M.ExtForces as MF:
        if len(I) != (node_ids.shape[0]-1)/2:
            raise Exception('Input force list length must be equal to the number of input nodes (m)')
        force_count = 0
        if show:
            print('Creating Forces')
        for y in range(nodes.shape[0]):
            node_id = node_ids[y, 0]
            if node_id > 0:
                MF.add_force(node_id, I[force_count])
                force_count += 1
                if show:
                    print('Added on force on node ' + str(node_id))
        if show:
            print('Force Setting Complete')

    # Set runtime setitngs
    M.Settings.incs = 100
    M.Settings.xlimit = (2, 0.5)
    M.Settings.dlpf
    M.Settings.stepcontrol = True
    M.Settings.maxfac = 4
    
    # build model, show build
    M.build()
    if show:
        fig, ax = M.plot_model(inc=0)
        fig.show()

    # Run model, show results
    M.run()
    if show:
        fig, ax = M.plot_model(
            view="xz",
            contour="force",
            lim_scale=(-1, 5, -0.5, 10),
        )
        fig.show()

    # Get the displacement of the output nodes post run
    output_node_disp = []
    for node in output_nodes:
        output_node_disp.append(
            np.array(M.Results.R[-1].U[np.where(M.Nodes.labels == node)]).tolist()
        )

    if show:
        print('Input forces:')
        print(I)
        print('Output Node Displacement:')
        print(output_node_disp)
        fig2, ax2 = M.plot_history(nodes=[1, 1], X='Displacement X', Y='Displacement Z')
        for node in output_nodes:
            fig2, ax2 = M.plot_history(nodes=[node, node], X='Displacement X', Y='Displacement Z', fig=fig2, ax=ax2)
        fig2.show()

    return output_node_disp


def solve_pynite_2d(nodes, node_ids, beams, beam_ids, E_vals, I, output_nodes, show_vis=False, show=False):
    """
    Solves a 2D lattice pattern with pynite FEA solver.

    :param nodes: Array of node locations as tuples
    :param node_ids: Array of node IDs associated with node locations
    :param beams: List of tuples containing beam connecting two node IDs
    :param beam_ids: List of ICs for beams associated to Beam list
    :param E_vals: List of Young moduli associated with Beam list
    :param I: List of vectors for the input vectors
    :param output_nodes: List of node IDs of
    :param show: if True shows console read out, plots and visualizations
    :return: list of displacement vectors for each output node
    :return: list of position coordinates for each output node
    :return: Model's global stiffness matrix'
    """

    M = FEModel3D()

    # Set nodes:
    if show:
        print('Creating Nodes...')
    for y in range(nodes.shape[0]):
        for x in range(nodes.shape[1]):
            node = nodes[y, x]
            node_id = node_ids[y, x]
            if node is not None:
                M.add_node(name=str(node_id), X=node[0], Y=node[1], Z=0)
                if show:
                    print('Created node ' + str(node_id) + " at " + str(node))
    if show:
        print('Node Creation Complete')
        print()

    # Create a specific material for each beam
    # TODO: these values are temporary
    #E = 29000  # Modulus of elasticity (ksi)
    G = 11200  # Shear modulus of elasticity (ksi)
    nu = 0.3  # Poisson's ratio
    rho = 2.836e-4  # Density (kci)
    for idx, E in enumerate(E_vals):
        beam_id = beam_ids[idx]
        M.add_material(name=str(beam_id), E=E, G=G, nu=nu, rho=rho)
        if show:
            print('Created material for beam ' + str(beam_id) + ' E='
                  + str(E) + '; G=' + str(G) + '; nu=' + str(nu) + '; rho=' + str(rho))

    # Create beams:
    if show:
        print('Creating Beams...')
    for beam_id in beam_ids:
        beam = beams[beam_id - 1]
        # TODO: Change material setting of beam
        M.add_member(name=str(beam_id), i_node=str(beam[0]), j_node=str(beam[1]), material=str(beam_id), Iy=100, Iz=150, J=250, A=20)
        if show:
            print('Created beam ' + str(beam_id) + " from node " + str(beam[0]) + " to node " + str(beam[1]))
    if show:
        print('Beam Creation Complete')
        print()

    # Set lattice boundaries:
    if show:
        print('Setting Node Boundaries...')
    for y in range(nodes.shape[0]):
        for x in range(nodes.shape[1]):
            # node = nodes[x, y]
            node_id = node_ids[y, x]

            if node_id > 0:
                if y == 0:
                    M.def_support(
                        node_name=str(node_id), 
                        support_DX=True, 
                        support_DY=True, 
                        support_DZ=True, 
                        support_RX=True, 
                        support_RY=True, 
                        support_RZ=True
                    )
                    if show:
                        print('Set node ' + str(node_id) + " to locked node")
                elif y == nodes.shape[1] - 1:
                    M.def_support(
                        node_name=str(node_id), 
                        support_DX=True, 
                        support_DY=True, 
                        support_DZ=True, 
                        support_RX=True, 
                        support_RY=True, 
                        support_RZ=True
                    )
                    if show:
                        print('Set node ' + str(node_id) + " to locked node")
                else:
                    if show:
                        print('Set node ' + str(node_id) + " to free node")
    if show:
        print('Boundary Setting Complete')
        print()


    # Set input forces:
    if len(I) != (node_ids.shape[0] - 1) / 2:
        raise Exception('Input force list length must be equal to the number of input nodes (m)')
    force_count = 0
    if show:
        print('Creating Forces')
    for y in range(nodes.shape[0]):
        node_id = node_ids[y, 0]
        if node_id > 0:
            force = I[force_count]
            M.add_node_load(Node=str(node_id), Direction='FX', P=force[0])
            M.add_node_load(Node=str(node_id), Direction='FY', P=force[1])
            M.add_node_load(Node=str(node_id), Direction='FZ', P=force[2])
            force_count += 1
            if show:
                print('Added on force on node ' + str(node_id))
    if show:
        print('Force Setting Complete')
        print()

    # Run analysis
    if show:
        print('Running Analysis...')
    M.analyze()
    if show:
        print('Analysis Complete')

    if show_vis:
        renderer = Renderer(M)
        renderer.annotation_size = 6
        renderer.deformed_shape = True
        renderer.deformed_scale = 100
        renderer.render_loads = True
        # TODO: Create separate renders for the pre and post deformed shape
        renderer.render_model()

    # Return output node locations
    output_node_fin_pos = []
    output_node_disp = []
    for node in output_nodes:
        model_node = M.Nodes[str(node)]
        new_pos = (model_node.DX['Combo 1'], model_node.DY['Combo 1'], model_node.DZ['Combo 1'])
        output_node_disp.append(new_pos)

    # Find output node final locations
    for idx, disp in enumerate(output_node_disp):
        node = output_nodes[idx]
        ori_pos = nodes[np.where(node_ids == node)]
        new_pos = (ori_pos[0][0]+disp[0], ori_pos[0][1]+disp[1])
        output_node_fin_pos.append(new_pos)

    if show:
        print('Input forces:')
        print(I)
        print('Output Node Positions:')
        print(output_node_fin_pos)
        print('Output Node Displacement:')
        print(output_node_disp)

        # TODO: Add displacement graph

    # Global stiffness matrix, geometric stiffness matrix
    Mats = {
        'global_stiffness': M.K(),
        'geometric_stiffness': M.Kg(),
        'force_vec': M.P(),
        'disp_vec': M.D()
    }

    return output_node_disp, output_node_fin_pos, Mats


def solve_pynite_3d():
    pass


if __name__ == "__main__":
    nodes, node_ids, beams, beam_ids = latticeGen.hex_2d_v2(4, 4, 200, show=False)

    E_values = []
    for id in beam_ids:
        E_values.append(19000)

    input_vecs = [(4000, 0, 0), (4000, 0, 0), (4000, 0, 0), (4000, 0, 0)]
    input_vec_1 = [(400, 0, 0)]
    output_nodes = node_ids[:, node_ids.shape[0]-1][node_ids[:, node_ids.shape[0]-1] != 0]

    #solve_trusspy_2d(nodes, node_ids, beams, beam_ids, E_values, input_vecs, output_nodes, show=True)
    solve_pynite_2d(nodes, node_ids, beams, beam_ids, E_values, input_vecs, output_nodes, show_vis=True, show=True)

