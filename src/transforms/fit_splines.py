import numpy as np
from scipy.interpolate import LSQUnivariateSpline


def fit_spline_coefficients(demand_vector, knots=(8, 16), degree=3):
    y = np.asarray(demand_vector, dtype=float)

    if len(y) != 26:
        raise ValueError(f"Expected 26 weekly values, got {len(y)}")

    x = np.linspace(0, 25, 26)
    spline = LSQUnivariateSpline(x, y, t=list(knots), k=degree)

    return spline.get_coeffs()