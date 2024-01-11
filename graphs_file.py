from PIL import Image, ImageTk
import pandas as pd
from matplotlib import pyplot as plt
import os

def show_graphs(param):
    path = 'D:\\Downloads\\Graph Pictures'

    if 'Temp' in param:
        df = pd.read_csv('D:\\Downloads\\Temp.csv')
        plt.xlabel('Index')
        plt.ylabel('Temperatura')
        plt.title('Graficul temperaturii')

    elif 'Humid' in param:
        df = pd.read_csv('D:\\Downloads\\Umiditate.csv')
        plt.xlabel('Index')
        plt.ylabel('Umiditate')
        plt.title('Graficul umiditatii')

    elif 'Speed' in param:
        df = pd.read_csv('D:\\Downloads\\Viteza.csv')
        plt.xlabel('Index')
        plt.ylabel('Viteza')
        plt.title('Graficul vitezei')

    elif 'Presence' in param:
        df = pd.read_csv('D:\\Downloads\\Prezenta.csv')
        plt.xlabel('Index')
        plt.ylabel('Prezenta')
        plt.title('Graficul prezentei')

    temp_data = {}
    col_names = df.columns.tolist()
    index_x = df['Index'].tolist()

    for index, name in enumerate(col_names[1:]):
        data = df[name].tolist()
        temp_data[name] = data

    for data in temp_data:
        plt.plot(index_x, temp_data.get(data), label=data)

    if os.path.exists(path):
        pass
    else:
        try:
            os.makedirs(path, exist_ok=True)
            print(f'Directory {path} created successfully.')
        except OSError as error:
            print(f'Directory {path} could not be created.')

    if 'Temp' in param:
        plt.savefig(path + '\\grafic_temperatura.png')
    elif 'Humid' in param:
        plt.savefig(path + '\\grafic_umiditate.png')
    elif 'Speed' in param:
        plt.savefig(path + '\\grafic_viteza.png')
    elif 'Presence' in param:
        plt.savefig(path + '\\grafic_prezenta.png')


