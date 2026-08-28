# Extension verification record

The clean-room expansion implementation is in `src/expansion_audit.py` and
the degree harness is in `src/extension_audit.py`. It constructs every clone
and every expanded edge directly from the definition, then uses a memoized
exact-cover solver independent of the f-factor solver.

Results:

* all 256 subsets of the eight triples on a 2-by-2-by-2 universe gave the
  same answer for the original exact f-factor solver and the expanded perfect
  matching solver;
* among those, all 193 instances satisfying source occurrence at most three
  had target maximum degree at most 10 and expansion maximum degree at most
  15;
* the one-triple expansion had 120 enumerated perfect matchings, and every
  projected multiplicity vector satisfied the original equations;
* every generated expanded edge had size at most four.

These are exact falsification checks, not substitutes for the proofs.
