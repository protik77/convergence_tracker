
Convergence Tracker
===================

Convergence Tracker is a class which returns converged k-points for a structure
and a calculator (i.e. VASP or Quantum Espresso).

The class take the following inputs:

* structure_path (**default**: `POSCAR` file in the current directory): The input structure name with file path.
* calculator (**default**: `VASP`): Calculator to be used. Right now supports only `VASP`.
* convergence_th (**default**: `1E-3`eV): Convergence threshold for the tracker. If the change of energy between two consecutive calculations is equal to or less than this, the `KPOINTS` is assumed a converged one.
* cutoff (**default**: `550`eV): Cut-off energy for the wavefunctions.

Usage:
```python
from convergence_tracker import ConvergenceTracker

ct = ConvergenceTracker()

converged_kpoints = ct.run_convergence_tracker()
```

Current features:

* Maximum 500 iterations.
* Reads any structure supported by ASE.
* Scales `KPOINTS` based on the lattice constants.
* If `verbose` is set to `True`, prints information in each step.
* Logging information.

Multiple Structure Convergence Tracker
======================================

Multiple Structure Convergence Tracker is a class which uses Convergence Tracker class
to get a list of converged k-points.

Usage:
```python
from convergence_tracker import MultipleStructureConvergenceTracker

structure_list = ['structure1.vasp',
                  'structure2.vasp',
                  'dir1\dir2\structure3.vasp',
                 ]

msct = MultipleStructureConvergenceTracker(structure_list=structure_list, verbose=True)

converged_kpoints_list = msct.run_multiple(convergence_th=5E-3)

```
