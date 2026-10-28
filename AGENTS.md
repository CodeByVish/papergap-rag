# Project collaboration

- Write shared source code in English.
- Consult `Instruction.pdf` first when checking mandatory assignment requirements. Treat it as the primary source over project plans, summaries, or prior interpretations; distinguish explicit requirements from project design choices and flag unresolved ambiguity.
- Shared documentation and reports may be English-only or have both English and Chinese versions. Keep bilingual versions consistent and include both in shared commits.
- Follow CONTRIBUTING.md for task branches, review and pull requests into main.
- When the user says “提交” or “推送”, interpret the request as committing or pushing the current version of the `p3` branch, respectively.
- Preserve shared interfaces; involve affected module owners when changing them.
- Keep passage schemas and split mappings marked `v0-proposed` until the team confirms them.
- Keep credentials, model weights and indexes out of Git.
- Track data files under `data/`, including QASPER raw and processed data and their manifests, together with the README files on the GitHub `p3` branch. GitHub Releases are not required. Record provenance, generation parameters, evaluation scope, and changes in the data documentation; use Git history for reproducibility.
- Maintain `data/README.md` and `data/README_zh-CN.md` together with reciprocal language links. Each processed artifact must have its own level-two section with generation commands and field-name/type/meaning tables, including nested fields. Document the local reproduction route as well as how to obtain the data files from the GitHub `p3` branch.
- Keep personal weekly-work notes local; shared milestones belong in docs/WEEKLY_TRACKER.md.
- Keep the published bilingual Week 1 and Week 2 reports under `weekly-work/week-1/` and `weekly-work/week-2/`, and only `week-3-report-en.md` and `week-3-report-zn.md` under `weekly-work/week-3/`, tracked as shared P3 deliverables; keep all other Week 3 files local as personal work notes.
