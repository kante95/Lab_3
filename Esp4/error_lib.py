from math import sqrt, log10, floor


def err_prop(x, dx, y, dy, operator):
    if operator == "+" or operator == "-":
        dz = sqrt(dx ** 2 + dy ** 2)
    elif operator == "*":
        dz = abs(x * y) * sqrt((dx / x) ** 2 + (dy / y) ** 2)
    elif operator == "/":
        dz = abs(x / y) * sqrt((dx / x) ** 2 + (dy / y) ** 2)
    return dz


def resolution_error(Delta_x):
    return (Delta_x / sqrt(12))


def error_mean(dx, N):
    return dx / N


def get_error(value, mode='R'):
    multimiter_setting = set_multimiter(mode)
    for ranges, xcent_val, xcent_range in multimiter_setting:
        if value < ranges:
            return (value * xcent_val) / 100 + (ranges * xcent_range) / 100


def set_multimiter(mode):
    if mode == 'R' or mode == 'Ohm':
        ranges = [200.0, 2000.0, 20000.0, 200000.0,
                  float(10 ** 6), float(10 ** 7)]
        percent_values = [0.010, 0.010, 0.010, 0.010, 0.012, 0.040]
        percent_ranges = [0.004, 0.001, 0.001, 0.001, 0.001, 0.001]
    elif mode == 'V':
        ranges = [0.2, 2.0, 20.0, 200.0, 1000.0]
        percent_values = [0.004, 0.0035, 0.004, 0.005, 0.0055]
        percent_ranges = [0.0025, 0.0006, 0.0005, 0.0006, 0.001]

    return zip(ranges, percent_values, percent_ranges)


def round_to_err(x, dx):
    to_decimal = - log10(dx) + 1
    return round(x, int(to_decimal))


def round_to_last2(x):
    return round(x, -int(floor(log10(abs(x)))) + 1)
