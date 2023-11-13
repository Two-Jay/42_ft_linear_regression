import os
import numpy as np

def _gradient_descent(x, y, theta_0, theta_1, learning_rate):
    m = len(y)
    sum_errors_theta_0 = 0
    sum_errors_theta_1 = 0

    for i in range(m):
        prediction = _predict(x[i], theta_0, theta_1)
        error = prediction - y[i]
        sum_errors_theta_0 += error
        sum_errors_theta_1 += error * x[i]

    temp_theta_0 = theta_0 - learning_rate * (1/m) * sum_errors_theta_0
    temp_theta_1 = theta_1 - learning_rate * (1/m) * sum_errors_theta_1
    return [temp_theta_0, temp_theta_1]

class Hyperparameters:
    def __init__(self, learning_rate, epochs, verbose):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.verbose = verbose

    def validate(self):
        if self.learning_rate <= 0:
            raise ValueError('learning_rate must be greater than 0')
        if self.epochs <= 0:
            raise ValueError('epochs must be greater than 0')
        if not isinstance(self.verbose, bool):
            raise TypeError('verbose must be a boolean')

def get_theta():
    try:
        with open(f"{os.getcwd()}/resources/theta.csv", 'r') as file:
            return [float(v.strip('')) for v in file.read().split(',')]
    except:
        return [0, 0]
    
def save_theta(theta):
    with open(f"{os.getcwd()}/resources/theta.csv", 'w') as file:
        file.write(','.join([str(v) for v in theta]))

def _predict(x, theta_0, theta_1):
    return theta_0 + (theta_1 * x)

def validate_Hyperparameters(f):    
    def wrapper(*args, **kwargs):
        args[0].hyperparameters.validate()
        return f(*args, **kwargs)
    return wrapper

class LinearRegression:
    def __init__(options):
        pass

    @classmethod
    def compile(cls, lr, epochs, verbose):
        cls.hyperparameters = Hyperparameters(
            learning_rate=lr,
            epochs=epochs,
            verbose=verbose
        )

    @classmethod
    @validate_Hyperparameters
    def fit(cls, x, y):
        theta = get_theta()
        for i, _ in enumerate(range(cls.hyperparameters.epochs)):
            theta = _gradient_descent(x, y, theta[0], theta[1], cls.hyperparameters.learning_rate)
            if cls.hyperparameters.verbose == True:
                print(f'Epoch {i} : Current theta: {theta}')
        save_theta(theta)
        return theta
    
    @classmethod
    def predict(cls, x):
        theta_0, theta_1 = get_theta()
        return _predict(x, theta_0, theta_1)