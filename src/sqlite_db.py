# Impliment all logic interacting with the SQLite database.

import sqlite3

class SQLiteDB:
    def __init__(self, db_file):
        """Initialize the SQLite database connection."""
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def run_query(self, query: str):
        pass

    def connect(self):
        """Connect to the SQLite database."""
        try:
            self.connection = sqlite3.connect(self.db_file)
            self.cursor = self.connection.cursor()
            print("Connection to SQLite DB successful")
        except sqlite3.Error as e:
            print(f"The error '{e}' occurred")

    