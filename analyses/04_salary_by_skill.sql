-- 04 · Posted salary range by skill
--
-- Table: jobs_raw.postings (salary_text looks like "50–58K €" or "52K €", often null)
-- Hints: REGEXP_EXTRACT the low and high numbers, SAFE_CAST them, use the midpoint,
--        UNNEST(skills), then APPROX_QUANTILES(midpoint, 2)[OFFSET(1)] for the median.
--        Show how many postings each median is based on, and keep skills with at least 10.
--
-- Your query:

