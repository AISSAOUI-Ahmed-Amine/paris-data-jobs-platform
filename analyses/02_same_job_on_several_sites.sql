-- 02 · Jobs posted on two or more job boards
--
-- Table: jobs_raw.postings
-- Hints: normalize company and title first (LOWER, TRIM, REGEXP_REPLACE to drop "H/F" and
--        punctuation), then GROUP BY them and keep groups with COUNT(DISTINCT source) >= 2.
-- Question to answer in a comment: how many postings would a naive count double-count?
--
-- Your query:

