# Mengerian rank-four hardness

Apply the vertex expansion (H\mapsto H^f) to the balanced rank-four target
constructed from 3DM-3. By `VERTEX_EXPANSION.md`, the source instance has a
perfect 3DM matching iff (H^f) has an ordinary perfect matching. By
`MENGERIAN_EXPANSION.md`, (H^f) is Mengerian.

Every original target edge contains exactly one center, and each center has
(f(c_e)=5). Therefore every original edge is duplicated exactly five
times, giving

\[
|E(H^f)|=5|E(H)|=50|M|.
\]

The target has (3n+7|M|) vertices before expansion and

\[
|V(H^f)|=3n+11|M|
\]

after expansion. The transformation is polynomial and preserves rank at
most four.

For the bounded-occurrence source, each center clone has degree 10, each
expanded (h_i) and (r_i) has degree (5\cdot2=10), and each source
vertex has degree at most (5\cdot3=15). Hence

\[
\Delta(H^f)\le15.
\]

Ordinary perfect matching is in NP: a certificate is a subset of hyperedges,
and pairwise disjointness plus full coverage are checked in polynomial time.
Thus Perfect Matching is NP-complete on Mengerian hypergraphs of rank at most
four and maximum degree at most fifteen.
