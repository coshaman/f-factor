# Mengerianity of the expansion

For a hypergraph (K), write (\nu(K)) for maximum matching size and
\(\tau(K)\) for minimum vertex-cover size. A hypergraph is Mengerian if
\(\nu(K^g)=\tau(K^g)\) for every nonnegative integer expansion function
\(g).

Balanced hypergraphs are Mengerian by the balanced-incidence min-max theorem
used by Beckenbach–Scheidweiler. Let (H) be the balanced target instance
and let (H^f) be its vertex expansion. For an arbitrary expansion (g) of
(H^f), label the clones of (v) by (v_1,\ldots,v_{f(v)}) and define

\[
h(v)=\sum_{i=1}^{f(v)}g(v_i).
\]

Expanding a clone (v_i) and then forgetting the intermediate label is
naturally isomorphic to expanding (v) into the (h(v)) final clones.
This isomorphism preserves edge multiplicities, vertex covers, and
matchings, so

\[
(H^f)^g\cong H^h.
\]

Since (H) is balanced and therefore Mengerian,
\(\nu(H^h)=\tau(H^h)\). Hence
\(\nu((H^f)^g)=\tau((H^f)^g)\) for every (g), proving that (H^f) is
Mengerian. This argument does not assert that (H^f) is balanced.
