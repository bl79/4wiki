-- выборка категорий-"потершек" для "родившихся"/"умерших" по местам этих рождений/смертей. Википедия:Обсуждение категорий/Сентябрь 2016#5 сентября 2016
-- "Умершие_" сменить на "Родившиеся_"
SELECT
  page.page_title,
  categorylinks.cl_to
FROM page
  INNER JOIN categorylinks
    ON page.page_id = categorylinks.cl_from
WHERE page.page_namespace = 14
AND page.page_title REGEXP '^Умершие_(?!(в(о)?_)?[0-9IXV]+)'
-- AND categorylinks.cl_to NOT IN (SELECT
  AND page.page_title NOT IN (SELECT
    page.page_title
  FROM page
    INNER JOIN categorylinks
      ON page.page_id = categorylinks.cl_from
  WHERE page.page_namespace = 14
  AND page.page_title LIKE 'Умершие_%'
  AND (categorylinks.cl_to LIKE 'Умершие_%'
    OR categorylinks.cl_to LIKE 'Неоднозначные_категории'
    OR categorylinks.cl_to LIKE 'Википедия:Категории-дубликаты'
    OR categorylinks.cl_to LIKE 'Персоналии_по_причине_смерти'
    OR categorylinks.cl_to LIKE 'Персоналии_по_обстоятельствам_смерти'
    )  -- фильтры
  GROUP BY  page.page_title
  )