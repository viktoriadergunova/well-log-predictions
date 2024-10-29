import argparse
from helper.process_logs import process_excel_logs
from helper.calculate_properties import predict_values

def main():
   
    parser = argparse.ArgumentParser(description="Process log files and predict values.")
    
    parser.add_argument(
        "--log_folder_path", 
        type=str, 
        required=True, 
        help="Path to the folder containing the raw log files."
    )
    parser.add_argument(
        "--processed_output_dir", 
        type=str, 
        required=True, 
        help="Path to the folder where the processed log files will be saved."
    )
    parser.add_argument(
        "--predictions_output_dir", 
        type=str, 
        required=True, 
        help="Path to the folder where the predicted values will be saved."
    )

    parser.add_argument(
        "--nan_value", 
        type=float,
        nargs='+',
        required=True,  
        help="Value to replace with NaN in the log files (default: -999.0)."
    )

    args = parser.parse_args()

    # step 1: Process the logs and save to processed_output_dir
    print(f"Processing logs from {args.log_folder_path} and saving processed logs to {args.processed_output_dir}")
    process_excel_logs(
        folder_path=args.log_folder_path,
        output_dir=args.processed_output_dir,
        nan_value=args.nan_value
    )
    
    # step 2: Predict values using processed logs and save predictions to predictions_output_dir
    print(f"Predicting values using processed logs in {args.processed_output_dir} and saving predictions to {args.predictions_output_dir}")
    predict_values(
        logs_path=args.processed_output_dir,
        output_dir=args.predictions_output_dir
    )
    
    print(f"Processing and prediction completed. Processed logs saved to {args.processed_output_dir}, predictions saved to {args.predictions_output_dir}")

if __name__ == "__main__":
    main()
