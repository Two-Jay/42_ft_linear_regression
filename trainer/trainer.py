import sys
import os
sys.path.insert(0, f'{os.getcwd()}/model')
from model import Linear_Regression
from Data_loader import Load_Code, Load_options_Code

def main():
    d = Load_Code.load('./resources/data.csv')
    model = Linear_Regression()
    options = Load_options_Code.load()
    model.fit(d.mileages, d.prices, options['learning_rate'], options['epochs'], options['visualize'], options['batch_size'])

if __name__ == '__main__':
    main()
