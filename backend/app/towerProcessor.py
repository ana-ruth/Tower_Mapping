import pandas as pd

COLUMNS = {
    "tower_name": ["tower", "tower_name", "site", "name", "tower name", "towers"],
    "latitude": [ "lat", "latitude", "latitudes"],
    "longitude": ["lon", "longitude", "long", "lng", "longitudes"],
    "address": ["addr", "site address", "location", "address", "addresses"]
}

@staticmethod
def validate_columns(file_uploads):

    print("Validating columns for uploaded files...")
    df = pd.DataFrame()

    for file_upload in file_uploads:

        #Check file type
        if file_upload.filename.endswith(".csv"):
            df = pd.read_csv(file_upload.file)
        elif file_upload.filename.endswith((".xls", ".xlsx")):
            df = pd.read_excel(file_upload.file)
        else:
            print(f"Unsupported file type: {file_upload.filename}")
            continue

        #Standardize column names to those in required_cols
        df = standardize_columns(df, COLUMNS)

        required_cols = ["tower_name", "latitude", "longitude", "address"]
        for col in required_cols:
            if col not in df.columns:
                raise ValueError(f"Missing required column: {col}")

        print(df['latitude'])
    
        
    return df

def standardize_columns(df, aliases):
    new_columns = {}
    for standard_name, variants in aliases.items():
        for col in df.columns:
            col_lower = col.strip().lower()
            if col_lower in [v.lower() for v in variants]:
                new_columns[col] = standard_name
                break  # Map only once
    return df.rename(columns=new_columns)


    