# Submission summary

## Title

Closing the Rank-Four Gap for \(f\)-Factors in Balanced Hypergraphs

## Abstract

We study exact incidence-degree problems in balanced hypergraphs. Previous
work established polynomial solvability for rank at most three and
NP-completeness for non-uniform balanced hypergraphs using a rank-five
construction, leaving rank four open. We close this gap. We give a simple
rank-four selector gadget and prove that it is balanced. A reduction from
bounded-occurrence three-dimensional matching shows that both the
\(f\)-factor problem and the perfect \(f\)-matching problem are NP-complete
even when the maximum degree is at most ten and \(\max_v f(v)\le5\). Applying
the standard vertex-expansion operation yields NP-completeness of ordinary
Perfect Matching for non-uniform Mengerian hypergraphs of rank at most four
and maximum degree at most fifteen. Since Mengerian hypergraphs are ideal,
the same instances give an ideal-hypergraph corollary. Thus the complexity
dichotomy by rank bound for non-uniform balanced \(f\)-factor and perfect
\(f\)-matching problems is polynomial for bounds at most three and
NP-complete already for bound four.

## Main results

1. Balanced rank-four \(f\)-factor and perfect \(f\)-matching are NP-complete
   with \(\Delta\le10\) and \(\max f\le5\).
2. Perfect Matching is NP-complete for Mengerian rank-four hypergraphs with
   \(\Delta\le15\).
3. The same instances establish the ideal-hypergraph corollary.
4. The non-uniform balanced rank-bound dichotomy is polynomial for \(r\le3\)
   and NP-complete already for every bound \(r\ge4\).

## Novelty summary

The rank-four selector replaces the rank-five selector in the prior
Beckenbach--Scheidweiler reduction. The final citation-chain search found no
prior equivalent rank-four result.

## Format and venues

The manuscript is 6 pages in the current article format, excluding no
separate supplement. A strong realistic venue is *Discrete Optimization* or
*Discrete Mathematics*; an algorithms-oriented fallback is *Algorithmica*.
An appropriate reach venue is *ACM Transactions on Algorithms*, subject to
editorial fit and external referee assessment.

## Caveats

The result is non-uniform. Uniform rank-four hardness, \(\max f\le4\), and
counting (#P) extensions are not claimed. Counting status:
COUNTING_EXTENSION_NOT_CERTIFIED.
