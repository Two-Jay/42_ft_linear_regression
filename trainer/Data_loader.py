import csv
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
            return Car_Data([float(row['km']) for row in reader], [float(row['price']) for row in reader])
