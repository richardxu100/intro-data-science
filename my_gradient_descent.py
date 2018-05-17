import numpy as np 

def compute_error_for_given_points(b, m, points):
    totalError = 0
    for point in points:
        x_i, y_i = point
        totalError += (y_i - (m*x_i + b))**2
    return totalError / len(points)


def step_gradient(b_current, m_current, learning_rate, points):
    b_gradient = 0
    m_gradient = 0
    N = len(points)
    for point in points:
        x_i, y_i = point 
        b_gradient += -(2/N) * (y_i - (m_current*x_i + b_current))
        m_gradient += -(2/N) * x_i*(y_i - (m_current*x_i + b_current))
    new_b = b_current - learning_rate*b_gradient
    new_m = m_current - learning_rate*m_gradient
    return new_b, new_m
    

def gradient_descent_runner(starting_b, starting_m, learning_rate, points, num_iterations):
    b, m = starting_b, starting_m
    for i in range(num_iterations):
        b, m = step_gradient(b, m, learning_rate, points)
    return b, m


def run():
    points = np.genfromtxt('./linear_regression_live/data.csv', delimiter=',')
    starting_b = 0
    starting_m = 0
    learning_rate = .0001
    num_iterations = 10000
    print('Starting gradient at b: {}, m: {}, error: {}'.format(starting_b,
                                                                starting_m, compute_error_for_given_points(starting_b, starting_m, points)))
    b, m = gradient_descent_runner(starting_b, starting_m, learning_rate, points, num_iterations)
    print('Ending gradient at b: {}, m: {}, error: {}'.format(b,
                                                                m, compute_error_for_given_points(b, m, points)))

if __name__ == '__main__':
    run()
