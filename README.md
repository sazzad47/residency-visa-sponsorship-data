# US residency and fellowship visa sponsorship data

What the websites of every open US residency and fellowship program say about **J-1** and **H-1B** visas and about
**international medical graduates (IMGs)**, counted nationally, by specialty and by state. Compiled by
[ResidencySpot](https://residencyspot.com) and updated every day from the live tables at
**[residencyspot.com/research/visa-sponsorship](https://residencyspot.com/research/visa-sponsorship)**, where the same
numbers are shown with charts, findings and an FAQ.

<!-- summary:start -->
**As of October 18, 2026:**

| | Programs |
| --- | ---: |
| Websites read | 14,647 |
| State a visa or IMG policy | 3,533 |
| Accept J-1 physicians | 1,962 |
| Sponsor H-1B | 562 |
| Say they do not sponsor H-1B | 1,443 (72% of those that address H-1B) |
| Offer both | 480 |
| Consider IMGs without naming a visa | 752 |

190 specialty rows and 51 state rows in [`data/latest.csv`](data/latest.csv).
<!-- summary:end -->

## Files

| File | What it holds |
| --- | --- |
| [`data/latest.csv`](data/latest.csv) | The current tables: one national row, one row per specialty and track, one row per state |
| [`data/snapshots/`](data/snapshots) | A dated copy of the tables each day they changed, so the history can be studied |
| [`CITATION.cff`](CITATION.cff) | How to cite the dataset (GitHub's "Cite this repository" button reads it) |
| [`LICENSE`](LICENSE) | Creative Commons Attribution 4.0 |

## Columns

| Column | Meaning |
| --- | --- |
| `level` | `national`, `specialty` or `state` |
| `track` | `residency` or `fellowship` (specialty rows only) |
| `specialty` | Specialty name (specialty rows only) |
| `state` | Two-letter US state or territory code (state rows only) |
| `programs_read` | Open programs whose website was read |
| `state_visa_or_img_policy` | Programs whose website says anything about J-1, H-1B or international graduates |
| `j1_yes` | Programs that say they accept J-1 physicians (ECFMG sponsors the J-1 for clinical training) |
| `j1_no` | Programs that say they do not accept J-1 |
| `h1b_yes` | Programs that say they sponsor H-1B visas |
| `h1b_no` | Programs that say they do not sponsor H-1B |
| `j1_and_h1b` | Programs that say they offer both |
| `img_without_visa_named` | Programs that say they consider international graduates without naming a visa |
| `img_friendly` | Programs that sponsor a visa or consider international graduates |
| `as_of` | Date of the most recent program page read when the table was computed |

A program that says nothing is counted in `programs_read` only. Silence is unknown, not "no".

## Method

- **Sources.** Every open program in the ResidencySpot directory: residency and fellowship programs at US teaching
  institutions, from their institutions' graduate medical education directories. For each, the program's own web
  page is read and, where it links to an eligibility or how-to-apply page on the same site, that page too.
- **Reading.** Written rules, not a language model, read every sentence. A fact is recorded only from a sentence that
  states it outright, such as "we sponsor J-1 visas", "we do not sponsor H-1B visas" or "applicants must have
  graduated within the last five years". A negation counts only when it governs that statement. Questions, general
  paragraphs about ECFMG or the State Department, and sentences that disagree with each other leave the fact unknown.
- **Evidence.** Every fact keeps the sentence it came from, and each program's page on
  [residencyspot.com/programs](https://residencyspot.com/programs) quotes it, so any number can be traced to a
  program's own words.
- **Freshness.** Program pages are read again as the directory is refreshed, and linked eligibility pages every two
  weeks. The counts grow as more pages are read, which the daily snapshots record.

## Limits

- A website can be out of date, and a program can change its policy without changing its page.
- The rules favour precision: a hedged sentence ("H-1B may be considered for exceptional candidates") counts as
  unknown, so the yes and no counts are floors, not estimates for every program.
- Programs outside the ResidencySpot directory are outside the dataset.
- This is a summary of what program websites say, not legal or immigration advice. Confirm with the program, ECFMG
  and US Citizenship and Immigration Services.

## Use and citation

Free to use, share and adapt under [CC BY 4.0](LICENSE): cite ResidencySpot with a link to
[residencyspot.com/research/visa-sponsorship](https://residencyspot.com/research/visa-sponsorship).

> ResidencySpot. "US residency and fellowship visa sponsorship data." https://residencyspot.com/research/visa-sponsorship

Program-level lists, searchable by specialty, state and visa, are at
[residencyspot.com/img-friendly-programs](https://residencyspot.com/img-friendly-programs). Corrections and questions:
support@residencyspot.com.
