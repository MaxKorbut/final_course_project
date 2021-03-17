class DataBase:

    def __init__(self, cursor):
        self.cursor = cursor

    def get_all_table(self):
        self.cursor.execute("SELECT * FROM pg_catalog.pg_tables")
        return self.cursor.fetchall()

    def get_all_auth_user(self):
        self.cursor.execute("SELECT * FROM auth_user")
        return self.cursor.fetchall()

    def is_user_in_auth_table(self, username: str):
        auth_user_info = self.get_all_auth_user()
        for user in auth_user_info:
            if username in user:
                return True
