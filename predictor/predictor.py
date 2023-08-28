import sys
import os
sys.path.insert(0, f'{os.getcwd()}/model')
from model import Linear_Regression
    
def main():
    model = Linear_Regression()
    input_mileage = float(input('Enter mileage: '))
    prediction = model.predict(input_mileage)
    if prediction != None:
        print(f'Estimated price: {prediction}')

if __name__ == '__main__':
    main()
