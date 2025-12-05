from data_loader import load_csv_into_db
from config import CSV_FILE_PATH, MYSQL_CONFIG, ORA_CONFIG

def main():
    load_csv_into_db(CSV_FILE_PATH, MYSQL_CONFIG)

if __name__ == "__main__":
    main()