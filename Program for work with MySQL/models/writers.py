TABLE_NAME = "writers" # задаем название таблицы

CREATE_SQL = (
    """CREATE TABLE writers (
        id INT(11) NOT NULL AUTO_INCREMENT,
        name VARCHAR(255) NOT NULL,
        PRIMARY KEY (id)) ENGINE = InnoDB
    """)