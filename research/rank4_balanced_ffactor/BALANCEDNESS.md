# Balancedness of the candidate construction

Consider any strong cycle (C) in the constructed hypergraph. We show it
cannot have odd length.

Fix a gadget (e). Every edge of size greater than two belongs to this one
gadget and is one of (B_1,B_2,A); every edge incident with a private vertex
of (e) also contains (c_e). The only size-two edges are the (U_i) and
(P_j).

## A cycle containing a center

Suppose (c_e) is a cycle vertex and a non-size-two edge (q) of gadget
(e) occurs in (C). The strong-cycle condition implies that (q) contains
at most one other cycle vertex, since it already contains (c_e). Thus its
other cycle endpoint is private.

If that endpoint is an (h_i), the only other edge incident with (h_i) is
(U_i). The two cycle edges at (h_i) are consequently (q) and (U_i),
and (U_i) also contains (c_e). The cyclic sequence therefore closes on
the two vertices (c_e,h_i), giving a 2-cycle.

If the endpoint is (r_1) (the (r_2) case is symmetric), the only other
non-size-two edge that can continue through (r_1) is (A). If (A) uses
(r_1,r_2) as its two cycle endpoints, it also contains the cycle vertex
(c_e), violating the strong-cycle condition. If it uses (c_e,r_1),
the sequence again closes as a 2-cycle. The same argument applies when
(q=A): because (c_e) is a cycle vertex, (A) can only use (c_e,r_i),
and a continuation through (B_i) either violates the condition by adding
an extra cycle vertex or closes a 2-cycle.

Therefore a strong cycle containing a center and a non-size-two edge has
length two, hence is not odd.

## A cycle avoiding all centers

Suppose (c_e) is not a cycle vertex. A size-two edge incident with (c_e)
contains at most one cycle vertex and therefore cannot be a cycle edge. Thus
no (U_i) or (P_j) can occur. Within gadget (e), the private supports of
(B_1,A,B_2) intersect only as

\[
B_1\cap A=\{r_1\},\quad A\cap B_2=\{r_2\},\quad B_1\cap B_2=\varnothing.
\]

This is a path, not a cycle. A cyclic sequence of distinct hyperedges would
need the last edge to share a cycle vertex with the first, which is
impossible here; using two edges is also impossible because each pair has
at most one common vertex, whereas a 2-cycle requires two common cycle
vertices. Different gadgets have disjoint private vertices, so they cannot
repair this failure.

## Remaining edges

If no non-size-two edge occurs, every cycle edge is a size-two edge joining a
center to either an original source vertex or an (h)-vertex. Hence these
edges form a bipartite graph with centers on one side and all other vertices
on the other. Every cycle in it is even.

All strong cycles are therefore even, so the construction is balanced.
