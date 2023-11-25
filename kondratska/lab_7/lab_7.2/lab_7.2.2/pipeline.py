import pandas as pd
from abc import ABC, abstractmethod
import matplotlib.pyplot as plt


class Pipeline(ABC):
    def __init__(self, data_file):
        self.data = None
        self.read_data(data_file)

    def read_data(self, data_file):
        self.data = pd.read_csv(data_file)

    def extract_features(self):
        return self.data.columns

    def visualize_features(self, column):
        if column not in self.data.columns:
            print(f"Error: '{column}' not found in the dataset.")
            return

        plt.figure(figsize=(10, 6))

        if self.data[column].dtype == 'object':
            self.data[column].value_counts().plot(kind='bar', color='skyblue')
            plt.title(f'Distribution of {column}')
            plt.xlabel(column)
            plt.ylabel('Count')
            plt.xticks(rotation=45, ha='right')
        else:
            self.data[column].plot(kind='hist', bins=20, color='skyblue')
            plt.title(f'Histogram of {column}')
            plt.xlabel(column)
            plt.ylabel('Frequency')

        plt.show()

    @abstractmethod
    def process_request_1(self, *args):
        pass

    @abstractmethod
    def process_request_2(self, *args):
        pass
