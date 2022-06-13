from mysql.connector import connect

# Create connection to DB and cursor for work with commands
class Connection:
    db_connection = connect(
        host = "localhost",
        user = "root",
        password = "9293709",
        database = "my_friends_info"
    )
    cursor = db_connection.cursor()