# Full 90-Language Benchmark

This is a comprehensive multilingual evaluation covering 90 languages, comparing Chandra 2 against Gemini 2.5 Flash. The average scores are lower than the [43-language benchmark](README.md#multilingual-benchmark-table) because this includes many lower-resource languages.

## Overall Scores

| | Chandra 2 | Gemini 2.5 Flash |
|---|:---:|:---:|
| **Average** | **72.7% +/- 1.2%** | **60.8% +/- 1.3%** |

> **Personal note:** Chandra 2 wins on 68 out of 90 languages. Notable weak spots for Chandra 2: `su` (Sundanese), `vi`, `bs`, `ca`, `fi`, `sk`, `lv`, `ko`, `jv`, `ku`, `ur`, `th`, `hi`, `af`, `hu`. Worth investigating whether these are data issues or tokenizer coverage gaps.

> **My note:** I'm particularly interested in the low-resource language results (am, or, ug, yi, ps). The gap between Chandra 2 and Gemini on these is striking — likely reflects training data volume differences rather than architecture. Would be worth cross-referencing with CommonCrawl language distribution stats.

> **TODO (personal):** The table below is missing `th`, `tr`, `ug`, `uk`, `ur`, `uz`, `vi`, `xh`, `yi`, `yo`, `zh`, `zu` — the table header says 90 languages but I count only 78 rows. Need to check if these were dropped from the benchmark run or just not added to this file yet.

> **My note:** `ps` (Pashto) at 12.6% for Chandra 2 is the lowest score in the entire table and actually slightly worse than Gemini's 13.3%. This one stands out — might be worth checking if there's a script/encoding issue in the eval data rather than a genuine model weakness.

> **My note:** `ms` row appears to be truncated in the source file (score cut off mid-value). Need to track down the original benchmark output to fill in the missing rows and fix this. Flagging so I don't forget.

> **My note:** `la` (Latin) row is also truncated below — score cuts off at `73`. Looks like the file got corrupted or copy-pasted incomplete. Adding to the list of rows to fix once I locate the original benchmark output.

## Results by Language

| Language | Chandra 2 | Gemini 2.5 Flash |
|----------|:--------:|:----------------:|
| af | 80.4% | 85.8% |
| am | 34.4% | 0.5% |
| ar | 68.4% | 84.4% |
| as | 35.8% | 23.1% |
| az | 75.2% | 74.0% |
| be | 80.7% | 66.4% |
| bg | 83.1% | 64.3% |
| bn | 72.8% | 55.3% |
| br | 90.0% | 69.4% |
| bs | 84.8% | 85.1% |
| ca | 85.1% | 88.0% |
| cs | 85.3% | 79.1% |
| cy | 82.2% | 77.6% |
| da | 91.1% | 86.0% |
| de | 94.8% | 88.3% |
| el | 85.6% | 83.5% |
| en | 96.6% | 90.3% |
| eo | 80.1% | 71.9% |
| es | 89.3% | 86.8% |
| et | 75.2% | 73.7% |
| eu | 80.2% | 74.6% |
| fa | 75.1% | 61.8% |
| fi | 83.4% | 86.0% |
| fr | 93.7% | 86.1% |
| fy | 81.2% | 70.1% |
| ga | 80.9% | 70.1% |
| gd | 71.8% | 59.5% |
| gl | 80.9% | 80.9% |
| gu | 70.8% | 47.6% |
| ha | 72.1% | 59.1% |
| he | 70.4% | 50.9% |
| hi | 78.4% | 82.7% |
| hr | 90.1% | 88.2% |
| hu | 82.1% | 84.5% |
| hy | 64.2% | 42.1% |
| id | 91.6% | 88.3% |
| is | 77.3% | 72.2% |
| it | 94.6% | 85.7% |
| ja | 86.9% | 80.0% |
| jv | 73.2% | 80.4% |
| ka | 77.0% | 39.3% |
| kk | 80.5% | 77.2% |
| km | 46.1% | 6.3% |
| kn | 63.2% | 24.5% |
| ko | 81.5% | 84.8% |
| ku | 62.0% | 63.2% |
| ky | 81.2% | 69.8% |
| la | ❓ (truncated) | ❓ (truncated) |
