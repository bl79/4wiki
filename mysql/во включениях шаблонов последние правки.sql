SELECT
  page.page_title,
  MAX(revision.rev_timestamp) AS timestamp,
  revision.rev_comment
FROM page
  INNER JOIN templatelinks
    ON page.page_id = templatelinks.tl_from
  INNER JOIN revision
    ON page.page_id = revision.rev_page
WHERE templatelinks.tl_namespace = 10
AND page.page_namespace = 0
AND templatelinks.tl_title = 'Sfn'
AND revision.rev_timestamp > 20160820000000
AND page.page_title = '0_(число)'
GROUP BY page.page_title
ORDER BY page.page_title