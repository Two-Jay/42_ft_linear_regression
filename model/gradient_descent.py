def estimatePrice(mileage, theta):
    return theta[0] + (theta[1] * mileage)

def update_theta(x_axis, y_axis, m, theta, learning_rates):
    theta0_sum = 0
    theta1_sum = 0
    for m in range(m):
        diff = estimatePrice(x_axis[0], theta) - y_axis[0]
        theta0_sum += diff
        theta1_sum += diff * x_axis[0]
    theta[0] = learning_rates * ((1 / m) * theta0_sum)
    theta[1] = learning_rates * ((1 / m) * theta1_sum)
    return theta


def gradient_descent(x_axis, y_axis, epochs : int = 100, learning_rates : float = 0.001, theta = [0, 0]):
    try:
        assert len(x_axis) == len(y_axis)
        tmp_theta = theta
        m = len(x_axis)
        for epoch in range(epochs):
            tmp_theta = update_theta(x_axis, y_axis, m, tmp_theta, learning_rates)
            if epoch % 50 == 0:
                print(f"Epoch {epoch + 1}/{epochs} - theta0: {tmp_theta[0]} - theta1: {tmp_theta[1]} | learning_rates: {learning_rates}")
        return tmp_theta
    except:
        print("Error: Invalid input.")
        exit(1)