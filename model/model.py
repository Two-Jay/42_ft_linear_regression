import os

class Linear_Regression:
    @staticmethod
    def fit(x_data, y_data):
        pass

    @staticmethod
    def predict(input_x_data):
        try:
            with open(f"{os.getcwd()}/resources/theta.csv", 'r') as file:
                theta0, theta1 = [float(v.strip('')) for v in file.read().split(',')]
                return theta0 + (theta1 * input_x_data)
        except:
            print('Error : Please train the model first')

    @staticmethod
    def evaluate(x_data, y_data):
        pass
