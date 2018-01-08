from ase.io import read

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

    def read_structure(self):
        ''' Reads structure from the path given

        ase.io.read function will be used to read the structure.
        WIll support all structure formats supported by ASE.
        '''

        return read(self.structure_path)

    def scale_kpoints(self):
        ''' Will return a list with scaling of correspondin k-point.

        If the lattice constant of the structure in any direction is twice or
        larger compared to any other direction, then k-points needed for that
        direction is half. This function will check for such properties and
        sets a list for scaling.
        '''

        pass

    def create_calculator(self):
        '''Creates calculator object from calculator.

        Reads mode from the calculator input and creates a calculator object
        with default parameters. In case changes needed in the default
        parameters, this class can be sub-classed.
        '''

        pass

    def get_new_kpoints(self):
        '''Gets new k-points from old k-points by increasing from the earlier
        values and taking into account of the scaling.

        '''

        pass

    def run_convergence(self):
        '''Runs calculations and checks for convergence.

        Runs calculation for each of the k-points and checks for convergence.
        Returns list of converged k-points.
        '''

        pass

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


