import sys
import os
sys.path.append(f"{os.getcwd()}/model")
from model import LinearRegression

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
    prediction = LinearRegression.predict(input_mileage)
    if prediction != None:
        prediction = int(prediction)
        mileage = int(input_mileage)
        print(f'Estimated price: {prediction} | Mileage: {mileage}')
    else:
        print(err_message['model_not_trained'])

if __name__ == '__main__':
    main()
