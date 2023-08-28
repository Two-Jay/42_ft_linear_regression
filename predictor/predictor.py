import sys
import os
sys.path.insert(0, f'{os.getcwd()}/model')
from model import Linear_Regression
    
def get_input_mileage() -> float:
    try:
        return float(input('Enter mileage: '))
    except:
        print('Invalid input. Please try again.')
        return get_input_mileage()

def main():
    prediction = Linear_Regression.predict(get_input_mileage())
    if prediction != None:
        print(f'Estimated price: {prediction}')
    else:
        print('Model is not trained yet. Please run trainer.py first.')

if __name__ == '__main__':
    main()
