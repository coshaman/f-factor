# Perfect (f)-matching extension

Every edge in the construction contains a vertex whose (f)-value is one:

* (U_i) contains (h_i);
* (B_1,B_2) contain private (h)- and (r)-vertices;
* (A) contains (r_1) and (r_2);
* (P_j) contains the source vertex (v_j).

If (x) is a perfect (f)-matching, then for any edge (q) and any
(w\in q) with (f(w)=1), the vertex equation gives (x(q)\le1). Hence
all (x(q)\in\{0,1\}), so (x) is exactly an (f)-factor. The converse
is immediate. The same reduction therefore proves NP-completeness for
perfect (f)-matchings under the same rank and (f)-value restrictions.
