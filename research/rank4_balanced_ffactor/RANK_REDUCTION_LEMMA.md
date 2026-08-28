# Protected rank-four selector replacement

Consider the protected interface consisting of a center (c), four helpers,
and external edges incident with (c). The rank-five selector has fallback
edges \(\{c,h_i\}\), a selector edge on all four helpers, and center demand
four. Its feasible local behavior is OFF = all four fallbacks, or ON = the
selector plus three external center incidences.

Replace the selector by

\[
B_1=\{c,h_1,h_2,r_1\},\quad
B_2=\{c,h_3,h_4,r_2\},\quad
A=\{c,r_1,r_2\},
\]

set the two (r)-demands and all helper demands to one, and raise the center
demand to five. The local equations in `GADGET_MODE_LEMMA.md` show exactly
two feasible modes:

* OFF: four fallbacks and (A), with zero external incidences;
* ON: (B_1,B_2) and exactly three external incidences, with no fallback or
  (A).

Thus the external 0-versus-3 behavior and the unique determination of all
private variables are preserved. The replacement has rank four. For the
external port structure of the 3DM reduction, `BALANCEDNESS.md` proves that
the replacement introduces no strong odd cycle. The balancedness assertion
is deliberately limited to that protected external structure.
