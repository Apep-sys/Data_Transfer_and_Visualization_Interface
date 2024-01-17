import pandas as pd

def process_csv(type, path, mode):
    ''''
    Functia proceseaza un fisier in functie de extensia fisierului. Prin aceasta procesare, se extrag numele
    coloanelor, reprezentate de parametri fizici si datele acestora.

    Parametri:
    ---------
    type: string - tipul extensiei fisierului dat CSV/XLSX
    path: string - calea fisierului dat
    mode: string - tmodul in care sa se descarce fisierul dat CSV/XLSX
    '''

    # Se citește fișierul CSV sau XLSX în funcție de tipul specificat
    if type == 'CSV':
        df = pd.read_csv(path)
    elif type == 'XLSX':
        df = pd.read_excel(path, sheet_name='Sheet1', index_col=0)

    # Se obțin numele coloanelor și se organizează în liste diferite în funcție de tipul acestora
    col_names = df.columns.tolist()
    temp_file = []
    umid_file = []
    prezenta_file = []
    viteza_file = []
    file_list = {'Temp': temp_file, 'Umiditate': umid_file, 'Prezenta': prezenta_file, 'Viteza': viteza_file}

    for name in col_names:
        if 'Temp' in name:
            temp_file.append(name)
        elif 'Umiditate' in name:
            umid_file.append(name)
        elif 'Prezenta' in name:
            prezenta_file.append(name)
        elif 'Viteza' in name:
            viteza_file.append(name)

    # Se procesează fiecare tip de fișier și se salvează ca CSV sau XLSX în funcție de modul specificat
    for file in file_list:
        if file_list.get(file):
            csv_file = df[file_list.get(file)]
        if mode == 'CSV':
            csv_file.to_csv(f'D:\\Downloads\\{file}.csv', index_label='Index')
        elif mode == 'XLSX':
            csv_file.to_excel(f'D:\\Downloads\\{file}.xlsx', sheet_name='Sheet1', index_label='Index')

def create_csv(p):
    ''''
        Functia creeaza un fisier in functie de lista tip Queue primita, din care preia date.
        Functia decodeaza si adauga in modul append datele intr-un fisier CSV, organizat pe doua coloane.

        Parametri:
        ---------
        p - lista tip Queue ce contine datele de la Arduino
        '''
    data_list = []

    # Anuntam inceperea si terminarea thread-ului.
    print('Thread-ul CSV a început!')
    for i in range(50):
        data = p.get()
        # Datele din lista Queue sunt preluate si decodate pentru a fi puse in fisierul CSV
        data = data.decode('utf-8', errors='ignore')

        if data:
            data_list.append([i, data])

    # Se creează un DataFrame și se adaugă la fișierul CSV
    df = pd.DataFrame(data_list, columns=['Index', 'Data'])
    df.to_csv(r'D:\Downloads\Date_Microcontroller.csv', mode='a', header=False, index=False, index_label='Index')
    print('Thread-ul CSV s-a încheiat.')
