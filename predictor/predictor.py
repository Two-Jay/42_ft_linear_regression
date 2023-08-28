import sys
import os
sys.path.insert(0, f'{os.getcwd()}/model')
from model import Linear_Regression

err_message = {
    'invalid_input': 'Invalid input. Please try again.',
    'model_not_trained': 'Model is not trained yet. Please run trainer.py first.'
}
    
def get_input_mileage() -> float:
    try:
        return float(input('Enter mileage: '))
    except:
        print(err_message['invalid_input'])
        return get_input_mileage()

def main():
    input_mileage = get_input_mileage()
    prediction = Linear_Regression.predict()
    if prediction != None:
        print(f'Estimated price: {prediction}')
        Linear_Regression.add_to_dataset(input_mileage, prediction)
    else:
        print(err_message['model_not_trained'])

if __name__ == '__main__':
    main()
