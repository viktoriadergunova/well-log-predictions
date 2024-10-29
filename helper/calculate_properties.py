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
    return logs_df



# load the equation data for TC, TD, SHC
# muss garnicht csv
def load_coefficients_data(coefficients_file):
    if coefficients_file.endswith('.csv'):
        coefficients_df = pd.read_csv(coefficients_file)
    elif coefficients_file.endswith('.xlsx'):
        coefficients_df = pd.read_excel(coefficients_file)
    else:
        raise ValueError("Unsupported file format: Only CSV and XLSX files are supported.")
    
    coefficients_df.reset_index(drop=True, inplace=True)
    return coefficients_df



# select fitting equations based on number of logs available in the log data
#partial match 
def select_best_equation(log_row, matching_equations):
    
    best_equation = None
    best_valid_count = -1
    #geht noch
    print('HERE')
    for _, eq_row in matching_equations.iterrows():
        available_logs = {
            "bRHOB": "RHOB" in log_row
            and pd.notna(log_row["RHOB"])
            and pd.notna(eq_row["bRHOB"]),
            "bPHIN": "PHIN" in log_row
            and pd.notna(log_row["PHIN"])
            and pd.notna(eq_row["bPHIN"]),
            "bU": "U" in log_row and pd.notna(log_row["U"]) and pd.notna(eq_row["bU"]),
            "bDT": "DT" in log_row
            and pd.notna(log_row["DT"])
    	    and pd.notna(eq_row["bDT"]),
            "bVSH": (
                "VSHA" in log_row
                and pd.notna(log_row["VSHA"])
                or "VSH" in log_row
                and pd.notna(log_row["VSH"])
            )
             and pd.notna(eq_row["bVSH"]),

        }

        valid_logs_count = sum(available_logs.values())

        if valid_logs_count > best_valid_count:
            best_equation = eq_row
            best_valid_count = valid_logs_count
            print( best_equation)

    return best_equation

# regression equation
def calculate_predicted_value(log_row, best_equation):
    intercept = best_equation["Bo"]

    if pd.notna(log_row.get("RHOB")) and pd.notna(best_equation.get("bRHOB")):
        intercept += best_equation["bRHOB"] * log_row["RHOB"]
    if pd.notna(log_row.get("PHIN")) and pd.notna(best_equation.get("bPHIN")):
        intercept += best_equation["bPHIN"] * log_row["PHIN"]
    if pd.notna(log_row.get("U")) and pd.notna(best_equation.get("bU")):
        intercept += best_equation["bU"] * log_row["U"]
    if pd.notna(log_row.get("DT")) and pd.notna(best_equation.get("bDT")):
        intercept += best_equation["bDT"] * log_row["DT"]
    if pd.notna(log_row.get("VSH")) and pd.notna(best_equation.get("bVSH")):
        intercept += best_equation["bVSH"] * log_row["VSH"]
    if pd.notna(log_row.get("VSHA")) and pd.notna(best_equation.get("bVSH")):
        intercept += best_equation["bVSH"] * log_row["VSHA"]

    return intercept

# map the logs to coefficients, rock type and number of logs, calculate predictive values and store the eq number that was used
def map_and_calculate(logs_df, coefficients_file, property_name):
    # load coefficient data
    coefficients_df = load_coefficients_data(coefficients_file)

    for index, log_row in logs_df.iterrows():
      
        matching_equations = coefficients_df[
            (coefficients_df["rock_type"] == log_row["rock_type"])  
            & (coefficients_df["No_logs"] == log_row["No_logs"])  
        ]

        best_equation = select_best_equation(log_row, matching_equations)

        if best_equation is not None:
            predicted_value = calculate_predicted_value(log_row, best_equation)
            logs_df.at[index, f"{property_name}"] = predicted_value
            logs_df.at[index, f"Equation_{property_name}"] = best_equation["Eq"]

# porcess single file
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
    base_name = os.path.basename(logs_file).rsplit('.', 1)[0] + "_output.xlsx"
    output_file_path = os.path.join(output_dir, base_name)

    # create dir if doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the predictions to the output file
    logs_df.to_excel(output_file_path, index=False)
    print(f"Predictions saved to {output_file_path}")

# main function
def predict_values(logs_path, output_dir, data_folder="./data/equations_data"):

    #create dir if doesnt exits
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
