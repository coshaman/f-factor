# Internal Review 1

## Scope

This review was performed after freezing the manuscript draft. It checked the
mode equations, strong-cycle argument, reduction directions, multiplicity
collapse, degree arithmetic, vertex expansion, Mengerian closure, rank-bound
wording, and bibliography.

## Findings

1. The two equations at \(r_1,r_2\) correctly force \(b_1=b_2\), and the
   center equation correctly forces the port sum to be \(0\) or \(3\).
2. In the balancedness proof, a non-size-two edge cannot occur in a strong
   cycle of length greater than two. The case \(c_e\notin C\) correctly
   excludes all incident size-two edges, and the remaining private
   intersection pattern is a path.
3. Every source vertex is incident only with port edges, so the backward
   reduction gives exact, rather than merely at-most-one, coverage.
4. The \(f=1\) witness on every target edge correctly collapses integer
   perfect \(f\)-matchings to 0/1 factors.
5. The bounded-degree values are \(10,2,2,\le3\); after fivefold center
   expansion they are \(10,10,10,\le15\).
6. Two-stage expansion is correctly identified with expansion by summed
   multiplicities, which proves Mengerianity of the expanded instance.
7. The rank dichotomy is phrased as a statement about rank bounds and does
   not incorrectly claim hardness for every graph whose exact rank is at
   least four.

No concrete mathematical or bibliographic defect was found. No revision was
required.
