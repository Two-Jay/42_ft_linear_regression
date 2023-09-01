def estimatePrice(mileage, theta0, theta1):
    return theta0 + (theta1 * mileage)

def gradient_descent(x_axis, y_axis, m : int, epochs : int = 100, learning_rates : float = 0.001, theta = [0, 0]):
    try:
        assert len(x_axis) == len(y_axis)
        for epoch in range(epochs):
            dir = 1 / m
            limit_range = range(m)
            tmp_theta0 = learning_rates * dir * sum([estimatePrice(x_axis[i], theta[0], theta[1]) - y_axis[i] for i in limit_range])
            tmp_theta1 = learning_rates * dir * sum([(estimatePrice(x_axis[i], theta[0], theta[1]) - y_axis[i]) * x_axis[i] for i in limit_range])
            theta = [tmp_theta0, tmp_theta1]
            print(f"Epoch {epoch + 1} : theta0 = {theta[0]}, theta1 = {theta[1]}")
        return theta
    except:
        print("Error: Invalid input.")
        exit(1)