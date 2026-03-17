import pandas as pd

class Survey:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path, skiprows=[1, 2])

    def filter_attention(self, column, correct_value):
        self.data = self.data[self.data[column] == correct_value]
        return self

    def reverse_score(self, columns, scale_min, scale_max):
        for col in columns:
            if col in self.data.columns:
                self.data[col] = (scale_max + scale_min) - self.data[col]
        return self

    def calculate_subscale(self, name, columns, method='mean'):
        if method == 'mean':
            self.data[name] = self.data[columns].mean(axis=1)
        elif method == 'sum':
            self.data[name] = self.data[columns].sum(axis=1)
        return self

    def batch_subscales(self, subscale_map, method='mean'):
        """Processes a dictionary of subscales at once."""
        for name, cols in subscale_map.items():
            self.calculate_subscale(name, cols, method=method)
        return self

    def get_df(self):
        return self.data