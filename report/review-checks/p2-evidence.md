# P2 numerical review and example provenance

Prepared 6 November 2026. This is a checked draft contribution, not a claim of final human sign-off.

Gold commit: f70bf95593a6b9f705674770b8c3e833ca76290c. Ranking commit: 1a1dc15b824590a39c80ea11a568fbe5814a926e.

Tables use P2 handoff comparison CSVs; paired arithmetic is reproduced from scores.jsonl. Precision/MRR use 200 questions; recall/nDCG use 199. Existing label disclosures remain applicable.

Example question: 114934e1a1e818630ff33ac5c4cd4be6c6f75bb2; paper 1811.08603. Selected to illustrate a reranking loss; no causal diagnosis or new labeling.

```json
[
  {
    "hits": [
      {
        "passage_id": "qasper-passage-v1-41f982298632271ce9a5c8211add4c0b47da516fb5d7b8dfc5b6e534a48eaf11",
        "rank": 1,
        "record_number": 255,
        "score": 5.124021980102393
      },
      {
        "passage_id": "qasper-passage-v1-44e44efe519598bfae80e36225d5701f339ca08cd8b218fd27f54aba0bf3eff7",
        "rank": 2,
        "record_number": 256,
        "score": 3.982316175427413
      },
      {
        "passage_id": "qasper-passage-v1-94dcdd7ef4b1de06f5f61103ee068471eae2b7e7b42c28c5b76608b323006cf6",
        "rank": 3,
        "record_number": 257,
        "score": 3.798167763963617
      },
      {
        "passage_id": "qasper-passage-v1-31dee3c8fa5b7279c3203d9fe9b347514e133bfe5b00b3cd1202d4b25ed83fca",
        "rank": 4,
        "record_number": 258,
        "score": 3.4658262860835496
      },
      {
        "passage_id": "qasper-passage-v1-290fdc6bb318fd955ef5a1f7ed35e6a2241a68c6a988771ca21f40c0968ee680",
        "rank": 5,
        "record_number": 259,
        "score": 2.7884795177795514
      }
    ],
    "method": "BM25",
    "question_id": "114934e1a1e818630ff33ac5c4cd4be6c6f75bb2"
  },
  {
    "hits": [
      {
        "passage_id": "qasper-passage-v1-44e44efe519598bfae80e36225d5701f339ca08cd8b218fd27f54aba0bf3eff7",
        "rank": 1,
        "record_number": 256,
        "score": 0.7122933864593506
      },
      {
        "passage_id": "qasper-passage-v1-f7e9ba587c9b7f7587169ae2d9a14ba9854f2505eb1d418fa59d247139437402",
        "rank": 2,
        "record_number": 260,
        "score": 0.6682924032211304
      },
      {
        "passage_id": "qasper-passage-v1-fd62322d473c885687d0ad35fe3901b590b43540cd63b56ee589ce29ea35a97c",
        "rank": 3,
        "record_number": 261,
        "score": 0.6589606404304504
      },
      {
        "passage_id": "qasper-passage-v1-10db27975d6ecad021ef981db1369d17c9c8c2bcfbd904556ed2aa93ec02abb0",
        "rank": 4,
        "record_number": 262,
        "score": 0.6585451364517212
      },
      {
        "passage_id": "qasper-passage-v1-31dee3c8fa5b7279c3203d9fe9b347514e133bfe5b00b3cd1202d4b25ed83fca",
        "rank": 5,
        "record_number": 258,
        "score": 0.6320257782936096
      }
    ],
    "method": "Dense",
    "question_id": "114934e1a1e818630ff33ac5c4cd4be6c6f75bb2"
  },
  {
    "hits": [
      {
        "passage_id": "qasper-passage-v1-44e44efe519598bfae80e36225d5701f339ca08cd8b218fd27f54aba0bf3eff7",
        "rank": 1,
        "record_number": 256,
        "score": 0.03252247488101534
      },
      {
        "passage_id": "qasper-passage-v1-31dee3c8fa5b7279c3203d9fe9b347514e133bfe5b00b3cd1202d4b25ed83fca",
        "rank": 2,
        "record_number": 258,
        "score": 0.031009615384615385
      },
      {
        "passage_id": "qasper-passage-v1-fd62322d473c885687d0ad35fe3901b590b43540cd63b56ee589ce29ea35a97c",
        "rank": 3,
        "record_number": 261,
        "score": 0.029957522915269395
      },
      {
        "passage_id": "qasper-passage-v1-8b472d54c88ba080427a327754ebaa3e1f8011ce9cd8b1ed9afd56fff739bcab",
        "rank": 4,
        "record_number": 263,
        "score": 0.029437229437229435
      },
      {
        "passage_id": "qasper-passage-v1-41f982298632271ce9a5c8211add4c0b47da516fb5d7b8dfc5b6e534a48eaf11",
        "rank": 5,
        "record_number": 255,
        "score": 0.02921395544346364
      }
    ],
    "method": "Hybrid RRF",
    "question_id": "114934e1a1e818630ff33ac5c4cd4be6c6f75bb2"
  },
  {
    "hits": [
      {
        "passage_id": "qasper-passage-v1-31dee3c8fa5b7279c3203d9fe9b347514e133bfe5b00b3cd1202d4b25ed83fca",
        "rank": 1,
        "record_number": 258,
        "score": 1.5932382345199585
      },
      {
        "passage_id": "qasper-passage-v1-3abeee7464efe417bc2400e1dd72548153e2e7aebcc8e25eae9bb668f176be53",
        "rank": 2,
        "record_number": 264,
        "score": -1.2337055206298828
      },
      {
        "passage_id": "qasper-passage-v1-86f7f0221213c1a48b1be8479d6ef6103c5b46d52df4d8a3fed28ee4eb805d6a",
        "rank": 3,
        "record_number": 265,
        "score": -2.3677799701690674
      },
      {
        "passage_id": "qasper-passage-v1-8b472d54c88ba080427a327754ebaa3e1f8011ce9cd8b1ed9afd56fff739bcab",
        "rank": 4,
        "record_number": 263,
        "score": -3.1080026626586914
      },
      {
        "passage_id": "qasper-passage-v1-94dcdd7ef4b1de06f5f61103ee068471eae2b7e7b42c28c5b76608b323006cf6",
        "rank": 5,
        "record_number": 257,
        "score": -3.8361878395080566
      }
    ],
    "method": "Hybrid RRF followed by BGE reranking",
    "question_id": "114934e1a1e818630ff33ac5c4cd4be6c6f75bb2"
  }
]
```
