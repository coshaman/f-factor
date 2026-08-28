# Final verification

Date: 2026-08-28.

The final manuscript was compiled with Tectonic from manuscript.tex and
references.bib. The build completed successfully after fetching the standard
TeX bundle. The resulting PDF has six A4 pages.

Checks performed:

* Tectonic completed without TeX errors.
* The log contains zero undefined-reference occurrences, zero citation
  warnings, and zero overfull-box warnings.
* All six PDF pages were rendered with Poppler at 120 dpi and visually
  inspected; no clipping, overlap, broken glyph, or unreadable table was
  found.
* Required theorem statements, abstract, introduction, conclusion, and
  bibliography were checked for consistency.
* The manuscript contains no counting theorem, uniform rank-four claim,
  max-\(f\le4\) claim, or universal rank-reduction claim.
* The exact computational checks reported in the manuscript were rerun:
  256 core instances, 256 expansion equivalence instances, 193 bounded
  degree instances, and 120 projection instances.

SHA-256:

* manuscript.tex: 6382CA43A2FB9C93446301922ED458DFC028EFFA01EA9260DFFFA50FE85466EB
* manuscript.pdf: 215D13C33FCA530B1D86F57A4C6A9CB2B235DD7F12C6AC9A2DF631907A91DB45

The final status is MANUSCRIPT_READY_FOR_SUBMISSION.
