-- Категории LIKE 'Родившиеся_%', 
-- входящие в LIKE 'Персоналии:%', но не входящие в LIKE 'Родившиеся_%'[АТЕ]
SELECT distinct
  page.page_title
FROM page
  INNER JOIN categorylinks
    ON page.page_id = categorylinks.cl_from
WHERE page.page_namespace = 14
AND page.page_title IN (SELECT
    page.page_title
  FROM page
    INNER JOIN categorylinks
      ON page.page_id = categorylinks.cl_from
  WHERE page.page_namespace = 14
  AND page.page_title LIKE 'Родившиеся_%'
  AND categorylinks.cl_to LIKE 'Персоналии:%')

AND page.page_title NOT IN (SELECT
    page.page_title
  FROM page
    INNER JOIN categorylinks
      ON page.page_id = categorylinks.cl_from
  WHERE page.page_namespace = 14
  AND page.page_title LIKE 'Родившиеся_%'
  AND categorylinks.cl_to LIKE 'Родившиеся_%')
ORDER BY categorylinks.cl_to, page.page_title