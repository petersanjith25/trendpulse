
CREATE DATABASE IF NOT EXISTS trendpulse_db;
USE trendpulse_db;

CREATE TABLE categories (
    category_id VARCHAR(20) PRIMARY KEY,
    category_name VARCHAR(255) NOT NULL
);

CREATE TABLE videos (
    video_id VARCHAR(100) PRIMARY KEY,
    title TEXT,
    channel_title VARCHAR(255),
    category_id VARCHAR(20),
    publish_time VARCHAR(50),
    tags TEXT,
    thumbnail_link TEXT,
    description TEXT,
    CONSTRAINT fk_videos_category
        FOREIGN KEY (category_id)
        REFERENCES categories(category_id)
);

CREATE TABLE trending_records (
    record_id BIGINT PRIMARY KEY,
    video_id VARCHAR(100) NOT NULL,
    country CHAR(2) NOT NULL,
    trending_date DATE NOT NULL,
    views BIGINT,
    likes BIGINT,
    dislikes BIGINT,
    comment_count BIGINT,
    CONSTRAINT fk_records_video
        FOREIGN KEY (video_id)
        REFERENCES videos(video_id)
);

CREATE INDEX idx_records_country_date
    ON trending_records(country, trending_date);

CREATE INDEX idx_records_views
    ON trending_records(views);


USE trendpulse_db;

SELECT 'categories' AS table_name, COUNT(*) AS row_count
FROM categories
UNION ALL
SELECT 'videos', COUNT(*) FROM videos
UNION ALL
SELECT 'trending_records', COUNT(*) FROM trending_records;

