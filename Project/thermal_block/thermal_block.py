# This file performs a Reduced Basis simulation for a backward facing step
# described in the project presentation.
# The file has been adopted and modified from RBnics tutorials available
# at <https://gitlab.com/RBniCS/RBniCS>.

from dolfin import *
from rbnics import *

class ThermalBlock(EllipticCoerciveCompliantProblem):

    # Default initialization of members
    def __init__(self, V, **kwargs):
        # Call the standard initialization
        EllipticCoerciveCompliantProblem.__init__(self, V, **kwargs)
        # Store FEniCS data structures for assembly
        assert "subdomains" in kwargs
        assert "boundaries" in kwargs
        self.subdomains, self.boundaries = kwargs["subdomains"], kwargs["boundaries"]
        self.u = TrialFunction(V)
        self.v = TestFunction(V)
        self.dx = Measure("dx")(subdomain_data=self.subdomains)
        self.ds = Measure("ds")(subdomain_data=self.boundaries)

    # Return the alpha_lower bound.
    def get_stability_factor_lower_bound(self):
        return min(self.compute_theta("a"))

    # Return theta multiplicative terms of the affine expansion of the problem.
    def compute_theta(self, term):
        mu = self.mu
        if term == "a":
            theta_a0 = mu[0]
            theta_a1 = 1.
            return (theta_a0, theta_a1)
        elif term == "f":
            theta_f0 = mu[1]
            return (theta_f0,)
        else:
            raise ValueError("Invalid term for compute_theta().")

    # Return forms resulting from the discretization of the affine expansion of the problem operators.
    def assemble_operator(self, term):
        v = self.v
        dx = self.dx
        if term == "a":
            u = self.u
            a0 = inner(grad(u), grad(v))*dx(1)
            a1 = inner(grad(u), grad(v))*dx(2)
            return (a0, a1)
        elif term == "f":
            ds = self.ds
            f0 = v*ds(1)
            return (f0,)
        elif term == "dirichlet_bc":
            bc0 = [DirichletBC(self.V, Constant(0.0), self.boundaries, 3)]
            return (bc0,)
        elif term == "inner_product":
            u = self.u
            x0 = inner(grad(u), grad(v))*dx
            return (x0,)
        else:
            raise ValueError("Invalid term for assemble_operator().")

# 1. Read the mesh for this problem
mesh = Mesh("data/thermal_block.xml")
subdomains = MeshFunction("size_t", mesh, "data/thermal_block_physical_region.xml")
boundaries = MeshFunction("size_t", mesh, "data/thermal_block_facet_region.xml")

# 2. Create Finite Element space (Lagrange P1)
V = FunctionSpace(mesh, "Lagrange", 1)

# 3. Allocate an object of the ThermalBlock class
thermal_block_problem = ThermalBlock(V, subdomains=subdomains, boundaries=boundaries)
mu_range = [(0.1, 10.0), (-1.0, 1.0)]
thermal_block_problem.set_mu_range(mu_range)

# 4. Prepare reduction with a reduced basis method
reduced_basis_method = ReducedBasis(thermal_block_problem)
reduced_basis_method.set_Nmax(10)
reduced_basis_method.set_tolerance(1e-5)

# 5. Perform the offline phase
reduced_basis_method.initialize_training_set(100)               # Create a uniformly distributed training set for basis functions
reduced_thermal_block_problem = reduced_basis_method.offline()

# 6. Perform an online solve
online_mu = (8.0, -1.0)                                         # Parameter value the model needs to be solved for
reduced_thermal_block_problem.set_mu(online_mu)
reduced_thermal_block_problem.solve()
reduced_thermal_block_problem.export_solution(filename="online_solution")
#plot(reduced_solution, reduced_problem=reduced_thermal_block_problem)

# 7. Perform an error analysis
reduced_basis_method.initialize_testing_set(100)                # Create a uniformly distributed testing set for error analysis
reduced_basis_method.error_analysis()

# 8. Perform a speedup analysis
reduced_basis_method.initialize_testing_set(100)                # Create a uniformly distributed testing set for speedup
reduced_basis_method.speedup_analysis()
