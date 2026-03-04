import mysql.connector

class DBhelper:

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='1234',
                database='hit-db-demo'
            )
            self.mycursor = self.conn.cursor()
        except Exception as e:
            print(f"Cannot connect to database: {e}")
        else:
            print("Connected to database")

    def register(self, name, email, password):
        try:
            self.mycursor.execute(
                "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
                (name, email, password)
            )
            self.conn.commit()
            return 1
        except Exception as e:
            print(f"Register error: {e}")
            return -1

    def search(self, email, password):
        self.mycursor.execute(
            "SELECT * FROM users WHERE email = %s AND password = %s",
            (email, password)
        )
        return self.mycursor.fetchall()

    def get_user(self, user_id):
        self.mycursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        return self.mycursor.fetchone()

    def update_user(self, user_id, name, email, password):
        try:
            self.mycursor.execute(
                "UPDATE users SET name=%s, email=%s, password=%s WHERE id=%s",
                (name, email, password, user_id)
            )
            self.conn.commit()
            return 1
        except Exception as e:
            print(f"Update error: {e}")
            return -1

    def delete_user(self, user_id):
        try:
            self.mycursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
            self.conn.commit()
            return 1
        except Exception as e:
            print(f"Delete error: {e}")
            return -1
