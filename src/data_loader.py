import pandas as pd
import sqlalchemy

def load_csv_into_db(csv_path, db_config):
    # Read CSV
    df = pd.read_csv(csv_path)
    
    # Create database connection
    engine = sqlalchemy.create_engine(db_config['connection_string'])
    
    # Load data into table (replace 'your_table_name' with actual table name)
    df.to_sql('your_table_name', con=engine, if_exists='replace', index=False)
    
    print("Data loaded successfully.")