from PIL import Image, ImageTk
import pandas as pd
from matplotlib import pyplot as plt

def show_graphs(param):
    if 'Temp' in param:
        df = pd.read_csv('D:\\Downloads\\Temp.csv')
        temp_data = {}
        col_names = df.columns.tolist()
        index_x = df['Index'].tolist()

        for index, name in enumerate(col_names[1:]):
            data = df[name].tolist()
            temp_data[name] = data

        for data in temp_data:
            plt.plot(index_x, temp_data.get(data), label=data)

        plt.xlabel('Index')
        plt.ylabel('Temperatura')
        plt.title('Temp Graph')
        plt.savefig('temp_graf.png')