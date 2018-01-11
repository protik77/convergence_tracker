from ConvergenceTracker import ConvergenceTracker

class MultipleStructureConvergenceTracker():
    ''' Runs convergence tracker on multiple structures.

    Given a list of structure file names, runs convergence tracker
    on each of them.
    '''

    def __init__(self, structure_list, verbose):

        self.structure_list = structure_list
        self.verbose = verbose


    def run_multiple(self):
        ''' Runs each file and prints information if verbose is True

        :return: Returns a list of convered k-points
        '''

        converged_kps = []

        for structure in self.structure_list:

            if self.verbose:
                print(' Running structure from file {}.\n'.format(structure))

            ct = ConvergenceTracker(structure_path=structure, verbose=self.verbose)

            conv_kp = ct.run_convergence_tracker()

            if self.verbose:
                print('\n\n Converged k-points: {}'.format(conv_kp))

            converged_kps.append(converged_kps)

        return converged_kps
