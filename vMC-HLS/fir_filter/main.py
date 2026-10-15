import numpy as np
import matplotlib.pyplot as plt

def plot(fixed):
    plt.plot(fixed)
    plt.ylim(0, 1)
    plt.title("FIR Filter Data")
    plt.show()

def fuzz(fixed):
    rng = np.random.default_rng()
    noise = fixed + rng.normal(0, 0.1, len(fixed))
    return np.clip(noise, 0, 1)

if "__main__" == __name__:
    ITEMS = 1024
    file_name = "./data/sine.bin"

    data = np.fromfile(file_name, dtype=np.uint16, count=ITEMS)
    fixed = data / 65535.0

    plot(fuzz(fixed))