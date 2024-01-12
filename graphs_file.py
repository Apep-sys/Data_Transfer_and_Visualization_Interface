from PIL import Image, ImageTk
import pandas as pd
from matplotlib import pyplot as plt
import os
import customtkinter as ctk

class TopLevel(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry('600x400')


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

    toplevel_window = None

    if 'Temp' in param:
        path = os.path.join(path, f'grafic_temperatura.png')
        plt.savefig(path)
        temp_img = ctk.CTkImage(light_image=Image.open(path), size=(600, 400))
        open_toplevel(temp_img, toplevel_window)
        plt.clf()

    elif 'Humid' in param:
        path = os.path.join(path, f'grafic_umiditate.png')
        plt.savefig(path)
        humid_img = ctk.CTkImage(light_image=Image.open(path), size=(600, 400))
        open_toplevel(humid_img)
        plt.clf()

    elif 'Speed' in param:
        path = os.path.join(path, f'grafic_viteza.png')
        plt.savefig(path)
        speed_img = ctk.CTkImage(light_image=Image.open(path), size=(600, 400))
        open_toplevel(speed_img)
        plt.clf()

    elif 'Presence' in param:
        path = os.path.join(path, f'grafic_prezenta.png')
        plt.savefig(path)
        presence_img = ctk.CTkImage(light_image=Image.open(path), size=(600, 400))
        open_toplevel(presence_img)
        plt.clf()


def open_toplevel(img, toplevel_window=None):
    if toplevel_window is None or toplevel_window.winfo_exists():
        toplevel_window = TopLevel()
        ctk.CTkLabel(toplevel_window, image=img).grid(column=0, row=0)
        toplevel_window = True
        return toplevel_window

    else:
        toplevel_window.focus()

