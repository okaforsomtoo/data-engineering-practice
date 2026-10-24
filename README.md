# Data Engineering Practice

My beginner-friendly workspace for learning the building blocks of data engineering through Python, pandas, SQL, and dbt exercises. 

I'll keep updating as practice continues.

The examples are practice scripts rather than a single production-ready application: they help build familiarity with reading and shaping data, querying tables, and
organising SQL transformations.

## What this project covers

- **Python fundamentals:** variables and types, lists and dictionaries, loops,
  functions, conditionals, exception handling, and text-file input/output.

- **Pandas:** creating and inspecting DataFrames, selecting rows, and adding
  derived columns.

- **A small CSV batch pipeline:** `pipeline.py` reads `people.csv`, fills missing age and salary values with their column means, adds a `high_earner`flag for salaries above £50,000, 
filters those records, and writes them to `high_earners.csv`.

- **SQL practice:** `queries.sql` contains employee and department query exercises covering filtering, aggregation, joins, and window functions.

  Some examples are commented out as practice notes; the uncommented queries are the ones that run when the file is executed.

- **dbt starter projects:** `my_dbt_project/` and `my_sbt_project/` contain dbt-style starter model folders for exploring SQL transformations and tests.

  They are separate starter projects, not configured parts of the pandas pipeline.

## Repository contents

| Path | Description |
| --- | --- |
| `lesson1.py`–`lesson8.py` | Short exercises introducing Python and pandas concepts |
| `codebasics1.py` | List and expense calculations |
| `python_test.py` | Additional practice challenges |
| `pipeline.py` | CSV read, clean, transform, filter, and write examples |
| `people.csv` | Sample input data for the pandas pipeline |
| `high_earners.csv` | Example output from the pipeline |
| `queries.sql` | Employee and department SQL practice |
| `cities.txt`, `test.txt` | Text-file input/output exercises |
| `my_dbt_project/` | dbt starter project folders |

## Run the pandas example

```bash
python -m pip install pandas
python pipeline.py
```

## Run the dbt starters

The dbt folders are starter examples. To try one, install dbt and the appropriate data-platform adapter, configure its dbt profile, and run dbt commands from that project's directory. For example:

```bash
cd my_dbt_project
dbt run
dbt test
```

The commands require a working profile and adapter for the selected platform;
the starter files do not by themselves configure a complete production
environment.

## Learning scope

This repository is intended for experimentation and learning. 

The examples use small local files and simplified assumptions for practice; they do not demonstrate production-grade validation, logging, orchestration, deployment, or large-scale data processing. 

Individual exercises are works in progress.

