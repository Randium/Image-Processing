import matplotlib.pyplot as plt
import math

files = ['Thermostaat_0.csv','Thermostaat_1.csv','Thermostaat_2.csv','Thermostaat_3.csv']

for bestand in files:
    input_file = open(bestand, 'r')


    Tijd = []
    Spanning = []

    for line in input_file:
        data_opgeknipt = line.split(',')
        #if data_opgeknipt[1] != "-2.56000" and data_opgeknipt[1] != "-2.54000":
        Tijd.append(float(data_opgeknipt[0]))
        Spanning.append(float(data_opgeknipt[1]))



    plt.plot(Tijd, Spanning, 'r.')
plt.show()