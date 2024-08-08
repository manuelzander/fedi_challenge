import sqlite3


class SQLite:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()

    def execute(self, query, params=None):
        """Executes a SQL query."""
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def commit(self):
        """Commits changes to the database."""
        self.conn.commit()

    def close(self):
        """Closes the database connection."""
        self.conn.close()
