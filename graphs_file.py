from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd
import os
import customtkinter as ctk

'''Fisierul care contine clase si metode relevante pentru generarea graficelor.'''

class TopLevel(ctk.CTkToplevel):
    '''
    Clasa care mosteneste widget-ul TopLevel.

    Metode:
    ------
    init - constructorul normal; initializeaza marimea ferestrei de TopLevel
    ------
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry('600x400')

# Lista cu perechi cheie:valoare pentru a verifica daca noua fereastra a unui parametru este deja deschisa
toplevel_open = {'Temp': None, 'Humid': None, 'Speed': None, 'Presence': None, 'Live Graph': None}


def show_graphs(param, toplevel_open=toplevel_open):
    '''
    Functia afiseaza diferitele grafice ale parametrilor din toplevel_open si le salveaza intr-un folder Graph Pictures.

    Parametri:
    ---------
    param: string - tipul parametrului pentru care se face grafic ex. temp, umiditate
    toplevel_open: string - variabila pentru a verifica daca respectiva fereastra TopLevel este deja deschisa
    ---------
    '''

    # Se verifica parametri, se citesc fisierele CSV corespunzatoare si se ploteaza in consecinta
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

    # Folosindu-ne de numele coloanelor, preluam datele de pe acestea si le punem in dictionarul temp_data
    temp_data = {}
    col_names = df.columns.tolist()
    index_x = df['Index'].tolist()

    for name in col_names[1:]:
        data = df[name].tolist()
        temp_data[name] = data

    # Odata puse in dictionar, acestea sunt plotuite in functie de index si date insesi
    for data in temp_data:
        plt.plot(index_x, temp_data.get(data), label=data)

    # Daca nu exista folderul din path, acesta se creeaza. Daca exista deja, nu face nimic.
    # Intampinarea unei erori va afisa un mesaj, care spune ca folderul nu a fost creat.
    if os.path.exists(path):
        pass
    else:
        try:
            os.makedirs(path, exist_ok=True)
            print(f'Directory {path} created successfully.')
        except OSError as error:
            print(f'Directory {path} could not be created.')

    # Se creeaza noul path pentru imaginea graficului, alcatuita din numele acesteia si extensia .png
    path = os.path.join(path, f'grafic_{param.lower()}.png')
    plt.savefig(path)
    img = ctk.CTkImage(light_image=Image.open(path), size=(600, 400))

    # Dupa salvarea si deschiderea imaginii folosind CTkImage, aceasta este deschisa intr-o noua fereastra
    open_toplevel(img, toplevel_open, param)

    # Graficul este curatat, pentru a nu se suprapune intre ele
    plt.clf()


def open_toplevel(img, toplevel_open, param):

    if not toplevel_open[param]:

        toplevel_open[param] = TopLevel()
        toplevel_open[param].title('Graph Window')

        toplevel_x = 1100
        toplevel_y = 200
        toplevel_width = 600
        toplevel_height = 400

        # Setam geometria ferestrei TopLevel deschise
        toplevel_open[param].geometry(f'{toplevel_width}x{toplevel_height}+{toplevel_x}+{toplevel_y}')

        ctk.CTkLabel(toplevel_open[param], text='', image=img).grid(column=0, row=0)
    else:
        toplevel_open[param].lift()  # Aduce fereastra in fata
        toplevel_open[param].focus_force() # Forteaza ca focusul sa fie pe fereastra deschisa, la fiecare apasare de buton

