# Data dictionary

## postings.ndjson

One JSON object per line, one line per posting.

| Field | Type | Meaning |
|---|---|---|
| `id` | STRING | Unique id: a prefix for the job board, then the board's own id |
| `source` | STRING | Job board the posting was collected from |
| `company` | STRING | Employer name as the board shows it (not normalized) |
| `title` | STRING | Job title as posted |
| `location` | STRING | Location as posted |
| `area` | STRING | `paris` (Paris proper), `near` (inner suburbs), `region` or `other` |
| `posted_date` | DATE | Publication date given by the board; can be null |
| `first_seen` | DATE | Day the collector first saw the posting; null for some boards |
| `url` | STRING | Link to the posting |
| `salary_text` | STRING | Salary as text, for example `50–58K €`; null when not posted |
| `employment_type` | STRING | For example `Full-time` |
| `easy_apply` | BOOLEAN | True when the board offers one-click applications |
| `description` | STRING | Full posting text |
| `skills` | ARRAY&lt;STRING&gt; | Skills the title or description names, found by keyword |

Skill ids in `skills`: `sql`, `python`, `spark`, `databricks`, `dbt`, `airflow`, `snowflake`, `bigquery`, `gcp`, `aws`, `azure`, `terraform`, `kafka` (Kafka and streaming), `docker`, `kubernetes`, `cicd`, `bi` (BI tools), `elt_tools` (ingestion tools such as Airbyte or Talend), `scala_java`, `quality` (data quality and tests), `lakehouse` (Delta, Iceberg), `hadoop`, `nosql`, `governance` (governance and semantic layer), `genai`, `sqlserver`, `postgres`.

## posting_checks.ndjson

One line each time a posting was re-opened to see whether it was still online.

| Field | Type | Meaning |
|---|---|---|
| `id` | STRING | Posting id, as in `postings.ndjson` |
| `checked_date` | DATE | Day of the check |
| `state` | STRING | `open` or `closed` |

## Known quirks

These are on purpose part of the exercise:

- The same job can appear under several ids, one per board, with slightly different company names or titles.
- `posted_date` can be older than `first_seen` by several days.
- A posting can be `open` on one check and `closed` on the next; it never comes back as the same id.
- Each daily export replaces the previous one, so loading every day's file shows rows that changed, appeared or disappeared.
