import sys
import os
sys.path.insert(0, f'{os.getcwd()}/model')
from model import Linear_Regression

def load_theta(path = './resources/theta.csv'):
    try:
        with open(path, 'r') as file:
            return [float(v.strip('')) for v in file.read().split(',')]
    except:
        return [0, 0]

def main():
    model = Linear_Regression()
    input_mileage = float(input('Enter mileage: '))
    theta0, theta1 = load_theta()
    if theta0 == 0 and theta1 == 0:
        print('Error : Please train the model first')
    else:
        print(model.predict(input_mileage))

if __name__ == '__main__':
    main()
