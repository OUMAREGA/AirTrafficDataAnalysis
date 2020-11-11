CREATE TABLE weather(
    origin CHAR(3) NOT NULL,
    year YEAR(4) NOT NULL,
    month TINYINT UNSIGNED NOT NULL,
    day TINYINT UNSIGNED NOT NULL,
    hour TINYINT UNSIGNED NOT NULL,
    temp FLOAT UNSIGNED NOT NULL,
    dewp FLOAT NOT NULL,
    humid FLOAT UNSIGNED NOT NULL,
    wind_dir TINYINT UNSIGNED NOT NULL,
    wind_speed FLOAT,
    wind_gust FLOAT UNSIGNED,
    precip FLOAT UNSIGNED NOT NULL,
    pressure FLOAT UNSIGNED DEFAULT 0,
    visib FLOAT UNSIGNED NOT NULL,
    time_hour DATETIME NOT NULL,
    PRIMARY KEY (origin,`year`,`month`,`day`,hour)
)