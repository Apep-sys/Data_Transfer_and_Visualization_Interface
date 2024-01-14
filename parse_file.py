import pandas as pd


def process_csv(type, path, mode):
    if type == 'CSV':
        df = pd.read_csv(path)
    elif type == 'XLSX':
        df = pd.read_excel(path, sheet_name='Sheet1', index_col=0)

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

    for file in file_list:
        if file_list.get(file):
            csv_file = df[file_list.get(file)]
        if mode == 'CSV':
                csv_file.to_csv(f'D:\\Downloads\\{file}.csv', index_label='Index')
        elif mode == 'XLSX':
                csv_file.to_excel(f'D:\\Downloads\\{file}.xlsx', sheet_name='Sheet1', index_label='Index')

def create_csv(p):
    data_list = []

    print('CSV thread has started!')
    for i in range(50):
        data = p.get()
        data = data.decode('utf-8', errors='ignore')

        if data:
            data_list.append([i, data])

    df = pd.DataFrame(data_list, columns=['Index', 'Data'])

    # Append to the CSV file
    df.to_csv(r'D:\Downloads\Date_Microcontroller.csv', mode='a', header=False, index=False, index_label='Index')
    print('CSV Thread has closed.')




