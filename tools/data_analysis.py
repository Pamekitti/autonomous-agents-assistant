from typing import Dict, Any
import pandas as pd
import numpy as np
from io import StringIO
import logging

def analyze_data(data: str) -> Dict[str, Any]:
    """Analyze data using pandas and numpy"""
    try:
        df = pd.read_csv(StringIO(data)) if ',' in data else pd.DataFrame(eval(data))
        
        analysis = {
            "summary": df.describe().to_dict(),
            "column_types": df.dtypes.to_dict(),
            "missing_values": df.isnull().sum().to_dict(),
            "row_count": len(df),
            "column_count": len(df.columns)
        }
        
        numerical_cols = df.select_dtypes(include=[np.number]).columns
        if len(numerical_cols) > 0:
            analysis["correlations"] = df[numerical_cols].corr().to_dict()
            
        return {
            "success": True,
            "analysis": analysis
        }
    except Exception as e:
        logging.error(f"Data analysis error: {str(e)}")
        return {
            "success": False,
            "error": str(e),
            "data_sample": data[:100]
        } 