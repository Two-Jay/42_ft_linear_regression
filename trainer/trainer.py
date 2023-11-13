import sys
import os
sys.path.append(f"{os.getcwd()}/model")
from model import LinearRegression
from Scaling import MaxAbsScaler
from DataLoader import DataLoader, OptionsLoader

def main():
    d = DataLoader.load('./resources/data.csv')
    model = LinearRegression()
    options = OptionsLoader.load()
    print(f'options: {options}')
    model.compile(
        lr=options['learning_rate'],
        epochs=options['epochs'],
        verbose=options['verbose']
    )
    scaler = MaxAbsScaler()
    scaler.fit(d.mileages)
    d.mileages = scaler.transform(d.mileages)
    d.prices = scaler.transform(d.prices)
    model.fit(d.mileages, d.prices)
    print("Model trained")

if __name__ == '__main__':
    main()
