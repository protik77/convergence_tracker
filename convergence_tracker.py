from ase.io import read
from pymatgen.io.ase import AseAtomsAdaptor
from math import ceil
from ase.calculators.vasp import Vasp

class ConvergenceTracker():
    ''' Class for tracking convergence.

    The class takes three inputs. These are
    structure_path: path of structure along with the structure name. Default
    is a POSCAR file in the current directory
    cutoff: energy cutoff. If not provided, default is 550eV which is enough for
    most pseudopotentials in vasp
    calculator: DFT tool to be used for the convergence. Default is vasp. For
    other calculators, will raise NotImplementedError.
    '''

    def __init__(self, structure_path='POSCAR', calculator='vasp', convergence_th=1E-3, cutoff=550):

        self.calculator = calculator
        self.convergence_th = convergence_th
        self.structure_path = structure_path
        self.cutoff = cutoff  # in eV
        self.max_iter = 500 # maximum number of iteration

    def read_structure(self):
        ''' Reads structure from the path given

        ase.io.read function will be used to read the structure.
        WIll support all structure formats supported by ASE.
        '''

        return read(self.structure_path)

    def get_lattice_constants(self):
        ''' Returns lattice constants as a list

        '''

        ase_struct = self.read_structure()

        # convert ase object to pymatgen object
        pmg_struct = AseAtomsAdaptor.get_structure(ase_struct)

        lattice_constants = list(pmg_struct.lattice.abc)

        # convert numpy data types to float to be consistent
        lattice_constants = [float(a) for a in lattice_constants]

        return lattice_constants

    def scale_kpoints(self):
        ''' Will return a list with scaling of correspondin k-point.

        If the lattice constant of the structure in any direction is twice or
        larger compared to any other direction, then k-points needed for that
        direction is half. This function will check for such properties and
        returns a list for scaling the k-points.
        '''

        lat_const = self.get_lattice_constants()

        return [ceil(z / min(lat_const)) for z in lat_const]

    def get_new_kpoints(self, old_kpoints, scaling_factor, inc=2):
        '''Gets new k-points from old k-points by increasing from the earlier
        values and scaling the k-points using the scaling_factor.

        '''

        new_max = max(old_kpoints) + inc

        new_kpoints = [ceil(new_max / a) for a in scaling_factor]

        return new_kpoints

    def create_calculator(self):
        '''Creates calculator object using ASE.

        Reads mode from the calculator input and creates a calculator object
        with default parameters. In case changes needed in the default
        parameters, this class can be sub-classed.
        If the calculator is not supported, NotImplementedError is raised.
        '''

        if self.calculator == 'vasp':
            calc_obj = Vasp(pp='pbe',
                    istart=0,
                    ismear=1,
                    sigma=0.05,
                    lcharg=False,
                    lwave=False,
                    encut = self.cutoff,
                    algo='Normal',
                    nelm=200,
                    ediff=1e-6,
                    ibrion=-1,
                    nsw=0,
                    gamma=True)

        else:
            raise NotImplementedError('Calculator {} not implemented.'.format(self.calculator))

        return calc_obj

    def run_convergence_tracker(self):
        '''Runs calculations and checks for convergence.

        Runs calculation for each of the k-points and checks for convergence.
        Returns list of converged k-points.
        '''

        # dummy value for initial k-points
        initial_kpoints = [1, 1, 1]
        old_kp = initial_kpoints

        scaling_factor = self.scale_kpoints()

        for iteration in range(self.max_iter):

            structure = self.read_structure()

            calc = self.create_calculator()

            if iteration == 0:
                this_kp = initial_kpoints
            else:
                this_kp = self.get_new_kpoints(old_kp, scaling_factor)

            calc.set(kpts = this_kp)

            structure.set_calculator(calc)

            energy = structure.get_potential_energy()

            calc.clean()

            if iteration > 0 and abs(energy - old_energy) < self.convergence_th :
                return this_kp
            else:
                old_kp = this_kp
                old_energy = energy

            if iteration == self.max_iter-1:
                raise RuntimeError('Reached maximum iteration without convergence.')


    def logger(self):
        '''Logs k-points and energy for each iteration.

        Stores k-points and energy for each iteration in two lists.
        '''

        pass

    def get_log(self):
        '''This method can be used to get list of k-points and energies used
        for the convergence tracker.

        '''

        pass


