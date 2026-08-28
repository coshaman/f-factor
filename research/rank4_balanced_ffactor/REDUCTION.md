# Reduction from 3-dimensional matching

Given a 3DM instance ((X,Y,Z,M)), make one gadget for every triple
(e=(x,y,z)\in M), sharing the source vertices (x,y,z) between gadgets.
Use the gadget and (f) specified in `GADGET.md`.

If (M'\subseteq M) is a perfect 3-dimensional matching, put each gadget
whose triple lies in (M') in MODE ON and every other gadget in MODE OFF.
The mode lemma verifies all private and center degrees. Every source vertex
belongs to exactly one selected triple, so its degree is one.

Conversely, any (f)-factor gives each gadget one of the two modes. Let
(M') be the triples in MODE ON. An original source vertex is incident only
with its source-port edges, and its required degree is one. The mode lemma
says all three ports of an ON gadget are selected and no port of an OFF
gadget is selected. Thus exactly one triple in (M') contains each source
vertex, so (M') is a perfect 3-dimensional matching.

The construction uses 7 private vertices and 10 edges per source triple,
plus the original source vertices. It is polynomial, has maximum (f)-value
five, and has rank at most four. Since 3DM is NP-complete, this establishes
NP-hardness once balancedness is combined with the preceding lemma.

The problem is in NP: a proposed subset of edges is checked by summing its
incidences at every vertex. Therefore the constructed restriction is
NP-complete.
