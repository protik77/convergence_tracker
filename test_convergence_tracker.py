import unittest
from ConvergenceTracker import ConvergenceTracker
import ase
import os
from os import path


class TestInputs(unittest.TestCase):

    def test_default_structure(self):
        '''Checks if the default structure can be read successfully

        Attempts to read a POSCAR from the current directory.
        Test is passed if the POSCAR file is read successfully.
        '''
        ct = ConvergenceTracker()
        self.assertTrue(isinstance(ct.read_structure(), ase.atoms.Atoms))

    def test_path_structure(self):
        '''Checks if the structure in a path can be read successfully

        Uses the same POSCAR with full path name
        '''

        current_dir = os.path.dirname(os.path.realpath(__file__))

        full_path  = path.join(current_dir, 'POSCAR')

        ct = ConvergenceTracker(structure_path=full_path)
        self.assertTrue(isinstance(ct.read_structure(), ase.atoms.Atoms))

    def test_scaling_function(self):
        ''' Checks if the scaling function works'''

        ct = ConvergenceTracker()

        self.assertEqual(ct.scale_kpoints(),[1,1,4])

    def test_new_kpoints(self):
        '''Test new kpoints function.
        '''

        ct = ConvergenceTracker()

        old_kp = [1, 1, 4]
        scaling_factor = [1, 1, 4]

        self.assertEqual(ct.get_new_kpoints(old_kp, scaling_factor), [6, 6, 2])




if __name__ == '__main__':
    unittest.main()
