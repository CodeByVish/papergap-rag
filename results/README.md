# Experiment results

Share experiment results under `results/` in Git, including metrics, reports and reproducibility records. Raw datasets, generated corpora, model weights and indexes stay out of Git. Each run should include its ID, code commit, config, data and split hashes, model revisions, prompts, seed, dependency snapshot, hardware, metrics, per-question predictions and latency records. P6 defines the shared record schema in Week 1. For outputs too large for Git, add external results links after checking collaborator access.

`.gitattributes` preserves the original bytes under `results/chunk_size/` so manifest SHA-256 checks remain valid after checkout on any platform. Do not normalize line endings in these artifacts.
