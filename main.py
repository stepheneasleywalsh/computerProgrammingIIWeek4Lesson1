import matplotlib.pyplot as p

values = [14.23, 14.35, 14.22, 14.42, 14.54, 14.36, 14.33, 14.45, 14.51, 14.52, 14.48, 14.55, 14.50, 14.49, 14.41, 14.50, 14.56, 14.43, 14.48, 14.52, 14.59]

p.plot(values, marker="o") # Add a marker dot
p.title("Global Mean Temperature from 1994 to 2014")
p.ylabel("Temp / °C")
p.xlabel("Number of Years Since 1994")
p.show()

quit()
