import lasio
import pandas as pd

def add_predicted_values_as_new_curve(las_file_path, predicted_file_path, output_las_file_path):
    las = lasio.read(las_file_path)
    print(f"Loaded LAS file with the following curves: {[curve.mnemonic for curve in las.curves]}")

    if predicted_file_path.endswith('.csv'):
        predicted_df = pd.read_csv(predicted_file_path)
    elif predicted_file_path.endswith('.xlsx'):
        predicted_df = pd.read_excel(predicted_file_path)
    else:
        raise ValueError("Predicted values file must be either .csv or .xlsx")

    depth_column = None
    for col in predicted_df.columns:
        if col.lower() in ["depth", "depth"]:
            depth_column = col
            break
    if not depth_column:
        raise ValueError("Predicted data file must contain a 'DEPTH' column.")

    
    for column in predicted_df.columns:
        if column != depth_column:  
            curve_data = list(zip(predicted_df[depth_column], predicted_df[column]))

          
            las.append_curve(column, [value for _, value in curve_data], unit="")

    las.write(output_las_file_path)
    print(f"Modified LAS file saved as {output_las_file_path} with added predicted values as new curves.")

las_file_path = "./data/test_data/Rheinsberg_prediction_heatflow.las"  
predicted_file_path = "/predictions_output/Rheinsberg_prediction_heatflow_ohne_rho.d_processed_output.csv"  
output_las_file_path = "output_with_predictions.las" 

add_predicted_values_as_new_curve(las_file_path, predicted_file_path, output_las_file_path)
