import matplotlib.pyplot as plt
import numpy as np
import math

N = 10
dataset = {
    "T": [298.6, 315.6, 332.3, 346.9, 359.5, 371.1, 382.9, 396.0, 407.9, 421.5],
    "L": [163, 169, 173, 183, 187, 196, 192, 200, 199, 205],
    "V": [326, 338, 346, 366, 374, 392, 384, 400, 398, 410]
}

dL = 2 * math.sqrt(2)
bL = [dL / i * 100 for i in dataset["L"]]

bV = [0.01 * math.sqrt(4 + i ** 2) for i in bL]
V2 = [pow(i, 2) / 1000 for i in dataset["V"]]
dV = [2 * V2[i] * bV[i] for i in range(0, N)]

Xi = sum(dataset["T"])
Xi2 = sum([math.pow(i, 2) for i in dataset["T"]])
Yi = sum(V2)
XiYi = sum([dataset["T"][i] * V2[i] for i in range(0, N)])
k = (Yi * Xi - N * XiYi) / (math.pow(Xi, 2) - N * Xi2)
b = (XiYi * Xi - Yi * Xi2) / (math.pow(Xi, 2) - N * Xi2)

print(f"Calculated: k={k}, b={b}")

fig, ax = plt.subplots()
ax.set_xticks(range(280, 430, 5), minor=True)
ax.set_yticks(range(100, 180, 5), minor=True)
ax.yaxis.grid(True, which='minor')
ax.xaxis.grid(True, which='minor')
plt.grid(True)

plt.xlim(280, 430)
plt.ylim(100, 180)

plt.errorbar(dataset["T"], V2, yerr=dV, fmt=".", ecolor="red")
x = np.linspace(280, 430, 2)
y = k * x + b
plt.plot(x, y, color="green")

plt.title("График 2.6а.1, \"Зависимость квадрата скорости звука в воздухе от температуры\"",
          color="gray", fontsize=9, pad=12)
plt.xlabel("T, К", color="gray")
plt.ylabel("v² * 10³, (м/с²)²", color="gray")

plt.show()
