import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port="30000",
    user='root',
    password='root',
    database='avions'
)
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE flights(
        year YEAR(4) NOT NULL,
        month TINYINT UNSIGNED NOT NULL,
        day TINYINT UNSIGNED NOT NULL,
        dep_time TIME,
        sched_dep_time TIME,
        dep_delay SMALLINT,
        arr_delay SMALLINT,
        arr_time TIME NOT NULL,
        sched_arr_time TIME,
        carrier CHAR(2) NOT NULL,
        flight SMALLINT UNSIGNED,
        tailnum CHAR(6),
        origin CHAR(3) NOT NULL,
        dest CHAR(3) NOT NULL,
        air_time SMALLINT UNSIGNED,
        distance SMALLINT UNSIGNED NOT NULL,
        hour TINYINT UNSIGNED NOT NULL,
        minute TINYINT UNSIGNED NOT NULL,
        time_hour DATETIME NOT NULL,
        PRIMARY KEY (year,month,day,hour,flight)
    )
""")
