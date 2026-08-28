# Vertex expansion

For (H=(V,E)) and (f:V\to\mathbb Z_{ge0}), replace each (v) by clones
(v_1,\ldots,v_{f(v)}). For every original edge (e) and every (v\in e),
replace (v) by one clone, producing one edge for each independent choice of
clones. If (f(v)=0), the vertex and every incident edge disappear.

No expanded edge has more vertices than its original edge, so

\[
\operatorname{rank}(H^f)\le\operatorname{rank}(H).
\]

For the present construction every (f(v)>0) and every original edge
survives, so equality also holds.

To prove perfect-matching equivalence, let (x(e)) be a perfect
(f)-matching of (H). At vertex (v), the total number of incident edge
copies required is 
\(\sum_{e\ni v}x(e)=f(v)\). Assign the (f(v)) clones bijectively to
these occurrences. For each occurrence of (e), choose the assigned clone
at every vertex of (e); the corresponding expanded edge exists by
construction. These edges cover every clone once and are pairwise disjoint.

Conversely, project every edge of a perfect matching of (H^f) to its
original edge. Let (x(e)) be the number of matching edges projecting to
(e). Each clone (v_i) is covered once, so counting all clones of (v)
gives \(\sum_{e\ni v}x(e)=f(v)\). Thus (x) is a perfect (f)-matching.

The two operations are inverse at the level of feasibility.
