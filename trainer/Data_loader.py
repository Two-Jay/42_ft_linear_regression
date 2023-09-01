import json
import csv
import os

class Car_Data():
    def __init__(self, mileages: list, prices: list):
        self.mileages = mileages
        self.prices = prices

    def column_name(self):
        return ['km', 'price']

class Load_Code():
    @staticmethod
    def load(file_path: str) -> Car_Data:
        # read_csv
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            mileages = []
            prices = []
            for row in reader:
                mileages.append(float(row['km']))
                prices.append(float(row['price']))
            return Car_Data(mileages, prices)

class Load_options_Code():
    @staticmethod
    def load(file_path: str = f"{os.getcwd()}/resources/options.json") -> dict:
        # read_csv
        with open(file_path, 'r') as file:
            reader = json.load(file)
            return {
                'epochs': int(reader['epochs']) if reader['epochs'] != 'None' else 100,
                'learning_rate': float(reader['learning_rate']) if reader['learning_rate'] != 'None' else 0.001,
                'batch_size': int(reader['batch_size']) if reader['batch_size'] != 'None' else 1,
                'visualize': bool(reader['visualize']) if reader['visualize'] != 'None' else False,
            }