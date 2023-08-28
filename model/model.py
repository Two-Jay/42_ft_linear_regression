import os
from mutils import gradient_descent

def get_theta():
    try:
        with open(f"{os.getcwd()}/resources/theta.csv", 'r') as file:
            return [float(v.strip('')) for v in file.read().split(',')]
    except:
        return [0, 0]

class Linear_Regression:
    @staticmethod
    def fit(x_data, y_data, learning_rate):
        pass

    @staticmethod
    def predict(input_x_data):
        theta = get_theta()
        return theta[0] + (theta[1] * input_x_data) if all(i == 0 for i in theta) == False else None

    @staticmethod
    def evaluate(x_data, y_data):
        pass
