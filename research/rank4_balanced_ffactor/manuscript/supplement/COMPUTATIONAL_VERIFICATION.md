# Computational verification supplement

The computational checks below are sanity checks for the finite construction
and its bookkeeping. They are not used as proofs of the structural,
complexity, balancedness, or Mengerian claims in the manuscript.

## Exact checks

The repository scripts exhaustively checked the following finite families:

* all 256 source instances with X, Y, and Z each of size 2;
* all 256 corresponding rank-four expanded instances;
* all 193 bounded-occurrence instances in the same universe;
* all 120 one-triple instances used for the projection check.

For every source instance, the constructed factor exists exactly when the
source 3DM instance has a perfect matching. The expanded rank-four instance
has a perfect matching exactly when the unexpanded balanced instance has an
f-factor. The bounded-occurrence audit found target maximum degree 10 and
expanded maximum degree 15. The projection audit found no projected
false-positive or false-negative.

The checks can be rerun from the repository root with the scripts in
research/rank4_balanced_ffactor/src/. Their role is deliberately limited to
detecting implementation and transcription errors in the displayed gadget.
