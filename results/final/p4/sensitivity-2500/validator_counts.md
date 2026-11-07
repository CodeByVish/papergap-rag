# Validator warnings and errors, primary (1,200) against post-hoc (2,500), 200 held-out questions

Recounted by P4 from the records' `validation.violations`; P5's counts are identical.

| code | static 1,200 | static 2,500 | adaptive 1,200 | adaptive 2,500 |
| --- | ---: | ---: | ---: | ---: |
| CITATION_PROVENANCE_MISMATCH (warning) | 23 | 15 | 24 | 19 |
| PROVENANCE_OVERSTATED (warning) | 69 | 64 | 69 | 66 |
| UNCOVERED_REQUIRED_COMPONENT (warning) | 45 | 42 | 44 | 40 |
| UNSUPPORTED_CLAIM (warning) | 4 | 5 | 5 | 5 |
| UNSUPPORTED_NUMERIC_CLAIM (error) | 0 | 1 | 0 | 1 |
| PARSE_ERROR (error) | 2 | 2 | 2 | 3 |

Mean citations per answered question (P5): static 1.75 to 1.88, adaptive 1.81 to 1.89.
