import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Depth Data.csv")

time = df["Point"]
depth = df["Depth (m)"]

plt.figure(figsize=(10, 5))
plt.plot(time, depth)

plt.xlabel("Time / Data Point")
plt.ylabel("Depth (m)")
plt.title("Depth-Time Graph of the Ship")
plt.grid(True)

plt.show()
