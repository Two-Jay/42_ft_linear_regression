from tqdm import tqdm
import numpy as np
from math import isnan

def estimatePrice(mileage, theta):
    return theta[0] + (theta[1] * mileage)

def gradient_descent(HP, P):