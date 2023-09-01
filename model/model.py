import os
from gradient_descent import gradient_descent

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
    def fit(x_data, y_data, learning_rate, epochs, visualize = False, batch_size = 1):
        theta = get_theta()
        result = gradient_descent(x_data, y_data, epochs, learning_rate, theta, visualize, batch_size)
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