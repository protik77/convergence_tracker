import unittest
from convergence_tracker import ConvergenceTracker
import ase


class TestInputs(unittest.TestCase):

    def test_default_structure(self):
        '''Checks if the default structure can be read successfully

        Attempts to read a POSCAR from the current directory.
        Test is passed if the POSCAR file is read successfully.
        '''
        self.ct = convergence_tracker()
        self.assertTrue(isinstance(self.ct.read_structure(), ase.atoms.Atoms))

    def test_path_structure(self):
        '''Checks if the structure in a path can be read successfully

        In order to pass this test, put a structure file in the upper directory.
        '''
        self.ct = convergence_tracker('../POSCAR')
        self.assertTrue(isinstance(self.ct.read_structure(), ase.atoms.Atoms))

if __name__ == '__main__':
    unittest.main()
