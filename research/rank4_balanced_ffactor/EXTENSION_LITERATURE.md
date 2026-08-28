# Extension literature freeze (28 August 2026)

Beckenbach–Scheidweiler define vertex expansion and Mengerian hypergraphs in
their 2017 paper. Their Corollary 4.2 states that deciding Perfect Matching
for Mengerian hypergraphs is NP-complete. The proof expands a balanced
hypergraph instance of the f-matching problem; their displayed construction
has the old rank-five selector. Their dissertation spells out that the
rank-at-most-three balanced case is polynomial and that the rank-four case
was open for the balanced f-factor problem.

The key closure argument is explicit: an expansion of an expansion is an
expansion whose multiplicity at an original vertex is the sum of the
multiplicities of its intermediate clones. Since balanced hypergraphs are
Mengerian, the expanded instances in the present rank-four construction are
Mengerian.

Searches using Mengerian, MFMC, ideal, clutter, balanced-incidence, exact
cover, rank-four, and bounded-rank terminology found no later result that
already proves rank-four Mengerian Perfect Matching hardness. A 2024 paper
classifying certain Mengerian 4-uniform hypergraphs derived from graphs is
structural and does not establish this non-uniform complexity result. The
present consequence therefore lowers the old expansion target from rank five
to rank four, conditional on the usual literature-search limitation for
unindexed manuscripts.

Primary references:

* [Beckenbach–Scheidweiler, Discrete Mathematics 340 (2017)](https://doi.org/10.1016/j.disc.2017.05.005)
* [Beckenbach dissertation](https://refubium.fu-berlin.de/bitstream/handle/fub188/24385/dissertation_beckenbach.pdf?isAllowed=y&sequence=3)
* [Garey–Johnson 3DM entry](https://perso.limos.fr/~palafour/PAPERS/PDF/Garey-Johnson79.pdf)
