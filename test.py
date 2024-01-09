import numpy as np
import trusspy as tp
from PyNite import FEModel3D
import latticeGen


def trusspy_test():
    M = tp.Model()
    E = 1           # Young's modulus
    A = 1           # Beam (element) area

    # create nodes
    with M.Nodes as MN:
        MN.add_node(1, (0, 0, 0))
        MN.add_node(2, (1, 0, 1))
        MN.add_node(3, (1, 0, 2))

    # create element
    with M.Elements as ME:
        ME.add_element(1, conn=[1, 2], gprop=[1])
        ME.add_element(2, conn=[2, 3], gprop=[1])
        ME.assign_material("all", [E])
        ME.assign_geometry("all", [A])

    # create displacement (U) boundary conditions
    with M.Boundaries as MB:
        MB.add_bound_U(1, (0, 0, 0))
        MB.add_bound_U(2, (1, 0, 0))
        MB.add_bound_U(3, (0, 0, 0))

    # create external forces
    with M.ExtForces as MF:
        MF.add_force(3, (1, 0, 2))

    # build model, run, show results
    M.build()
    fig, ax = M.plot_model()
    fig.show()
    M.run()

    # plot results of last increment
    M.plot_model(inc=-1, contour="force")


def trusspy_test_2():
    M = tp.Model(logfile=False)

    with M.Nodes as MN:
        MN.add_node(6, coord=(0, 0, 0))
        MN.add_node(3, coord=(1, 0, 1))
        MN.add_node(15, coord=(2, 0, 0))
        MN.add_node(90, coord=(1, 0, -1))

    with M.Elements as ME:
        ME.add_element(1, conn=(6, 3), gprop=[1])
        ME.add_element(2, conn=(3, 15), gprop=[1])
        ME.add_element(3, conn=(15, 90), gprop=[1])
        ME.add_element(4, conn=(90, 6), gprop=[1])
        ME.add_element(5, conn=(6, 15), gprop=[1])

        E = 1
        ME.assign_material("all", [E])

    with M.Boundaries as MB:
        MB.add_bound_U(1, (1, 0, 1))
        MB.add_bound_U(2, (0, 0, 0))
        MB.add_bound_U(3, (1, 0, 1))
        MB.add_bound_U(4, (0, 0, 0))

    with M.ExtForces as MF:
        MF.add_force(1, (0.01, 0, 0))

    M.Settings.incs = 100
    M.Settings.xlimit = (2, 0.5)
    M.Settings.dlpf
    M.Settings.stepcontrol = True
    M.Settings.maxfac = 4

    M.build()
    fig, ax = M.plot_model(inc=0)
    fig.show()

    M.run()

    fig, ax = M.plot_model(
        view="xz",
        contour="force",
        lim_scale=(-1, 3, -1, 3),
    )

    fig.show()

    fig, ax = M.plot_history(nodes=[1, 1], X="Displacement X", Y="LPF")

    fig.show()
    
