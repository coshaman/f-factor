# Final venue verification

Date: 2026-08-28

## Build

Command:

    tectonic -X compile manuscript.tex --keep-logs

Result: successful. The final PDF is A4, 6 pages. The log contains zero
undefined-reference diagnostics, zero citation warnings, and zero overfull
box diagnostics. All six rendered pages were visually inspected; no clipping,
overlap, missing glyph, or broken layout was found.

The only TeX warning is an underfull bibliography box caused by line
justification; it does not affect legibility or page geometry.

## Exact checks

The current final package retains the theorem-critical finite checks:

* 256 of 256 source instances pass the core equivalence;
* 256 of 256 rank-four expanded instances pass the expansion equivalence;
* the bounded-occurrence audit previously found 193 cases with no degree
  violation, target maximum degree 10, and expanded maximum degree 15;
* the one-triple projection audit previously found 120 of 120 valid
  projections.

The detailed methodology is in supplement/COMPUTATIONAL_VERIFICATION.md.

## Final files

* Main source: manuscript.tex
* Compiled article: manuscript.pdf
* Venue analysis: VENUE_ANALYSIS.md
* Revision log: VENUE_REVISION_LOG.md
* Cover letter: submission/COVER_LETTER.md
* Computational supplement: supplement/COMPUTATIONAL_VERIFICATION.md

## SHA-256

* manuscript.tex:
  C9273AAE603BC3B26D04BD9363D9B85E3E178D528F1E7EB3F78CB750497D5976
* manuscript.pdf:
  AFD2B9D84769AA8DA734510EBF955932020E7857D4B5767C48679318940DCE8B

## Release gate

Primary status: EJC_STRONG_ACCEPT_READY.

Before real submission, replace the explicit author placeholder and check the
destination journal's live submission form and formatting requirements.
