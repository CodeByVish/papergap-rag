# Reviewed submission outputs

Each owner publishes a folder (p1, p2, etc.) with final CSV/JSON metrics,
per-question scores, run/configuration manifests, a README explaining limitations,
and file checksums. Preserve immutable experiment identities when adding later runs.
Keep large corpus/model/index files, secrets, temporary logs and trial outputs outside
this directory. Use pinned Git commits or shared-storage links and checksums for inputs.

P2's completed benchmark is in `p2/`. Other folders should contain actual delivered
outputs, not placeholders presented as completed runs. Read all disclosures when
using the tables in the report.

To package the committed final outputs from the repository root:

```sh
git archive --format=zip --output=/tmp/papergap-final-results.zip HEAD results/final
```

This packages results only; the submission may additionally require code and dataset
links. Other `results/` paths remain ignored.
