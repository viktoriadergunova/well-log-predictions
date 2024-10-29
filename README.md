# Predict Thermal Properties

This repository employs multivariate statistical regression functions to estimate thermal conductivity (TC), thermal diffusivity (TD), and specific heat capacity (SHC) for boreholes in sedimentary rocks. The predictions are based on the combination of **PHIN**, **U**, **DT**, **VSHA**, and **RHOB** well logs.

## Getting Started

Install the required dependencies by running:

```bash
pip install -r requirements.txt
```
## Format of Log Files

To process the log files correctly, ensure that the column names in your XLSX file are as follows:

    Depth
    PHIN (scale 0-1)
    DT
    VSHA
    VSH
    RHOB
    U
    Stratigraphy
    Lithology
    SedType
     -sedimentary type is classified as:
        -3: clastics
        -2: carbonates
        -1: evaporites

Ensure that the log file is in XLSX format and contains these exact column names, since the program will look for these specific labels to perform the calculations.

# Run Script 

 Run example with the log files in `/test_data`:

**All log files in one dir:**
 ```bash
 python main.py --log_folder_path "./data/test_data" --processed_output_dir "./data/processed_logs" --predictions_output_dir "./data/predictions" --nan_value -999
```

**Single log file**:
 If you wish to process a single log file, you can provide the path to that specific file: 

 ```bash
 python main.py --log_folder_path "./data/test_data/single_log_file.xlsx" --processed_output_dir "./data/processed_logs" --predictions_output_dir "./data/predictions"  --nan_value -999
 ```

**log_folder_path**: This is the path to the directory containing the logs of the boreholes. Ensure that the log files in this folder have the correct column names as mentioned in the Processing Log Files section.

**processed_output_dir**: This is the directory where the processed log files will be saved. These files will be marked with _processed and are ready for thermal properties calculation

**predictions_output_dir**: This is the output directory where the predicted values will be saved. The output files will contain the estimated Thermal Conductivity (TC), Thermal Diffusivity (TD), and Specific Heat Capacity (SHC) for each depth, based on the number of logs available.

**nan_value**: This parameter defines how missing values are handled in the data. If your log data contains missing values, they will be replaced by the speciefied value.