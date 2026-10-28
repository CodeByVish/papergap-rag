# Project collaboration

- Write shared source code in English.
- Shared documentation and reports may be English-only or have both English and Chinese versions. Keep bilingual versions consistent and include both in shared commits.
- Follow CONTRIBUTING.md for task branches, review and pull requests into main.
- When the user says “提交” or “推送”, interpret the request as committing or pushing the current version of the `p3` branch, respectively.
- Preserve shared interfaces; involve affected module owners when changing them.
- Keep passage schemas and split mappings marked `v0-proposed` until the team confirms them.
- Keep credentials, raw datasets, generated corpora, model weights and indexes out of Git.
- Share QASPER raw and processed data as versioned GitHub Release attachments associated with an exact `p3` commit; keep the data files and archives out of Git. Include the raw and processed manifests, an archive SHA-256 checksum, and release notes describing provenance, generation parameters, evaluation scope, and changes. Publish changed data under a new version and retain previous versions for reproducibility; do not silently replace published assets.
- Maintain `data/README.md` and `data/README_zh-CN.md` together with reciprocal language links. Record actual published Release download links only after publication; do not imply that a planned data package is already available. Each processed artifact must have its own level-two section with generation commands and field-name/type/meaning tables, including nested fields. Document the local reproduction route as well as the Release download/extraction workflow.
- Keep personal weekly-work notes local; shared milestones belong in docs/WEEKLY_TRACKER.md.
- Keep the published bilingual Week 1 and Week 2 reports under `weekly-work/week-1/` and `weekly-work/week-2/`, and only `week-3-report-en.md` and `week-3-report-zn.md` under `weekly-work/week-3/`, tracked as shared P3 deliverables; keep all other Week 3 files local as personal work notes.
