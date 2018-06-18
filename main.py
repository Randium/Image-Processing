import matplotlib.pyplot as plt
import functions
import math

def thermostaat_plot()
    files = ['csv/Thermo_0.csv','csv/Thermo.csv','csv/Thermo_2.csv','csv/Thermo_3.csv']

    for bestand in files:
        plt.plot(import_data(bestand), 'r.')
    plt.show()

if __name__ == "__main__":
    thermostaat_plot()