def pynite_test():
    # Create a new finite element model
    beam = FEModel3D()

    # Add nodes (14 ft = 168 inches apart)
    beam.add_node('N1', 0, 0, 0)
    beam.add_node('N2', 168, 0, 0)


    # Define a material
    E = 29000  # Modulus of elasticity (ksi)
    G = 11200  # Shear modulus of elasticity (ksi)
    nu = 0.3  # Poisson's ratio
    rho = 2.836e-4  # Density (kci)
    beam.add_material('Steel', E, G, nu, rho)

    # Add a beam with the following properties:
    # Iy = 100 in^4, Iz = 150 in^4, J = 250 in^4, A = 20 in^2
    beam.add_member('M1', 'N1', 'N2', 'Steel', 100, 150, 250, 20)

    # Provide simple supports
    beam.def_support('N1', True, True, True, False, False, False)
    beam.def_support('N2', True, True, True, True, False, False)

    # Add a uniform load of 200 lbs/ft to the beam (from 0 in to 168 in)
    beam.add_member_dist_load('M1', 'Fy', -200 / 1000 / 12, -200 / 1000 / 12, 0, 168)

    # Alternatively the following line would do apply the load to the full
    # length of the member as well
    # beam.add_member_dist_load('M1', 'Fy', 200/1000/12, 200/1000/12)

    # Analyze the beam
    beam.analyze()

    # Print the shear, moment, and deflection diagrams
    beam.Members['M1'].plot_shear('Fy')
    beam.Members['M1'].plot_moment('Mz')
    beam.Members['M1'].plot_deflection('dy')

    # Print reactions at each end of the beam
    print('Left Support Reaction:', beam.Nodes['N1'].RxnFY, 'kip')
    print('Right Support Reacton:', beam.Nodes['N2'].RxnFY, 'kip')

    # Render the deformed shape of the beam magnified 100 times, with a text
    # height of 5 inches
    from PyNite.Visualization import Renderer
    renderer = Renderer(beam)
    renderer.annotation_size = 6
    renderer.deformed_shape = True
    renderer.deformed_scale = 100
    renderer.render_loads = True
    renderer.render_model()


def pynite_test_2():
    # Create a new finite element model
    beam = FEModel3D()

    # Add nodes (14 ft = 168 inches apart)
    beam.add_node('N1', 0, 0, 0)
    beam.add_node('N2', 168, 0, 0)
    beam.add_node('N3', 168/2, 168/2, 0)
    beam.add_node('N4', 168/2, -168/2, 0)

    # Define a material
    E = 29000  # Modulus of elasticity (ksi)
    G = 11200  # Shear modulus of elasticity (ksi)
    nu = 0.3  # Poisson's ratio
    rho = 2.836e-4  # Density (kci)
    beam.add_material('Steel', E, G, nu, rho)

    # Add a beam with the following properties:
    # Iy = 100 in^4, Iz = 150 in^4, J = 250 in^4, A = 20 in^2
    beam.add_member('M1', 'N1', 'N2', 'Steel', 100, 150, 250, 20)
    beam.add_member('M2', 'N1', 'N3', 'Steel', 100, 150, 250, 20)
    beam.add_member('M3', 'N1', 'N4', 'Steel', 100, 150, 250, 20)
    beam.add_member('M4', 'N2', 'N3', 'Steel', 100, 150, 250, 20)
    beam.add_member('M5', 'N2', 'N4', 'Steel', 100, 150, 250, 20)


    # Provide simple supports
    beam.def_support('N3', True, True, True, False, False, False)
    beam.def_support('N4', True, True, True, True, False, False)

    # Add a uniform load of 200 lbs/ft to the beam (from 0 in to 168 in)
    #beam.add_member_dist_load('M1', 'Fy', -200 / 1000 / 12, -200 / 1000 / 12, 0, 168)
    beam.add_node_load('N1', 'FX', P=1000)

    # Alternatively the following line would do apply the load to the full
    # length of the member as well
    # beam.add_member_dist_load('M1', 'Fy', 200/1000/12, 200/1000/12)

    # Analyze the beam
    beam.analyze()

    # Print the shear, moment, and deflection diagrams
    beam.Members['M1'].plot_shear('Fy')
    beam.Members['M1'].plot_moment('Mz')
    beam.Members['M1'].plot_deflection('dy')

    # Print reactions at each end of the beam
    print('Left Support Reaction:', beam.Nodes['N1'].RxnFY, 'kip')
    print('Right Support Reacton:', beam.Nodes['N2'].RxnFY, 'kip')

    # Render the deformed shape of the beam magnified 100 times, with a text
    # height of 5 inches
    from PyNite.Visualization import Renderer
    renderer = Renderer(beam)
    renderer.annotation_size = 6
    renderer.deformed_shape = True
    renderer.deformed_scale = 100
    renderer.render_loads = True
    renderer.render_model()
    
if __name__ == '__main__':
    #pynite_test()
    pynite_test_2()
