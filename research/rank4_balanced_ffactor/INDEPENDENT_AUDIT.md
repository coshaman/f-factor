# Independent audit record

The exact checker in `src/exact_audit.py` uses three independent tests:

1. source 3DM is enumerated directly;
2. the target f-factor is solved by exact incidence backtracking;
3. strong odd cycles are enumerated directly, and balancedness is also
   checked through odd square incidence submatrices with row and column sum
   two.

For every subset of the eight possible triples on
(X=Y=Z=\{1,2\}) (256 instances), the source and target answers agreed.
The direct strong-cycle search found no odd strong cycle in any of those
256 constructed instances. The incidence-matrix audit also found none for
the one-triple and two-triple test instances.

Mutation tests used during development:

* deleting (A_e) removes the OFF mode (the factor equations force the ON
  choice), so the mode audit rejects the mutation;
* changing (f(c_e)) from 5 to 4 makes both intended modes infeasible, so
  the factor audit rejects it;
* adding a private edge must be checked by both independent balancedness
  tests; the checker is configured to report any discovered odd cycle or
  odd two-regular incidence submatrix.

For the concrete mutation (\{h_{e,1},h_{e,3}\}), the direct checker finds
the odd strong cycle

\[
h_{e,1},\{h_{e,1},h_{e,3}\},h_{e,3},B_{e,2},c_e,U_{e,1},h_{e,1},
\]

and consequently rejects the mutation. This is a useful sanity check that
the balancedness audit is sensitive to an actually forbidden connection.

These computations are falsification evidence only; the proofs in the
other files do not depend on them.
