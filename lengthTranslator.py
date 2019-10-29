data = input().split()
d_length = {"mile": 1609, "yard": 0.9144, "foot": 0.3048, "inch": 0.0254, "km": 1000, "cm": 0.01, "mm": 0.001, "m": 1}
a = (float(data[0]) * d_length[data[1]]) / d_length[data[3]]
print(("{0:.2e}".format(a)))
