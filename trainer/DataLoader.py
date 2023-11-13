import json
import csv
import os

class CarData():
    def __init__(self, mileages: list, prices: list):
        self.mileages = mileages
        self.prices = prices

    def column_name(self):
        return ['km', 'price']

class DataLoader():
    @staticmethod
    def load(file_path: str) -> CarData:
        # read_csv
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            mileages = []
            prices = []
            for row in reader:
                mileages.append(float(row['km']))
                prices.append(float(row['price']))
            return CarData(mileages, prices)

class OptionsLoader():
    @staticmethod
    def load(file_path: str = f"{os.getcwd()}/resources/options.json") -> dict:
        # read_csv
        with open(file_path, 'r') as file:
            reader = json.load(file)
            return {
                'learning_rate': reader['learning_rate'],
                'epochs': reader['epochs'],
                'verbose': reader['verbose']['is_verbose'] == 'True'
                    or reader['verbose']['is_verbose'] == 'true',
                'verbose_presision': reader['verbose']['presision'],
                "test_split_rates" : reader['data_split']["test"],
                "validation_split_rates" : reader['data_split']["validation"],
            }
        