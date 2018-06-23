SELECT
  categorylinks.cl_to,  
  page.page_title,
  page.page_id 
FROM page
  INNER JOIN categorylinks
    ON page.page_id = categorylinks.cl_from
WHERE page.page_namespace = 14

AND categorylinks.cl_to LIKE '%категори%'
AND page.page_title LIKE 'Умершие_%'

ORDER BY categorylinks.cl_to