# Bounded-degree consequence

Use the standard NP-complete problem 3DM-3: (|X|=|Y|=|Z|), and every
element occurs in at most three source triples. Garey and Johnson list this
restriction as still NP-complete (their 1979 guide, problem SP1; the same
statement is reproduced in the cited primary-source literature).

For each source triple the target contains exactly the four (U)-edges, two
(B)-edges, one (A)-edge, and three (P)-edges. Thus

\[
\deg(c_e)=4+2+1+3=10.
\]

Each (h_i) is in exactly one (U)-edge and one (B)-edge, so it has degree
two. Each (r_i) is in one (B)-edge and (A), so it has degree two. An
original source vertex is in one port edge per source occurrence, hence has
degree at most three. There are no other edges.

Therefore the constructed balanced hypergraph has
(\Delta(H)\le10), rank at most four, and (max f\le5). The frozen 3DM
reduction and the perfect-f-matching argument consequently prove
NP-completeness for both problems under all three restrictions.
