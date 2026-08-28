# Venue analysis and internal referee calibration

Date: 2026-08-28

These are internal, simulated editorial/referee assessments, not journal
decisions. Current scope and submission-policy checks used the official
publisher or society pages available at the time of this pass:

* [JCTB](https://www.sciencedirect.com/journal/journal-of-combinatorial-theory-series-b)
* [EJC](https://www.sciencedirect.com/journal/european-journal-of-combinatorics)
* [SIDMA editorial policy](https://epubs.siam.org/sidma/editorial-policy)
* [SIDMA instructions for authors](https://epubs.siam.org/journal/sidma/instructions-for-authors)
* [Discrete Optimization](https://www.sciencedirect.com/journal/discrete-optimization)
* [Discrete Mathematics](https://www.sciencedirect.com/journal/discrete-mathematics)

The ScienceDirect pages were intermittently access-restricted during the
check, so no unsupported claim about current impact factor, quartile,
indexing, APC, or acceptance rate is used below.

## Fit ladder

### Journal of Combinatorial Theory, Series B

The topic is within the journal's combinatorics remit, but the manuscript is
a short, highly specialized complexity-boundary paper whose main technical
device is a compact gadget. A skeptical higher-tier editor could regard
the increment from the known rank-five construction as too narrow for this
venue, despite the correctness and clean dichotomy. Internal verdict:
WEAK_REJECT_ON_SIGNIFICANCE, with no mathematical defect identified.

### European Journal of Combinatorics

The paper is a direct fit for structural hypergraph combinatorics and
complexity of discrete structures. The rank-four boundary is a concrete
open-case resolution, and the balanced/Mengerian/ideal consequences give
multiple natural audiences without inflating the claims. Internal verdict:
STRONG_ACCEPT_READY, conditional on supplying real author metadata and
using the journal's current submission format.

### SIAM Journal on Discrete Mathematics

SIDMA explicitly covers combinatorics, discrete optimization, theoretical
computer science, and discrete computational complexity. Its policy also
requires a clearly written significant contribution and accepts supplementary
materials. The fit is strong, but the simulated referee weighs the very
specialized gadget contribution slightly more conservatively than EJC.
Internal verdict: ACCEPT_WITH_MINOR_PRESENTATION_REQUESTS.

### Discrete Optimization

The reduction is relevant to discrete optimization through exact incidence
degree and matching feasibility, but the paper is more structural-
combinatorial than algorithmic. Internal verdict:
ACCEPT_WITH_MINOR_SCOPE_POSITIONING.

### Discrete Mathematics

The paper is a safe topical fit and the prior rank-five publication gives a
natural continuity point. Internal verdict: STRONG_ACCEPT_READY, subject to
the same metadata and formatting completion.

## Blind skeptical review records

### Reviewer A: primary EJC-calibrated report

**Verdict:** STRONG_ACCEPT

The local equations force exactly the two claimed modes, every edge contains
a degree-one support vertex, and the balancedness argument correctly
separates the only non-size-two edges from the residual bipartite incidence
graph. The reduction is polynomial and uses bounded-occurrence 3DM-3. The
expansion equivalence and two-stage expansion argument support the Mengerian
corollary. The paper should be publishable after ordinary copyediting and
completion of author metadata. No correctness or novelty objection was
found.

### Reviewer B: independent skeptical report

**Verdict:** ACCEPT

The reviewer rechecked the center equation, the 0/1 consequence for perfect
f-matchings, rank preservation under expansion, and the degree counts 10 and
15. The main reservation is that the manuscript should not suggest uniform
hardness or stronger bounds on f; the final version now states those
limitations explicitly. The bounded-occurrence source claim is cited to
Garey--Johnson and is consistent with the stated reduction.

### Reviewer C: presentation and novelty audit

**Verdict:** ACCEPT

The citation chain identifies the prior rank-five construction and the
rank-four open boundary. No equivalent rank-four non-uniform balanced result
was found in the final search pass. The computational checks are now
supplementary rather than evidence for the proof. Remaining action is
administrative: replace the author placeholder before submission.

## Gate decision

The selected venue is EJC. JCTB was tested and rejected internally on
significance calibration, not correctness. SIDMA, Discrete Optimization,
and Discrete Mathematics were tested as lower or parallel fits; each clears
an ordinary accept-level fit, with EJC the best balance of novelty and scope.

The readiness label is an internal submission-preparation status. It is not
a prediction of editorial acceptance.
