import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pandas as pd
from datetime import datetime
from utils.constants import *


def read_registers_from_excel(file_path, expected_columns):
    try:
        # Attempt to read the Excel file with the openpyxl engine
        df = pd.read_excel(file_path, engine="openpyxl")
        missing = [col for col in expected_columns if col not in df.columns]
        if missing:
            raise ValueError(f"Excel file is missing required columns: {missing}")

        # Check for duplicate index
        if df.index.duplicated().any():
            raise ValueError("Duplicate index values found in DataFrame.")

        # Check for duplicate columns
        if df.columns.duplicated().any():
            raise ValueError("Duplicate column names found in DataFrame.")

        # Check for empty, null, or None values
        if df.isnull().values.any():
            raise ValueError("Null/NaN/None values found in the DataFrame.")

        # Check for empty strings specifically (optional but useful)
        if (df.map(lambda x: isinstance(x, str) and x.strip() == "")).any().any():
            raise ValueError("Empty string values found in the DataFrame.")

        # return df
        return pd.read_excel(file_path, engine="openpyxl", index_col=0)

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Error reading Excel file: {e}")
    return None


def save_df(df: pd.DataFrame, file_type: str = "csv", folder: str = "."):
    """
    Saves the DataFrame to a CSV or Excel file in the specified folder with a timestamped filename.

    Args:
        df (pd.DataFrame): The DataFrame to save.
        file_type (str): 'csv' or 'excel' (default is 'csv').
        folder (str): Path to the folder where the file should be saved (default is current directory).

    Raises:
        ValueError: If unsupported file_type is passed.
    """
    # Ensure folder exists
    os.makedirs(folder, exist_ok=True)

    # Create timestamped filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    if file_type.lower() == "csv":
        filename = f"data_{timestamp}.csv"
        filepath = os.path.join(folder, filename)
        df.to_csv(filepath, index=True)
    elif file_type.lower() in ("excel", "xlsx"):
        filename = f"data_{timestamp}.xlsx"
        filepath = os.path.join(folder, filename)
        df.to_excel(filepath, index=True)

    elif file_type.lower() == "json":
        filename = f"data_{timestamp}.json"
        filepath = os.path.join(folder, filename)
        df.to_json(filepath, orient="records", lines=True)
    else:
        raise ValueError("Unsupported file_type. Use 'csv' or 'excel'.")

    print(f"DataFrame saved to: {filepath}")


if __name__ == "__main__":
    # Example usage
    file_path = "files\\data.xlsx"  # Update this path as needed
    register_data = read_registers_from_excel(file_path, REQUIRED_COLUMNS)

    print(register_data["refresh_rate"].iloc[0])
    if register_data is not None:
        print(register_data.loc[TS1])
    else:
        print("Failed to read register data from Excel.")
