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
    
    # Debug output to ensure all keys are present with correct equations
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
    
    # Initialize output columns for predictions and equations
    logs_df["TD"] = None
    logs_df["TC"] = None
    logs_df["SHC"] = None
    logs_df["Equation_TD"] = None
    logs_df["Equation_TC"] = None
    logs_df["Equation_SHC"] = None

    # Use helper function for column type conversion
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

    # Use helper function to convert rock_type and No_logs to integers and coefficients to numeric
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

    # Determine which logs are available in the log row
    available_logs = {
        "bRHOB": any(col.startswith("RHOB") for col in log_row.index) and pd.notna(log_row.filter(like="RHOB").values[0]),
        "bPHIN": any(col.startswith("PHIN") for col in log_row.index) and pd.notna(log_row.filter(like="PHIN").values[0]),
        "bU": any(col.startswith("U_pi") for col in log_row.index) and pd.notna(log_row.filter(like="U_pi").values[0]),
        "bDT": any(col.startswith("DT") for col in log_row.index) and pd.notna(log_row.filter(like="DT").values[0]),
        "bVSH": any(col.startswith("VSH") for col in log_row.index) and pd.notna(log_row.filter(like="VSH").values[0])
    }

    print(f"Available logs in log_row (filtered for non-empty): {available_logs}")
    print(f"Matching equations before filtering by logs:\n{matching_equations}")

    for _, eq_row in matching_equations.iterrows():
        # Count the number of matching logs for this equation
        match = True
        valid_logs_count = 0

        for log_type, is_available in available_logs.items():
            # Check if the coefficient is non-null and the log is available
            has_coefficient = pd.notna(eq_row[log_type])
            if has_coefficient:
                if is_available:
                    valid_logs_count += 1  # This coefficient matches an available log
                else:
                    # The equation expects a log that isn't available, so it's an invalid match
                    match = False
                    break
            elif is_available:
                # Equation is missing a coefficient for an available log, so it's an invalid match
                match = False
                break

        # Debug output: show valid logs count and match status
        print(f"Equation {eq_row['Eq']} - Match status: {match}, Valid logs count: {valid_logs_count}")
        
        # Only select this equation if it has the highest match score so far
        if match and valid_logs_count > best_valid_count:
            best_equation = eq_row
            best_valid_count = valid_logs_count
            print(f"New best equation selected: {eq_row['Eq']} with match score {valid_logs_count}")

    # Final debug output to confirm the selected equation
    if best_equation is not None:
        print(f"Best equation chosen: {best_equation['Eq']}")
    else:
        print("No suitable equation found for the log row")

    return best_equation


# regression equation
def calculate_predicted_value(log_row, best_equation):
    intercept = best_equation["Bo"]
    # partical macth for log column
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
    # Load and preprocess coefficients data into a dictionary for fast lookup
    coefficients_df = load_coefficients_data(coefficients_file)
    coefficients_dict = preprocess_coefficients(coefficients_df)
    
    # Do partial match to find columns with "rock"
    rock_column_log = [col for col in logs_df.columns if "rock" in col.lower()]
    
    if not rock_column_log:
        print("No columns containing 'rock' found in logs data.")
        return

    rock_column_log = rock_column_log[0]

    # Iterate over each row in logs_df
    for index, log_row in logs_df.iterrows():
        # Retrieve the rock type and No_logs values for the current row
        rock_type = log_row.get(rock_column_log)
        no_logs = log_row.get("No_logs")

        # Construct the key for dictionary lookup
        key = (rock_type, no_logs)
        
        # Get matching equations from the dictionary
        matching_equations = coefficients_dict.get(key, [])

        # Debugging output
        if not matching_equations:
            print(f"No matching equations found for row {index} with rock_type: {rock_type} and No_logs: {no_logs}")
            continue
        else:
            print(f"Matching equations found for row {index} with rock_type: {rock_type} and No_logs: {no_logs}")

        # Find the best equation among the matching ones
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
        base_name = os.path.basename(logs_file).replace(".xlsx", "_output.xlsx")
        output_file_path = os.path.join(output_dir, base_name)
        # Save the predictions to an Excel file
        logs_df.to_excel(output_file_path, index=False)
    elif logs_file.endswith('.csv'):
        base_name = os.path.basename(logs_file).replace(".csv", "_output.csv")
        output_file_path = os.path.join(output_dir, base_name)
        # Save the predictions to a CSV file
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
