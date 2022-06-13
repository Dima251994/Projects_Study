from connection_db import Connection


cursor = Connection().cursor
connection_db = Connection().db_connection
class Commands:
    def add_friend(self):
        """ Add new friend to database """
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        salary = float(input("Enter salary: "))
        
        cursor.execute(f"""INSERT INTO friends(first_name, last_name, salary)
                                      VALUES ('{first_name}', '{last_name}', '{salary}') """)

        connection_db.commit()
        
    def show_info_from_table(self):
        """ Show info about friends in table """
        cursor.execute("SELECT * FROM friends")
        table = cursor.fetchall()
        for row in table:
            for info in row:
                print(info, end=" ")

