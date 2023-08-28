import sys
import os
sys.path.insert(0, f'{os.getcwd()}/model')
from model import Linear_Regression
from Data_loader import Load_Code

def main():
    d = Load_Code.load('./resources/data.csv')
    model = Linear_Regression()
    model.fit(d.mileages, d.prices)

if __name__ == '__main__':
    main()
