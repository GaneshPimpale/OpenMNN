import numpy as np
import scipy as sp
import pygad

import latticeGen
import latticeSolver


"""
### Helper Functions
"""
def euc_dist(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)


def mse_3d(y, y_h):
    Sum = 0
    for idx, p in enumerate(y):
        p_h = y_h[idx]
        e_d = euc_dist(p, p_h)
        Sum += e_d**2
    return Sum/len(y)

"""
### Topology Opt 
"""

class TopOpt:

    def __int__(self):
        ### Lattice parameters
        m = 1  # number of input nodes
        n = 1  # number of lattice layers
        l = 200  # init distance between nodes
        ### End of lattice parameters

        nodes, node_ids, beams, beam_ids = latticeGen.hex_2d_v2(m, n, l, show=False)

        ### Model parameters
        # List of E_vals to optimize
        E_def = 29000  # default starting E value
        self.E_values = [E_def] * len(beam_ids)
        print(str(len(self.E_values)) + ' E values of lattice')

        # Input vectors; len(input_vecs) = m; (x,y,z)
        input_vecs = [(4000, 0, 0)]

        # Output nodes; len(output_nodes) = m
        output_nodes = node_ids[:, node_ids.shape[0] - 1][node_ids[:, node_ids.shape[0] - 1] != 0]

        # Desired output node displacement; (x, y, z)
        fin_disp = [(5, 0, 0)]

        des_mse = 1  # Desired MSE value
        ### End of model parameters

        # Solve lattice and produce output node locations
        self.disp, self.pos, self.M = latticeSolver.solve_pynite_2d(
            nodes, node_ids, beams, beam_ids, self.E_values, input_vecs, output_nodes, show_vis=True, show=True
        )

        print('Initial MSE: ' + str(mse_3d(self.disp, fin_disp)))
        print('Minimum MSE: ' + str(des_mse))



    def assemble_stiffness_matrix(self):
        K0 = self.M['global_stiffness'].toarray()
        f = self.M['force_vec']
        d0 = self.M['disp_vec']

        Ki = np.gradient(K0)
        Kij = np.gradient(Ki)

        f_psuedo = Ki*d0



    def evaluate_statistical_analysis(self, ):
        pass

    def compute_sensitivity(self, ):
        pass

    def gradient_descent(self):
        pass

    def run(self):
        pass






def solve_E_single_gradient_des():
    ### Lattice parameters
    m = 1  # number of input nodes
    n = 1  # number of lattice layers
    l = 200  # init distance between nodes
    ### End of lattice parameters

    nodes, node_ids, beams, beam_ids = latticeGen.hex_2d_v2(m, n, l, show=False)

    ### Model parameters
    # List of E_vals to optimize
    E_def = 29000  # default starting E value
    E_values = [E_def] * len(beam_ids)
    print(str(len(E_values)) + ' E values of lattice')

    # Input vectors; len(input_vecs) = m; (x,y,z)
    input_vecs = [(4000, 0, 0)]

    # Output nodes; len(output_nodes) = m
    output_nodes = node_ids[:, node_ids.shape[0] - 1][node_ids[:, node_ids.shape[0] - 1] != 0]

    # Desired output node displacement; (x, y, z)
    fin_disp = [(5, 0, 0)]

    des_mse = 1  # Desired MSE value
    ### End of model parameters
    
    # Solve lattice and produce output node locations
    disp, pos, M = latticeSolver.solve_pynite_2d(
        nodes, node_ids, beams, beam_ids, E_values, input_vecs, output_nodes, show_vis=True, show=True
    )

    print('Initial MSE: ' + str(mse_3d(disp, fin_disp)))
    print('Minimum MSE: ' + str(des_mse))

    g_stiffness_mat = M['global_stiffness'].toarray()
    print(M['disp_vec'])
    comp_force = g_stiffness_mat * M['disp_vec']
    node_disp = comp_force * np.linalg.inv(g_stiffness_mat)
    print(node_disp)



if __name__ == '__main__':
    solve_E_single_gradient_des()

