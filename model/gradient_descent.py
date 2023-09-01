from tqdm import tqdm
import numpy as np
from math import isnan

def estimatePrice(mileage, theta):
    return theta[0] + (theta[1] * mileage)

def update_theta(x_axis, y_axis, m, theta, learning_rates):
    temp_theta = theta
    theta0_sum = 0
    theta1_sum = 0
    for m in range(m):
        diff = estimatePrice(x_axis[m], temp_theta) - y_axis[m]
        theta0_sum += diff
        theta1_sum += (diff * x_axis[m])
    temp_theta[0] = temp_theta[0] - (((1 / m) * theta0_sum) * learning_rates) 
    temp_theta[1] = temp_theta[1] - (((1 / m) * theta1_sum) * learning_rates) 
    return temp_theta


def gradient_descent(x_axis, y_axis, epochs : int = 100, learning_rates : float = 0.001, theta = [0, 0], visualize : bool = False, batch_size : int = 1):
    try:
        assert len(x_axis) == len(y_axis)
        tmp_theta = theta
        m = len(x_axis)
        if visualize == False:
            v = tqdm(total=epochs, desc="Training...")
        else:
            v = range(epochs)
        for epoch in v:
            tmp_theta = update_theta(x_axis, y_axis, m, tmp_theta, learning_rates)
            if tmp_theta[1] == 0:
                print(f"training completed at epoch {epoch}... | learning_rates: {learning_rates} | theta0: {tmp_theta[0]} | theta1: {tmp_theta[1]}")
                break
            if isnan(tmp_theta[0]) or isnan(tmp_theta[1]):
                print(f"The model is not converging. Try to decrease the learning rate.")
                exit(1)
            if visualize == True and epoch % batch_size == 0:
                print(f"theta0: {tmp_theta[0]:20f} | theta1: {tmp_theta[1]:20f} | epochs: {epoch:15} | learning_rates: {learning_rates}")
        return tmp_theta
    except:
        print("Error: Invalid input.")
        exit(1)