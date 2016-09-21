-- выборка категорий для страниц по id страниц или названий page_title
SELECT
  page.page_title,
  page.page_id,
  categorylinks.cl_to
FROM page
  INNER JOIN categorylinks
    ON page.page_id = categorylinks.cl_from
WHERE page.page_id = 28  -- id страницы
-- WHERE page.page_title = '' -- название страницы
AND page.page_namespace = 0  -- 0 = статьи в основном пространстве
ORDER BY page.page_title