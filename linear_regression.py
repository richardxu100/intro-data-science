import numpy as np 

def find_m(x_s, y_s):
    x_mean = x_s.mean()
    y_mean = y_s.mean()
    top_value = 0
    for i in range(len(x_s)):
        top_value += (x_s[i]-x_mean)*(y_s[i]-y_mean)
    bot_value = 0
    for x in x_s:
        bot_value += (x-x_mean)**2
    return top_value / bot_value


def find_slope_and_intercept(data_path):
    points = np.genfromtxt(data_path, delimiter=',')
    print(points)
    x_s, y_s = points[:, 0], points[:, 1]
    m = find_m(x_s, y_s)
    b = y_s.mean() - m*x_s.mean()
    print(m)
    print(b)


if __name__ == '__main__':
    find_slope_and_intercept('./linear_regression_live/data.csv')
