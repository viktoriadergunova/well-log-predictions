import pandas as pd
import os
import glob

# load the log data and prepare the necessary columns
def load_logs_data(logs_file):
    if logs_file.endswith('.csv'):
        logs_df = pd.read_csv(logs_file)
    elif logs_file.endswith('.xlsx'):
        logs_df = pd.read_excel(logs_file)
    else:
        raise ValueError("Only CSV and XLSX files are supported.")
    
    logs_df.reset_index(drop=True, inplace=True)
    logs_df["TD"] = None
    logs_df["TC"] = None
    logs_df["SHC"] = None
    logs_df["Equation_TD"] = None
    logs_df["Equation_TC"] = None
    logs_df["Equation_SHC"] = None
    print(logs_df)
    return logs_df



# load the equation data for TC, TD, SHC
def load_coefficients_data(coefficients_file):
    if coefficients_file.endswith('.xlsx'):
        coefficients_df = pd.read_excel(coefficients_file)
    else:
        raise ValueError("Cant open equations files")
    
    coefficients_df.reset_index(drop=True, inplace=True)
    return coefficients_df


# select fitting equations based on number of logs available in the log data
def select_best_equation(log_row, matching_equations):
    best_equation = None
    best_valid_count = -1

    for _, eq_row in matching_equations.iterrows():
        available_logs = {
            "bRHOB": any(col.startswith("RHOB") for col in log_row.index)
            and pd.notna(log_row.filter(like="RHOB").values[0])
            and pd.notna(eq_row["bRHOB"]),
            "bPHIN": any(col.startswith("PHIN") for col in log_row.index)
            and pd.notna(log_row.filter(like="PHIN").values[0])
            and pd.notna(eq_row["bPHIN"]),
            "bU": any(col.startswith("U") for col in log_row.index)
            and pd.notna(log_row.filter(like="U").values[0])
            and pd.notna(eq_row["bU"]),
            "bDT": any(col.startswith("DT") for col in log_row.index)
            and pd.notna(log_row.filter(like="DT").values[0])
            and pd.notna(eq_row["bDT"]),
            "bVSH": (
                any(col.startswith("VSH") for col in log_row.index)
                and pd.notna(log_row.filter(like="VSH").values[0])
            )
            and pd.notna(eq_row["bVSH"]),
        }

        valid_logs_count = sum(available_logs.values())

        if valid_logs_count > best_valid_count:
            best_equation = eq_row
            best_valid_count = valid_logs_count

    return best_equation


# regression equation
def calculate_predicted_value(log_row, best_equation):
    intercept = best_equation["Bo"]

    if any(col.startswith("RHOB") for col in log_row.index) and pd.notna(best_equation.get("bRHOB")):
        intercept += best_equation["bRHOB"] * log_row.filter(like="RHOB").values[0]
    if any(col.startswith("PHIN") for col in log_row.index) and pd.notna(best_equation.get("bPHIN")):
        intercept += best_equation["bPHIN"] * log_row.filter(like="PHIN").values[0]
    if any(col.startswith("U") for col in log_row.index) and pd.notna(best_equation.get("bU")):
        intercept += best_equation["bU"] * log_row.filter(like="U").values[0]
    if any(col.startswith("DT") for col in log_row.index) and pd.notna(best_equation.get("bDT")):
        intercept += best_equation["bDT"] * log_row.filter(like="DT").values[0]
    if any(col.startswith("VSH") for col in log_row.index) and pd.notna(best_equation.get("bVSH")):
        intercept += best_equation["bVSH"] * log_row.filter(like="VSH").values[0]

    return intercept


# map the logs to coefficients, sedType and number of logs, calculate predictive values and store the eq number that was used
def map_and_calculate(logs_df, coefficients_file, property_name):
    coefficients_df = load_coefficients_data(coefficients_file)

    for index, log_row in logs_df.iterrows():
        # Ensure both "Rock group" columns are treated as strings before comparison
        rock_group_log = str(log_row["rock_type"]) if pd.notna(log_row["rock_type"]) else ""
        rock_group_coefficients = coefficients_df["rock_type"].astype(str)

        # Check if "Rock group" column values start with the same prefix, not exact match
        matching_equations = coefficients_df[
            rock_group_coefficients.str.startswith(rock_group_log, na=False)
            & (coefficients_df["No_logs"] == log_row["No_logs"])
        ]

        if matching_equations.empty:
            continue

        best_equation = select_best_equation(log_row, matching_equations)

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

    # generate output file dir
    base_name = os.path.basename(logs_file).replace(".xlsx", "_output.xlsx")
    output_file_path = os.path.join(output_dir, base_name)

    # create dir if don't exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the predictions to the output file
    logs_df.to_excel(output_file_path, index=False)
    print(f"Predictions saved to {output_file_path}")

# main function
def predict_values(logs_path, output_dir, data_folder="./data/equations_data"):

    # create dir if doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if os.path.isdir(logs_path):
        # process all files in the dir
        logs_files = glob.glob(os.path.join(logs_path, "*.xlsx"))
        if not logs_files:
            print(f"No Excel files found in directory: {logs_path}")
            return

        # process each file in the dir
        for logs_file in logs_files:
            process_single_file(logs_file, output_dir, data_folder)
    else:
        # handle single log file 
        process_single_file(logs_path, output_dir, data_folder)
