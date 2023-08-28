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
        theta0, theta1 = get_theta()
        if theta0 == 0 and theta1 == 0:
            print('Error : Please train the model first')
            exit()
        return theta0 + (theta1 * input_x_data)

    @staticmethod
    def evaluate(x_data, y_data):
        pass
