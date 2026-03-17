import pandas as pd

class Survey:
    """
    The main class for the psych-prep pipeline. 
    Designed to take raw Qualtrics CSVs and transform them into 
    clean DataFrames for analysis.
    """

    def __init__(self, file_path):
        """
        Initializes the Survey object.
        Qualtrics CSVs usually have 3 header rows. This skips the 2nd 
        and 3rd rows (index 1 and 2) to keep the data clean.
        """
        self.data = pd.read_csv(file_path, skiprows=[1, 2])

    def filter_attention(self, column, correct_value):
        """
        Drops participants who failed an attention check.
        Example: study.filter_attention("Check_Q1", 1)
        """
        self.data = self.data[self.data[column] == correct_value]
        return self

    def reverse_score(self, columns, scale_min, scale_max):
        """
        Inverts scores for items that were negatively phrased.
        Formula: (Max + Min) - X
        """
        for col in columns:
            if col in self.data.columns:
                self.data[col] = (scale_max + scale_min) - self.data[col]
            else:
                print(f"Warning: Column '{col}' not found.")
        return self

    def calculate_subscale(self, name, columns, method='mean'):
        """
        Creates a new column by aggregating multiple items.
        - name: The name of the new composite score.
        - columns: List of columns to average or sum.
        - method: 'mean' or 'sum'.
        """
        if method == 'mean':
            self.data[name] = self.data[columns].mean(axis=1)
        elif method == 'sum':
            self.data[name] = self.data[columns].sum(axis=1)
        return self

    def get_df(self):
        """Returns the processed Pandas DataFrame."""
        return self.data