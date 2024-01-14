from PIL import Image
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import os
import customtkinter as ctk



class TopLevel(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry('600x400')


toplevel_open = {'Temp': None, 'Humid': None, 'Speed': None, 'Presence': None}


def show_graphs(param, toplevel_open=toplevel_open):
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

    for name in col_names[1:]:
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

    path = os.path.join(path, f'grafic_{param.lower()}.png')
    plt.savefig(path)
    img = ctk.CTkImage(light_image=Image.open(path), size=(600, 400))
    open_toplevel(img, toplevel_open, param)
    plt.clf()


def open_toplevel(img, toplevel_open, param):
    if not toplevel_open[param]:

        #TODO Rename the toplevel's titles.
        toplevel_open[param] = TopLevel()

        toplevel_x = 900
        toplevel_y = 200
        toplevel_width = 600
        toplevel_height = 400
        #TODO Could add taking the app's window geometry characteristics to update properly in case of resizing.

        # Setam geometria ferestrei TopLevel deschise
        toplevel_open[param].geometry(f'{toplevel_width}x{toplevel_height}+{toplevel_x}+{toplevel_y}')

        ctk.CTkLabel(toplevel_open[param], image=img).grid(column=0, row=0)
    else:
        toplevel_open[param].lift()  # Aduce fereastra in fata
        toplevel_open[param].focus_force() # Forteaza ca focusul sa fie pe fereastra deschisa, la fiecare apasare de buton

