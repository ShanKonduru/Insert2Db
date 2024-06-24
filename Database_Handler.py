from abc import ABC, abstractmethod

class DatabaseHandler(ABC):
    def __init__(self, db_params):
        self.db_params = db_params
        self.conn = None
        self.cursor = None

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def create_table(self, df, table_name):
        pass

    @abstractmethod
    def insert_data(self, df, table_name):
        pass

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
