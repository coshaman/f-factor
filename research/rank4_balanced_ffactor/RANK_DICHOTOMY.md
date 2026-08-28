# Rank dichotomy

The prior rank-at-least-five hardness result and the rank-at-most-three
polynomial result from Beckenbach–Scheidweiler combine with the construction
in `REDUCTION.md` to give the following non-uniform balanced-hypergraph
classification, subject to the stated literature freeze:

* rank at most 3: polynomial time for f-factor and perfect f-matching;
* rank at least 4: NP-complete for both problems.

The new rank-four hardness uses edge sizes 2, 3, and 4 and satisfies
(\max_v f(v)\le5). It does not establish hardness for uniform rank-four
hypergraphs.
