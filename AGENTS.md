# Project Collaboration Rules

- All project code and reports must be written in English.
- Team members must communicate with one another in English.
- The user is Chinese, so conversations between the user and Codex should remain in Chinese.
- GitHub repository: <https://github.com/CodeByVish/papergap-rag>
- Project Conda environment: `papergap-rag` (Python 3.11); keep local environments outside the repository.
- `Instruction.pdf` contains the detailed requirements for the group project issued by the professor.
- `ProjectPlan.pdf` contains the project plan finalized after discussion among the group members.
- The GitHub repository also contains substantial project information and work plans.
- Files under `weekly-work/` are primarily personal work arrangements for the user, are not intended to be pushed to GitHub, and should be written in Chinese. Important terms should retain both Chinese and English versions.

## P3 Branch Collaboration

- Use `p3-qasper-foundation` for the P3 QASPER data foundation and teammate integration.
- Submit shared P3 changes through this branch and a review pull request targeting `main`.
- Keep interfaces and split mappings marked `v0-proposed` until the team confirms them; do not describe them as frozen before then.
- Keep downloaded raw data and generated derived samples out of Git. Teammates reproduce them locally using the commands in `data/README.md`.
