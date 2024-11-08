import pandas as pd
import os
import glob

# make sure that columns are numeric and int
def safe_numeric_conversion(df, int_columns=None, float_columns=None):
    if int_columns:
        for col in int_columns:
            if col in df.columns:
                df[col] = (
                    pd.to_numeric(df[col], errors="coerce")
                    .round(0)
                    .fillna(pd.NA)
                    .astype("Int64")
                )
    if float_columns:
        for col in float_columns:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce")

# preprocess equation data: dict kyed by rock_type and no_logs, enable direct lookups to speed it ip
def preprocess_coefficients(coefficients_df):
    safe_numeric_conversion(coefficients_df, int_columns=["rock_type", "No_logs"])

    coefficients_dict = {}
    for _, row in coefficients_df.iterrows():
        key = (row['rock_type'], row['No_logs'])
        if key not in coefficients_dict:
            coefficients_dict[key] = []
        coefficients_dict[key].append(row)
    
    # ensure all keys are present with correct equations
    for key, equations in coefficients_dict.items():
        print(f"Key {key} contains equations: {[eq['Eq'] for eq in equations]}")
    
    return coefficients_dict

# load the log data and prepare the necessary columns
def load_logs_data(logs_file):
    if logs_file.endswith('.csv'):
        logs_df = pd.read_csv(logs_file)
    elif logs_file.endswith('.xlsx'):
        logs_df = pd.read_excel(logs_file)
    else:
        raise ValueError("Only CSV and XLSX files are supported.")
    
    logs_df.reset_index(drop=True, inplace=True)
    
    # output columns for predictions and equations in log file
    logs_df["TD"] = None
    logs_df["TC"] = None
    logs_df["SHC"] = None
    logs_df["Equation_TD"] = None
    logs_df["Equation_TC"] = None
    logs_df["Equation_SHC"] = None

    # data type conversion for log file
    safe_numeric_conversion(
        logs_df, 
        int_columns=["rock_type", "No_logs"], 
        float_columns=["Bo", "bRHOB", "bPHIN", "bU", "bDT", "bVSH"]
    )

    return logs_df

# load the equation data for TC, TD, SHC
def load_coefficients_data(coefficients_file):
    if coefficients_file.endswith('.xlsx'):
        coefficients_df = pd.read_excel(coefficients_file, decimal=',')
    else:
        raise ValueError("Cannot open equations files")

    coefficients_df.reset_index(drop=True, inplace=True)

    # data type conversion for coefficient file
    safe_numeric_conversion(
        coefficients_df, 
        int_columns=["rock_type", "No_logs"], 
        float_columns=["Bo", "bRHOB", "bPHIN", "bU", "bDT", "bVSH"]
    )

    return coefficients_df

# select fitting equations based on specific logs available in the log data
def select_best_equation(log_row, matching_equations):
    best_equation = None
    best_valid_count = -1

    # check which logs are available in log file
    available_logs = {
        "bRHOB": any(col.startswith("RHOB") for col in log_row.index) and pd.notna(log_row.filter(like="RHOB").values[0]),
        "bPHIN": any(col.startswith("PHIN") for col in log_row.index) and pd.notna(log_row.filter(like="PHIN").values[0]),
        "bU": any(col.startswith("U_pi") for col in log_row.index) and pd.notna(log_row.filter(like="U_pi").values[0]),
        "bDT": any(col.startswith("DT") for col in log_row.index) and pd.notna(log_row.filter(like="DT").values[0]),
        "bVSH": any(col.startswith("VSH") for col in log_row.index) and pd.notna(log_row.filter(like="VSH").values[0])
    }

    # check if VSH is non negative
    vsh_value = log_row.filter(like="VSH").values[0] if available_logs["bVSH"] else None
    rock_type = log_row.get("rock_type", "Unknown")  # Assuming "rock_type" is in log_row
    if vsh_value is not None and vsh_value < 0:
        print(f"\033[91mSkipping row due to invalid VSH value: {vsh_value} (must be non-negative). "
              f"Log row details: {log_row.to_dict()}, Rock type: {rock_type}\033[0m")
        return None  # Return None immediately if VSH is invalid

    print(f"Available logs in log_row (filtered for non-empty): {available_logs}")

    for _, eq_row in matching_equations.iterrows():
        # count available log
        match = True
        valid_logs_count = 0

        for log_type, is_available in available_logs.items():
            # coefficient is non null and matching log available
            has_coefficient = pd.notna(eq_row[log_type])
            if has_coefficient:
                if is_available:
                    valid_logs_count += 1 
                else:
                    # log isnt availaible? invalid match 
                    match = False
                    break
            elif is_available:
                # invalid match, either no rock type, missing coefficient -> VSH: evaporites
                match = False
                break

        # keeps track of best equation
        if match and valid_logs_count > best_valid_count:
            best_equation = eq_row
            best_valid_count = valid_logs_count

    # log print: best equation    
    if best_equation is not None:
        print(f"\033[92mBest equation chosen: {best_equation['Eq']}\033[0m")
    else:
        print(f"\033[91mNo suitable equation found for the log row. Log row details: {log_row.to_dict()}, Rock type: {rock_type}\033[0m")

    return best_equation

