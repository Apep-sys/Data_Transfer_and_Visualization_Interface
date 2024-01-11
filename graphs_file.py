from PIL import Image
import pandas as pd
from matplotlib import pyplot as plt
import os
import customtkinter as ctk


class TopLevel(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry('600x400')


def show_graphs(param, instance):
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
        path = path + '\\grafic_temperatura.png'
        plt.savefig(path)
        temp_img = ctk.CTkImage(light_image=Image.open(path), size=(600, 400))
        print(instance.toplevel_opened)
        open_toplevel(instance, temp_img, param)

    elif 'Humid' in param:
        path = path + '\\grafic_umiditate.png'
        plt.savefig(path)
        humid_img = ctk.CTkImage(light_image=Image.open(path), size=(600, 400))
        open_toplevel(instance.toplevel_window, humid_img, instance)

    elif 'Speed' in param:
        path = path + '\\grafic_viteza.png'
        plt.savefig(path)
        speed_img = ctk.CTkImage(light_image=Image.open(path), size=(600, 400))
        open_toplevel(instance.toplevel_window, speed_img, instance)

    elif 'Presence' in param:
        path = path + '\\grafic_prezenta.png'
        plt.savefig(path)
        presence_img = ctk.CTkImage(light_image=Image.open(path), size=(600, 400))
        open_toplevel(instance.toplevel_window, presence_img, instance)

def open_toplevel(instance, img, param):
    if not instance.toplevel_opened:
        toplevel_window = TopLevel()
        instance.toplevel_opened = True
        ctk.CTkLabel(toplevel_window, image=img ).grid(column=0, row=0)
    else:
        instance.toplevel_window.focus()

