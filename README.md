# Pulling Out All The Full Stops: Punctuation Robustness in Neural Machine Translation and Evaluation

Scripts and data for the ACL 2023 Findings paper.

## Scripts

`filter_by_finalchar.py` is used to separate the testsets into sentences with and without sentence-final punctuation.

`modify_finalchar.py` is used to insert and delete final punctuation as perturbation.

## Data
Original testsets: combined from FLORES, WMT and NTREX (see paper for exact details) and sentences with full stops, question marks, exclamation marks and no punctuation were filtered out using the script `filter_by_finalchar.py`. 
1. Final full stop: original sentence ends with a full stop (modification is to delete)
2. Final exclamation: original sentence ends with an exclamation mark (modification is to delete)
3. Final question: original sentence ends with a question mark (modification is to delete)
4. No final punct: original sentence does not end with any punctuation (modification is to insert full stop, exclamation mark, question mark and random character)

Directory structure with self-explanatory filenames:

```
data/
├── model_outputs
│   ├── deepl
│   │   ├── german
│   │   │   ├── addfinalexclamation.de-en.de.out.en
│   │   │   ├── addfinalfullstop.de-en.de.out.en
│   │   │   ├── addfinalquestion.de-en.de.out.en
│   │   │   ├── removefinalexclamation.de-en.de.out.en
│   │   │   ├── removefinalfullstop.de-en.de.out.en
│   │   │   └── removefinalquestion.de-en.de.out.en
│   │   ├── japanese
│   │   │   ├── addfinalexclamation.ja-en.ja.out.en
│   │   │   ├── addfinalfullstop.ja-en.ja.out.en
│   │   │   ├── addfinalquestion.ja-en.ja.out.en
│   │   │   ├── removefinalexclamation.ja-en.ja.out.en
│   │   │   ├── removefinalfullstop.ja-en.ja.out.en
│   │   │   └── removefinalquestion.ja-en.ja.out.en
│   │   └── ukrainian
│   │       ├── addfinalexclamation.uk-en.uk.out.en
│   │       ├── addfinalfullstop.uk-en.uk.out.en
│   │       ├── addfinalquestion.uk-en.uk.out.en
│   │       ├── removefinalexclamation.uk-en.uk.out.en
│   │       ├── removefinalfullstop.uk-en.uk.out.en
│   │       └── removefinalquestion.uk-en.uk.out.en
│   ├── google
│   │   ├── german
│   │   │   ├── addfinalexclamation.de-en.de.out.en
│   │   │   ├── addfinalfullstop.de-en.de.out.en
│   │   │   ├── addfinalquestion.de-en.de.out.en
│   │   │   ├── removefinalexclamation.de-en.de.out.en
│   │   │   ├── removefinalfullstop.de-en.de.out.en
│   │   │   └── removefinalquestion.de-en.de.out.en
│   │   ├── japanese
│   │   │   ├── addfinalexclamation.ja-en.ja.out.en
│   │   │   ├── addfinalfullstop.ja-en.ja.out.en
│   │   │   ├── addfinalquestion.ja-en.ja.out.en
│   │   │   ├── removefinalexclamation.ja-en.ja.out.en
│   │   │   ├── removefinalfullstop.ja-en.ja.out.en
│   │   │   └── removefinalquestion.ja-en.ja.out.en
│   │   └── ukrainian
│   │       ├── addfinalexclamation.uk-en.uk.out.en
│   │       ├── addfinalfullstop.uk-en.uk.out.en
│   │       ├── addfinalquestion.uk-en.uk.out.en
│   │       ├── removefinalexclamation.uk-en.uk.out.en
│   │       ├── removefinalfullstop.uk-en.uk.out.en
│   │       └── removefinalquestion.uk-en.uk.out.en
│   └── microsoft
│       ├── german
│       │   ├── addfinalexclamation.de-en.de.out.en
│       │   ├── addfinalfullstop.de-en.de.out.en
│       │   ├── addfinalquestion.de-en.de.out.en
│       │   ├── removefinalexclamation.de-en.de.out.en
│       │   ├── removefinalfullstop.de-en.de.out.en
│       │   └── removefinalquestion.de-en.de.out.en
│       ├── japanese
│       │   ├── addfinalexclamation.ja-en.ja.out.en
│       │   ├── addfinalfullstop.ja-en.ja.out.en
│       │   ├── addfinalquestion.ja-en.ja.out.en
│       │   ├── removefinalexclamation.ja-en.ja.out.en
│       │   ├── removefinalfullstop.ja-en.ja.out.en
│       │   └── removefinalquestion.ja-en.ja.out.en
│       └── ukrainian
│           ├── addfinalexclamation.uk-en.uk.out.en
│           ├── addfinalfullstop.uk-en.uk.out.en
│           ├── addfinalquestion.uk-en.uk.out.en
│           ├── removefinalexclamation.uk-en.uk.out.en
│           ├── removefinalfullstop.uk-en.uk.out.en
│           └── removefinalquestion.uk-en.uk.out.en
└── testset
	├── german
    │   ├── addfinalexclamation.de-en.de
    │   ├── addfinalexclamation.de-en.en
    │   ├── addfinalfullstop.de-en.de
    │   ├── addfinalfullstop.de-en.en
    │   ├── addfinalquestion.de-en.de
    │   ├── addfinalquestion.de-en.en
    │   ├── addfinalrandom.de-en.de
    │   ├── addfinalrandom.de-en.en
    │   ├── finalexclamation.de-en.de
    │   ├── finalexclamation.de-en.en
    │   ├── finalfullstop.de-en.de
    │   ├── finalfullstop.de-en.en
    │   ├── finalquestion.de-en.de
    │   ├── finalquestion.de-en.en
    │   ├── nofinalpunct.de-en.de
    │   ├── nofinalpunct.de-en.en
    │   ├── removefinalexclamation.de-en.de
    │   ├── removefinalexclamation.de-en.en
    │   ├── removefinalfullstop.de-en.de
    │   ├── removefinalfullstop.de-en.en
    │   ├── removefinalquestion.de-en.de
    │   ├── removefinalquestion.de-en.en
    │   ├── removefinalrandom.de-en.de
    │   └── removefinalrandom.de-en.en
    ├── japanese
    │   ├── addfinalexclamation.ja-en.en
    │   ├── addfinalexclamation.ja-en.ja
    │   ├── addfinalfullstop.ja-en.en
    │   ├── addfinalfullstop.ja-en.ja
    │   ├── addfinalquestion.ja-en.en
    │   ├── addfinalquestion.ja-en.ja
    │   ├── addfinalrandom.ja-en.en
    │   ├── addfinalrandom.ja-en.ja
    │   ├── finalexclamation.ja-en.en
    │   ├── finalexclamation.ja-en.ja
    │   ├── finalfullstop.ja-en.en
    │   ├── finalfullstop.ja-en.ja
    │   ├── finalquestion.ja-en.en
    │   ├── finalquestion.ja-en.ja
    │   ├── nofinalpunct.ja-en.en
    │   ├── nofinalpunct.ja-en.ja
    │   ├── removefinalexclamation.ja-en.en
    │   ├── removefinalexclamation.ja-en.ja
    │   ├── removefinalfullstop.ja-en.en
    │   ├── removefinalfullstop.ja-en.ja
    │   ├── removefinalquestion.ja-en.en
    │   ├── removefinalquestion.ja-en.ja
    │   ├── removefinalrandom.ja-en.en
    │   └── removefinalrandom.ja-en.ja
    └── ukrainian
		├── addfinalexclamation.uk-en.en
        ├── addfinalexclamation.uk-en.uk
        ├── addfinalfullstop.uk-en.en
        ├── addfinalfullstop.uk-en.uk
        ├── addfinalquestion.uk-en.en
        ├── addfinalquestion.uk-en.uk
        ├── addfinalrandom.uk-en.en
        ├── addfinalrandom.uk-en.uk
        ├── finalexclamation.uk-en.en
        ├── finalexclamation.uk-en.uk
        ├── finalfullstop.uk-en.en
        ├── finalfullstop.uk-en.uk
        ├── finalquestion.uk-en.en
        ├── finalquestion.uk-en.uk
        ├── nofinalpunct.uk-en.en
        ├── nofinalpunct.uk-en.uk
        ├── removefinalexclamation.uk-en.en
        ├── removefinalexclamation.uk-en.uk
        ├── removefinalfullstop.uk-en.en
        ├── removefinalfullstop.uk-en.uk
        ├── removefinalquestion.uk-en.en
        ├── removefinalquestion.uk-en.uk
        ├── removefinalrandom.uk-en.en
        └── removefinalrandom.uk-en.uk

```
	


