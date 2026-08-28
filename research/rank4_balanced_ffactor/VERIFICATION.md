# Exact verification plan

`src/build_reduction.py` is the producer. `src/exact_audit.py` independently
enumerates source subsets for 3DM, solves the target f-factor by exact
incidence backtracking, and enumerates candidate vertex/edge sequences for
strong odd cycles. The implementations do not use the gadget-mode equations.

Results: all 256 instances formed by subsets of the eight triples on a
2-by-2-by-2 3DM universe agreed between source and target; 20 additional
random instances on a 2-by-2-by-2 universe also agreed. Direct strong-cycle
enumeration found no odd cycle in all 276 tested constructions. The
odd-square incidence test found no forbidden submatrix for one- and
two-triple constructions. The mutation record is in
`INDEPENDENT_AUDIT.md`.

The audit is exact integer computation and is falsification evidence only;
the mathematical proof does not depend on it.
