
Convergence Tracker
===================

Convergence Tracker is a class which returns converged k-points for a structure
and a calculator (i.e. VASP or Quantum Espresso).

The class take the following inputs:

* structure_path (**default**: `POSCAR` file in the current directory): The input structure name with file path.
* calculator (**default**: `VASP`): Calculator to be used. Right now supports only `VASP`.
* convergence_th (**default**: `1E-3`eV): Convergence threshold for the tracker. If the change of energy between two consecutive calculations is less than this, the `KPOINTS` is assumed a converged one.
* cutoff (**default**: `550`eV): Cut-off energy for the wavefunctions.

Usage:
```python
from convergence_tracker import ConvergenceTracker

ct = ConvergenceTracker()

ct.run_convergence_tracker()
```

Other aspects:

* Maximum 500 iterations.

Current features:

* Can read any structure supported by ASE.
* Can scale `KPOINTS` based on the lattice constants.

Features in progress:

* Printing information in each step
* Loggin information