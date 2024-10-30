import glob
import os
import numpy as np
import pandas as pd

def process_excel_logs(folder_path, output_dir, nan_value):
    # create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir)
            print(f"Created directory for processed logs: {output_dir}")
        except PermissionError as e:
            print(f"PermissionError: {e}")
            return
        except Exception as e:
            print(f"Error creating directory for processed logs {output_dir}: {e}")
            return

    # search for all .xlsx and .csv files in the given folder
    xlsx_files = glob.glob(os.path.join(folder_path, "*.xlsx"))
    csv_files = glob.glob(os.path.join(folder_path, "*.csv"))
    all_files = xlsx_files + csv_files

    if not all_files:
        print(f"No .xlsx or .csv files found in {folder_path}")
        return

    # process each file
    for file_path in all_files:
        print(f"Processing file: {file_path}")
        try:
            # check file type and read accordingly
            if file_path.endswith('.xlsx'):
                # skip second row, which are the units
                df = pd.read_excel(file_path, skiprows=[1])
                file_extension = '.xlsx'
            elif file_path.endswith('.csv'):
                # handle CSV files, skip second row
                df = pd.read_csv(file_path, skiprows=[1])
                file_extension = '.csv'

            # clean column names
            df.columns = df.columns.str.strip()

            # replace specified nan values
            df.replace(nan_value, np.nan, inplace=True)

            # convert columns to numeric types where applicable
            for col in df.columns:
                if df[col].dtype != 'object':  
                    df[col] = pd.to_numeric(df[col], errors="coerce")
                else:
                    df[col] = df[col].astype(str)

            # drop columns that are entirely NaN
            df = df.dropna(axis=1, how="all")

            # calculate number of logs for each depth
            log_columns = ["PHIN", "RHOB", "VSH", "DT", "U_pi"]
            available_log_columns = [
                col for col in df.columns if any(col.startswith(log_col) for log_col in log_columns)
            ]

            if available_log_columns:
                df["No_logs"] = df[available_log_columns].notna().sum(axis=1)
            
            # remove rows with 0 logs to save memory
            df = df[df["No_logs"] > 0]

            # reset index
            df.reset_index(drop=True, inplace=True)

            # determine output file path with the original extension
            base_name = os.path.basename(file_path).replace(".xlsx", "_processed" + file_extension).replace(".csv", "_processed" + file_extension)
            output_file_path = os.path.join(output_dir, base_name)

            # save in the appropriate format
            if file_extension == '.xlsx':
                with pd.ExcelWriter(output_file_path, engine="openpyxl") as writer:
                    df.to_excel(writer, index=False)
            elif file_extension == '.csv':
                df.to_csv(output_file_path, index=False)

            print(f"Successfully processed and saved log to {output_file_path}")

        except Exception as e:
            print(f"Error processing {file_path}: {e}")
