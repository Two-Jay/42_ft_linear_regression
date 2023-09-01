import tqdm

def estimatePrice(mileage, theta):
    return theta[0] + (theta[1] * mileage)

def update_theta(x_axis, y_axis, m, theta, learning_rates):
    temp_theta = theta
    theta0_sum = 0
    theta1_sum = 0
    for m in range(m):
        diff = estimatePrice(x_axis[m], theta) - y_axis[m]
        theta0_sum += diff
        theta1_sum += diff * x_axis[m]
    temp_theta[0] = temp_theta[0] - (((1 / m) * theta0_sum) * learning_rates) 
    temp_theta[1] = temp_theta[1] - (((1 / m) * theta1_sum) * learning_rates) 
    return temp_theta


def gradient_descent(x_axis, y_axis, epochs : int = 100, learning_rates : float = 0.001, theta = [0, 0]):
    try:
        assert len(x_axis) == len(y_axis)
        tmp_theta = theta
        m = len(x_axis)
        for epoch in tqdm.tqdm(range(epochs)):
            tmp_theta = update_theta(x_axis, y_axis, m, tmp_theta, learning_rates)
        print(f"theta0: {tmp_theta[0]} | theta1: {tmp_theta[1]} | epochs: {epochs} | learning_rates: {learning_rates}")
        return tmp_theta
    except:
        print("Error: Invalid input.")
        exit(1)