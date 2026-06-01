import numpy as np
import pandas as pd
from .equation_data import EQUATIONS
from .io import ROCK_GROUP_COLUMN

def calculate_eq_spread(
    df: pd.DataFrame, 
    prop: str, 
    main_pred: pd.Series, 
    main_eq_ids: pd.Series
) -> pd.DataFrame:
    
    all_equations = [eq for eq in EQUATIONS.values() if eq.property == prop]
    pred_matrix = pd.DataFrame(index=df.index)
    
    used_logs_sets = [set() for _ in range(len(df))]

    for eq in all_equations:
        req_inputs = [eq.required_inputs] if isinstance(eq.required_inputs, str) else list(eq.required_inputs)
        missing_from_df = [c for c in req_inputs if c not in df.columns]
        if missing_from_df:
            continue

        mask = (df[req_inputs].notna().all(axis=1)) & (df[ROCK_GROUP_COLUMN] == eq.rock_group)
        
        if mask.any():
            input_kwargs = {col: df.loc[mask, col] for col in req_inputs}
            if eq.id not in pred_matrix.columns:
                pred_matrix[eq.id] = np.nan
            
            pred_matrix.loc[mask, eq.id] = eq.predict(**input_kwargs)
            
            for idx in np.where(mask)[0]:
                used_logs_sets[idx].update(req_inputs)


    ensemble_stats = pd.DataFrame(index=df.index)
    

    eq_to_logs = {id: (", ".join(eq.required_inputs) if not isinstance(eq.required_inputs, str) else eq.required_inputs) 
                  for id, eq in EQUATIONS.items()}


    ensemble_stats[f"{prop}_n_equations"] = pred_matrix.count(axis=1)
    ensemble_stats[f"{prop}_ensemble_logs"] = [", ".join(sorted(list(s))) if s else "" for s in used_logs_sets]
    
    # Min Attribution
    ensemble_stats[f"{prop}_ensemble_min"] = pred_matrix.min(axis=1)
    min_ids = pred_matrix.idxmin(axis=1)
    ensemble_stats[f"{prop}_min_eq"] = min_ids
    ensemble_stats[f"{prop}_min_logs"] = min_ids.map(eq_to_logs) 
    
    # Max Attribution
    ensemble_stats[f"{prop}_ensemble_max"] = pred_matrix.max(axis=1)
    max_ids = pred_matrix.idxmax(axis=1)
    ensemble_stats[f"{prop}_max_eq"] = max_ids
    ensemble_stats[f"{prop}_max_logs"] = max_ids.map(eq_to_logs) 
    
    ordered_cols = [
        f"{prop}_n_equations", f"{prop}_ensemble_logs",
        f"{prop}_ensemble_min", f"{prop}_min_logs", f"{prop}_min_eq",
        f"{prop}_ensemble_max", f"{prop}_max_logs", f"{prop}_max_eq"
    ]
    
    return ensemble_stats[ordered_cols]