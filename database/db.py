class DataBase:

    def __init__(self, connect):
        self.connect = connect

    def get_all_table(self):
        cursor = self.connect.cursor()
        cursor.execute("SELECT * FROM pg_catalog.pg_tables")
        return cursor.fetchall()

    def get_all_auth_user(self):
        cursor = self.connect.cursor()
        cursor.execute("SELECT * FROM auth_user")
        return cursor.fetchall()

    def is_user_in_auth_table(self, username: str):
        auth_user_info = self.get_all_auth_user()
        for user in auth_user_info:
            if username in user:
                return True
