
SELECT video_id, country, views
FROM trending_records
WHERE country = 'US'
  AND views >= 1000000;



SELECT video_id, country, views
FROM trending_records
ORDER BY views DESC
LIMIT 10;



SELECT DISTINCT country
FROM trending_records
ORDER BY country;



SELECT
    country,
    ROUND(AVG(views), 2) AS average_views,
    COUNT(*) AS record_count
FROM trending_records
GROUP BY country
ORDER BY average_views DESC;



SELECT
    c.category_name,
    COUNT(*) AS record_count,
    ROUND(AVG(tr.views), 2) AS average_views
FROM trending_records AS tr
INNER JOIN videos AS v
    ON tr.video_id = v.video_id
INNER JOIN categories AS c
    ON v.category_id = c.category_id
GROUP BY c.category_id, c.category_name
HAVING COUNT(*) >= 100
ORDER BY record_count DESC;



SELECT
    tr.record_id,
    tr.country,
    tr.trending_date,
    tr.views,
    v.title,
    v.channel_title
FROM trending_records AS tr
INNER JOIN videos AS v
    ON tr.video_id = v.video_id
ORDER BY tr.views DESC
LIMIT 20;



SELECT
    v.video_id,
    v.title,
    v.channel_title
FROM videos AS v
LEFT JOIN trending_records AS tr
    ON v.video_id = tr.video_id
WHERE tr.record_id IS NULL;



SELECT
    c.category_id,
    c.category_name,
    COUNT(v.video_id) AS video_count
FROM videos AS v
RIGHT JOIN categories AS c
    ON v.category_id = c.category_id
GROUP BY c.category_id, c.category_name
ORDER BY video_count ASC, c.category_name;



SELECT
    v.video_id,
    v.title,
    v.category_id,
    c.category_name
FROM videos AS v
LEFT JOIN categories AS c
    ON v.category_id = c.category_id
ORDER BY v.video_id
LIMIT 20;



SELECT
    country,
    COUNT(*) AS high_comment_records,
    ROUND(AVG(views), 2) AS average_views
FROM trending_records
WHERE comment_count >= 1000
GROUP BY country
HAVING COUNT(*) >= 10
ORDER BY high_comment_records DESC;
