
Convergence Tracker
===================

Convergence Tracker is a class which returns converged k-points for a structure
and a calculator (i.e. VASP or Quantum Espresso).

The class take the following inputs:

* structure_path (**default**: `POSCAR` file in the current directory): The input structure name with file path.
* calculator (**default**: `VASP`): Calculator to be used. Right now supports only `VASP`.
* convergence_th (**default**: `1E-3`eV): Convergence threshold for the tracker. If the change of energy between two consecutive calculations is equal to or less than this, the `KPOINTS` is assumed a converged one.
* cutoff (**default**: `550`eV): Cut-off energy for the wavefunctions.

## Usage:
```python
from convergence_tracker import ConvergenceTracker

ct = ConvergenceTracker()

converged_kpoints = ct.run_convergence_tracker()
```

## Current features:

* Maximum 500 iterations.
* Reads any structure supported by ASE.
* Scales `KPOINTS` based on the lattice constants.
* If `verbose` is set to `True`, prints information in each step.
* Logging information.

Multiple Structure Convergence Tracker
======================================

Multiple Structure Convergence Tracker is a class which uses Convergence Tracker class
to get a list of converged k-points.

## Usage:
```python
from convergence_tracker import MultipleStructureConvergenceTracker

structure_list = ['structure1.vasp',
                  'structure2.vasp',
                  'dir1\dir2\structure3.vasp',
                 ]

msct = MultipleStructureConvergenceTracker(structure_list=structure_list, verbose=True)

converged_kpoints_list = msct.run_multiple(convergence_th=5E-3)

```

## Example output:

'''bash

 Running structure from file structure1.vasp.

 iteration  k-points     energy (eV)      dE
         1 [1, 1, 1]    -7.04470e+00  -7.045e+00
         2 [3, 3, 3]    -1.43814e+01  -7.337e+00
         3 [5, 5, 5]    -1.47712e+01  -3.898e-01
         4 [7, 7, 7]    -1.49201e+01  -1.488e-01
         5 [9, 9, 9]    -1.49202e+01  -1.116e-04


 Converged k-points: [9, 9, 9]


 Running structure from file structure2.vasp.

 iteration  k-points     energy (eV)      dE
         1 [1, 1, 1]    -8.51177e+00  -8.512e+00
         2 [3, 3, 1]    -1.43781e+01  -5.866e+00
         3 [5, 5, 2]    -1.42541e+01   1.240e-01
         4 [7, 7, 2]    -1.42850e+01  -3.086e-02
         5 [9, 9, 3]    -1.42816e+01   3.385e-03


 Converged k-points: [9, 9, 3]


 Running structure from file dir1\dir2\structure3.vasp.

 iteration  k-points     energy (eV)      dE
         1 [1, 1, 1]    -7.64215e+01  -7.642e+01
         2 [2, 3, 2]    -9.92865e+01  -2.286e+01
         3 [3, 5, 3]    -9.95579e+01  -2.715e-01
         4 [4, 7, 4]    -9.95834e+01  -2.548e-02
         5 [5, 9, 5]    -9.95853e+01  -1.925e-03


 Converged k-points: [5, 9, 5]


'''
