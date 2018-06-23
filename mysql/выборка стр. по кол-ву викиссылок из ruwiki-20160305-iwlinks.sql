SELECT
  iwlinks.iwl_title,
  COUNT(*) AS count
FROM iwlinks
WHERE (iwlinks.iwl_prefix LIKE 's'
OR iwlinks.iwl_prefix LIKE 'wikisource')
AND iwlinks.iwl_title LIKE 'ТСД/%'
GROUP BY iwlinks.iwl_title
ORDER BY count DESC