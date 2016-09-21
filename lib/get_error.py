def get_error(value, type='R'):
    error = None
    if type == 'R':
        error = get_error_resistance(float(value))
    return error


def get_error_resistance(value):
    ranges = [200.0, 2000.0, 20000.0, 200000.0, float(10 ** 6), float(10 ** 7)]
    percent_values = [0.010, 0.010, 0.010, 0.010, 0.012, 0.040]
    percent_ranges = [0.004, 0.001, 0.001, 0.001, 0.001, 0.001]
    multimiter_setting = zip(ranges, percent_values, percent_ranges)
    for ranges, xcent_val, xcent_range in multimiter_setting:
        if value < ranges:
            return calculate_err(value, ranges, xcent_val, xcent_range)


def calculate_err(value, ranges, xcent_val, xcent_range):
    return (value * xcent_val) / 100 + (ranges * xcent_range) / 100

print get_error(1000)