# regression equation
def calculate_predicted_value(log_row, best_equation):
    intercept = best_equation["Bo"]
    # partical match for log column
    if any(col.startswith("RHOB") for col in log_row.index) and pd.notna(best_equation.get("bRHOB")):
        intercept += best_equation["bRHOB"] * log_row.filter(like="RHOB").values[0]
    if any(col.startswith("PHIN") for col in log_row.index) and pd.notna(best_equation.get("bPHIN")):
        intercept += best_equation["bPHIN"] * log_row.filter(like="PHIN").values[0]
    if any(col.startswith("U_pi") for col in log_row.index) and pd.notna(best_equation.get("bU")):
        intercept += best_equation["bU"] * log_row.filter(like="U_pi").values[0]
    if any(col.startswith("DT") for col in log_row.index) and pd.notna(best_equation.get("bDT")):
        intercept += best_equation["bDT"] * log_row.filter(like="DT").values[0]
    if any(col.startswith("VSH") for col in log_row.index) and pd.notna(best_equation.get("bVSH")):
        intercept += best_equation["bVSH"] * log_row.filter(like="VSH").values[0]
    
    # round 6 decimals
    return round(intercept, 6)


# map the logs to coefficients, sedType and number of logs, calculate predictive values and store the eq number that was used
def map_and_calculate(logs_df, coefficients_file, property_name):

    coefficients_df = load_coefficients_data(coefficients_file)
    coefficients_dict = preprocess_coefficients(coefficients_df)
    
    # partial match to find columns with "rock"
    rock_column_log = [col for col in logs_df.columns if "rock" in col.lower()]
    
    if not rock_column_log:
        print(f"\033[93mWarning: 'rock_type' is None for row {index}\033[0m")
        return

    rock_column_log = rock_column_log[0]

    # each row in log file
    for index, log_row in logs_df.iterrows():

        logs_df.at[index, f"Equation_{property_name}"] = "No equation available"
        logs_df.at[index, f"{property_name}"] = None  

        # rock type, no logs for current row
        rock_type = log_row.get(rock_column_log)
        no_logs = log_row.get("No_logs")

        key = (rock_type, no_logs)
        
        # matching eq from dict
        matching_equations = coefficients_dict.get(key, [])

        # printing output
        if not matching_equations:
            print(f"\033[91mNo matching equations found for row {index} with rock_type: {rock_type} and No_logs: {no_logs}\033[0m")
            logs_df.at[index, f"Equation_{property_name}"] = "No equation available"
            continue
        else:
            print(f"\033[92mMatching equations found for row {index} with rock_type: {rock_type} and No_logs: {no_logs}\033[0m")

           
        best_equation = select_best_equation(log_row, pd.DataFrame(matching_equations))

        if best_equation is not None:
            predicted_value = calculate_predicted_value(log_row, best_equation)
            logs_df.at[index, f"{property_name}"] = predicted_value
            logs_df.at[index, f"Equation_{property_name}"] = best_equation["Eq"]

# process single file
def process_single_file(logs_file, output_dir, data_folder):
    logs_df = load_logs_data(logs_file)

    # absolute paths to equation data
    td_file = os.path.join(data_folder, "TD.xlsx")
    tc_file = os.path.join(data_folder, "TC.xlsx")
    shc_file = os.path.join(data_folder, "SHC.xlsx")

    # calculate TD, TC, and SHC
    map_and_calculate(logs_df, td_file, "TD")
    map_and_calculate(logs_df, tc_file, "TC")
    map_and_calculate(logs_df, shc_file, "SHC")

    # generate output file path with the same extension as input file
    if logs_file.endswith('.xlsx'):
        base_name = os.path.basename(logs_file).replace(".xlsx", "_prediction_output.xlsx")
        output_file_path = os.path.join(output_dir, base_name)
        # save excel file
        logs_df.to_excel(output_file_path, index=False)
    elif logs_file.endswith('.csv'):
        base_name = os.path.basename(logs_file).replace(".csv", "_prediction_output.csv")
        output_file_path = os.path.join(output_dir, base_name)
        # save csv file
        logs_df.to_csv(output_file_path, index=False)

    print(f"Predictions saved to {output_file_path}")

# main function
def predict_values(logs_path, output_dir, data_folder="./data/equations_data"):

    # create dir if doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if os.path.isdir(logs_path):
        # process all files in the dir
        logs_files = glob.glob(os.path.join(logs_path, "*.xlsx"))+ glob.glob(os.path.join(logs_path, "*.csv"))
        if not logs_files:
            print(f"No Excel or CSV files found in directory: {logs_path}")
            return

        # process each file in the dir
        for logs_file in logs_files:
            process_single_file(logs_file, output_dir, data_folder)
    else:
        # handle single log file 
        process_single_file(logs_path, output_dir, data_folder)
