import sys
print(sys.executable)
print(f"system path: {sys.path} ")
import pandas as pd
from pathlib import Path
print("Pandas version:",pd.__version__)

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully.")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
    
def basic_summary(data):
    print("Rows:", data.shape[0])
    print("Columns:", data.shape[1])
    print("Column names:", data.columns.tolist())
    print("Missing values per column:", data.isnull().sum())

def check_duplicates(data):
    dup_count = data.duplicated().sum()
    print("Number of duplicate rows:", dup_count)

def check_dublicates_in_key_columns(data, key):
    dup_count = data.duplicated(subset=key).sum()
    print(f"Number of duplicate rows based on key columns {key}:", dup_count)
    
if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent
    print(f"Base directory: {BASE_DIR.parent}")
    print(f"total: {1899+389+419}")
    file_path = BASE_DIR.parent / "data" / "sample_data.csv"  # Replace with your actual file path
    data = load_data(file_path)
    basic_summary(data)
    check_duplicates(data)
    key_columns = ['id']  # Replace with your actual key columns
    check_dublicates_in_key_columns(data, key_columns)
    print(f"Data shape: {data.shape}" if data is not None else "No data to display.")