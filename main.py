import numpy as np
import matplotlib.pyplot as plt


def generate_1d_data(n=128, sins=5):
    x = np.linspace(1, n, n)
    freqs = np.random.normal(0, 1, size=sins)
    y = [np.sin(x * freq) for freq in freqs]
    return np.sum(np.array(y), axis=0)


def main():
    test_1d = generate_1d_data()
    plt.plot(test_1d)
    plt.show()
    print('a')


if __name__ == "__main__":
    main()
