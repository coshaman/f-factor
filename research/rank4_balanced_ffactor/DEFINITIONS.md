# Definitions

We use a finite hypergraph (H=(V,E)), with no repeated hyperedges. Its
rank is (max_{ein E}|e|). A strong cycle of length (kge 2) is an
alternating sequence of distinct vertices (v_1,ldots,v_k) and distinct
hyperedges (e_1,ldots,e_k), cyclically indexed, such that

\[
e_i\cap\{v_1,ldots,v_k\}=\{v_i,v_{i+1}\}.
\]

The hypergraph is **balanced** if it has no strong odd cycle.

For (f:V\to\mathbb Z_{ge0}), an **(f)-factor** is a subset
(F\subseteq E) satisfying

\[
|\{e\in F:v\in e\}|=f(v)\qquad(v\in V).
\]

A **perfect (f)-matching** is an integer vector (x\in\mathbb Z_{ge0}^E)
satisfying

\[
\sum_{e\ni v}x(e)=f(v)\qquad(v\in V).
\]

The rank convention is maximum cardinality of a hyperedge, so the proposed
construction has rank four because its edges have sizes 2, 3, or 4.
