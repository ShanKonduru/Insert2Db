import os
import pandas as pd
from PostgreSQL_Handler import PostgreSQLHandler
import configparser

def main(db_type, db_params, file_path):
    file_name, file_extension = os.path.splitext(os.path.basename(file_path))
    
    if file_extension.lower() == '.csv':
        df = pd.read_csv(file_path, parse_dates=True)
        table_name = file_name
    elif file_extension.lower() in ['.xls', '.xlsx']:
        excel_file = pd.ExcelFile(file_path)
        for sheet_name in excel_file.sheet_names:
            df = pd.read_excel(file_path, sheet_name=sheet_name, parse_dates=True)
            table_name = f"{file_name}_{sheet_name}"
            process_data(db_type, db_params, df, table_name)
        return
    else:
        raise ValueError("Unsupported file type")

    process_data(db_type, db_params, df, table_name)

def process_data(db_type, db_params, df, table_name):
    if db_type == 'postgresql':
        handler = PostgreSQLHandler(db_params)
    # elif db_type == 'oracle':
    #    handler = OracleHandler(db_params)
    # Add other database handlers as needed
    # elif db_type == 'sqlserver':
    #     handler = SQLServerHandler(db_params)
    # elif db_type == 'db2':
    #     handler = DB2Handler(db_params)
    else:
        raise ValueError("Unsupported database type")

    handler.connect()
    handler.create_table(df, table_name)
    handler.insert_data(df, table_name)
    handler.close()

# Read database credentials from configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# Example usage for PostgreSQL
db_params_postgres = {
    'dbname': config.get('PostgreSQL_DB', 'dbname'),
    'user': config.get('PostgreSQL_DB', 'user'),
    'password': config.get('PostgreSQL_DB', 'password'),
    'host': config.get('PostgreSQL_DB', 'host'),
    'port': config.get('PostgreSQL_DB', 'port')}

main('postgresql', db_params_postgres, './input/SrcEmpDataCSV.csv')
# main('postgresql', db_params_postgres, './input/SrcLargeDataSetCSV.csv')
# main('postgresql', db_params_postgres, './input/TargetEmpDataCSV.csv')
# main('postgresql', db_params_postgres, './input/TargetLargeDataSetCSV.csv')


# Example usage for Oracle
# db_params_oracle = {
#     'user': 'your_username',
#     'password': 'your_password',
#     'host': 'your_host',
#     'port': 'your_port',
#     'service_name': 'your_service_name'
# }
# main('oracle', db_params_oracle, 'path/to/your/file.xlsx')
