-- 05 · The oldest postings that are still open
--
-- Tables: jobs_raw.postings, jobs_raw.posting_checks
-- Hints: keep each posting's latest check (QUALIFY ROW_NUMBER() OVER (PARTITION BY id
--        ORDER BY checked_date DESC) = 1), join on id, keep state = 'open',
--        and order by DATE_DIFF(CURRENT_DATE(), posted_date, DAY).
--
-- Your query:

