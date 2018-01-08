import unittest
from convergence_tracker import convergence_tracker
import ase


class test_inputs(unittest.TestCase):


    def test_default_structure(self):
        '''Checks if the default structure can be read successfully

        '''

        self.ct = convergence_tracker()
        self.assertTrue(isinstance(self.ct.read_structure(), ase.atoms.Atoms))

    def test_path_structure(self):
        '''Checks if the structure in a path can be read successfully

        '''
        self.ct = convergence_tracker('../POSCAR')
        self.assertTrue(isinstance(self.ct.read_structure(), ase.atoms.Atoms))

if __name__ == '__main__':
    unittest.main()
