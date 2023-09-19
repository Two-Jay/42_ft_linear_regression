import os
from gradient_descent import gradient_descent
import numpy as np


class Hyperparameters:
    def __init__(self, learning_rate, epochs, visualize, batch_size):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.visualize = visualize
        self.batch_size = batch_size

class BatchManager:
    @staticmethod
    def make(data : np.ndarray, batch_size : int):
        return [data[i:i+batch_size] for i in range(0, len(data), batch_size)]
    
    @staticmethod
    def make_batches(data : np.ndarray, batch_size : int):
        return [BatchManager.make(data[i], batch_size) for i in range(0, len(data), batch_size)]

class Data:
    def __init__(self, x, y, batch_size = None):
        assert len(x) == len(y)
        if batch_size is None:
            self.x = x
            self.y = y
        else:
            self.x = BatchManager.make_batches(x, batch_size)
            self.y = BatchManager.make_batches(y, batch_size)

    def __len__(self):
        return len(self.x)
    
    def __getitem__(self, index):
        return self.x[index], self.y[index]
    
    def __iter__(self):
        for i in range(len(self)):
            yield self[i]

def get_theta():
    try:
        with open(f"{os.getcwd()}/resources/theta.csv", 'r') as file:
            return [float(v.strip('')) for v in file.read().split(',')]
    except:
        return [0, 0]

class Linear_Regression:
    def __init__(options):
        pass

    @staticmethod
    def fit(data : Data, hyperparameters : Hyperparameters):
        theta = get_theta()
        result = gradient_descent()
        with open(f"{os.getcwd()}/resources/theta.csv", 'w') as file:
            file.write(f"{result[0]},{result[1]}")

    @staticmethod
    def set_arguments(epochs = 100, learning_rate = 0.001):
        pass

    @staticmethod
    def predict(input_x_data):
        theta = get_theta()
        return theta[0] + (theta[1] * input_x_data) if all(i == 0 for i in theta) == False else None

    @staticmethod
    def add_to_dataset(input_mileage, predicted_price):
        with open(f"{os.getcwd()}/resources/data.csv", 'a') as file:
            file.write(f"{input_mileage},{predicted_price}\n")

    @staticmethod
    def save_theta(theta0, theta1):
        with open(f"{os.getcwd()}/resources/theta.csv", 'w') as file:
            file.write(f"{theta0},{theta1}")

    @staticmethod
    def evaluate(x_data, y_data):
        pass