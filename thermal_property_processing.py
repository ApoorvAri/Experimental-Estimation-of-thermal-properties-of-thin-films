import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
from sklearn.linear_model import LinearRegression

data = pd.read_csv("temperature_data.csv")

x = data["X"]
T = [data[c] for c in ["a","b","c","d","e","f","g","h"]]

def input_func(x, A, w, phi, offset):
    return A * np.sin(w * x + phi) + offset

phase = []
Temp = []

for signal in T:
    params, _ = curve_fit(input_func, x, signal)

    phase.append(params[2])
    Temp.append(params[3])

    fitted = input_func(x, *params)

    plt.figure()
    plt.plot(x, signal, 'o', label="Measured Data")
    plt.plot(x, fitted, '--', label="Fitted Curve")
    plt.xlabel("Time (s)")
    plt.ylabel("Temperature")
    plt.legend()
    plt.show()

Dist_U = np.array([0.00,0.01,0.02,0.03]).reshape(-1,1)
Dist_D = np.array([0.01,0.02,0.03,0.04]).reshape(-1,1)

U_ph = np.array(phase[:4]).reshape(-1,1)
D_ph = np.array(phase[4:]).reshape(-1,1)

U_T = np.array(Temp[:4]).reshape(-1,1)
D_T = np.array(Temp[4:]).reshape(-1,1)

Up_predict = np.array([0.04]).reshape(-1,1)
Dp_predict = np.array([0.00]).reshape(-1,1)

model = LinearRegression()

model.fit(Dist_U, U_ph)
Ph1 = float(model.predict(Up_predict)[0])

model.fit(Dist_D, D_ph)
Ph2 = float(model.predict(Dp_predict)[0])

model.fit(Dist_U, U_T)
Ts1 = float(model.predict(Up_predict)[0])

model.fit(Dist_D, D_T)
Ts2 = float(model.predict(Dp_predict)[0])

print("Upper Surface Phase (Ph1):", Ph1)
print("Lower Surface Phase (Ph2):", Ph2)
print("Upper Surface Temp  (Ts1):", Ts1)
print("Lower Surface Temp  (Ts2):", Ts2)
