import os

def get_theta():
    try:
        with open(f"{os.getcwd()}/resources/theta.csv", 'r') as file:
            return [float(v.strip('')) for v in file.read().split(',')]
    except:
        print('Error : Please train the model first')
        exit()

class Linear_Regression:
    @staticmethod
    def fit(x_data, y_data):
        pass

    @staticmethod
    def predict(input_x_data):
        theta0, theta1 = get_theta()
        return theta0 + (theta1 * input_x_data)

    @staticmethod
    def evaluate(x_data, y_data):
        pass
