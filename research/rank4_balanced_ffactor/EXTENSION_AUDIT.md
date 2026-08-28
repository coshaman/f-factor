# Extension audit

The bounded-degree calculation has no hidden incidence: the center sees ten
edges, helpers and (r)-vertices see two, and source vertices see at most
three. Expansion duplicates each center-containing edge five times, so the
three degree types become 10, 10, and at most 15 respectively.

The expansion equivalence was audited using a separate exact-cover solver.
It agreed on all 256 tiny instances. Projection was checked over all 120
perfect covers of the one-triple expansion. No mutation of the original
clean-room audit was used to decide either side.

The fresh terminology search included Mengerian, MFMC, ideal, clutter,
integer vertex-cover polyhedra, exact cover, rank-four, and bounded-rank
phrases. It located the 2017 Corollary 4.2 result for general Mengerian
hypergraphs and later structural work on special 4-uniform classes, but no
rank-four non-uniform hardness theorem. Counting is intentionally not
claimed: `COUNTING_EXTENSION_NOT_CERTIFIED`.
