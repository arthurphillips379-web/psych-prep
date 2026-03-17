import pandas as pd

class Survey:
    def __init__(self, file_path):
        # Skips the two messy metadata rows Qualtrics generates
        self.data = pd.read_csv(file_path, skiprows=[1, 2])
    
    def reverse_score(self, columns, scale_min, scale_max):
        for col in columns:
            self.data[col] = (scale_max + scale_min) - self.data[col]
        return self