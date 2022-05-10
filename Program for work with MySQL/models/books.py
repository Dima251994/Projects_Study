TABLE_NAME = "books" # задаем название таблицы

CREATE_SQL = (
    """CREATE TABLE books (
        id INT(11) NOT NULL AUTO_INCREMENT,
        name VARCHAR(255) NOT NULL,
        description VARCHAR(255),
        writer_id INT(11) NOT NULL,
        PRIMARY KEY (id) ) 
        ENGINE = InnoDB """)