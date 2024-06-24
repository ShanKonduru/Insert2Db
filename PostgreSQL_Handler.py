import pandas as pd
import psycopg2
from Database_Handler import DatabaseHandler

class PostgreSQLHandler(DatabaseHandler):
    def __init__(self, db_params):
        super().__init__(db_params)
        # Additional initialization specific to PostgreSQLHandler
        self.HandlerName = 'PostgreSQLHandler'

    def connect(self):
        self.conn = psycopg2.connect(**self.db_params)
        self.cursor = self.conn.cursor()

    def create_table(self, df, table_name):
        columns = df.columns
        column_defs = []
        for column in columns:
            if pd.api.types.is_integer_dtype(df[column]):
                col_type = 'INTEGER'
            elif pd.api.types.is_float_dtype(df[column]):
                col_type = 'REAL'
            elif pd.api.types.is_datetime64_any_dtype(df[column]):
                col_type = 'TIMESTAMP'
            else:
                col_type = 'TEXT'
            column_defs.append(f"{column} {col_type}")
        columns_str = ', '.join(column_defs)
        create_table_query = f"""
        DROP TABLE IF EXISTS {table_name};
        CREATE TABLE {table_name} ({columns_str});
        """
        self.cursor.execute(create_table_query)
        self.conn.commit()

    def insert_data(self, df, table_name):
        for i, row in df.iterrows():
            row_values = tuple(row)
            placeholders = ', '.join(['%s'] * len(row))
            insert_query = f"INSERT INTO {table_name} VALUES ({placeholders})"
            self.cursor.execute(insert_query, row_values)
        self.conn.commit()
