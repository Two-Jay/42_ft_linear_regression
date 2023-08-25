import csv

class Car_Data():
    def __init__(self, source : dict):
        self.km = source['km']
        self.price = source['price']

class Load_Code():
    @staticmethod
    def load(file_path : str) -> Car_Data:
        # read_csv
        dict = {}
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            dict['km'] = [int(row['km']) for row in reader]
            dict['price'] = [int(row['price']) for row in reader]
        return Car_Data(dict)