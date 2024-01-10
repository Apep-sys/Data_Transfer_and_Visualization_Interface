import pandas as pd


def process_csv(type, path, mode):

    # TODO Modify the two functions to be a single one, depending on the file type given through the user Entry/Input
    if type == 'CSV':
        df = pd.read_csv(path)
    elif type == 'XLSX':
        df = pd.read_excel(path, sheet_name='Sheet1', index_col=0)
    col_names = df.columns.tolist()
    temp_file = []
    umid_file = []
    prezenta_file = []
    viteza_file = []
    pozitie_file = []
    file_list = {'Temp': temp_file, 'Umiditate': umid_file, 'Prezenta': prezenta_file, 'Pozitie': pozitie_file,
                 'Viteza': viteza_file}

    for name in col_names:
        file = df[name].tolist()
        if 'Temp' in name:
            temp_file.extend(file)
        elif 'Umiditate' in name:
            umid_file.extend(file)
        elif 'Prezenta' in name:
            prezenta_file.extend(file)
        elif 'Pozitie' in name:
            pozitie_file.extend(file)
        elif 'Viteza' in name:
            viteza_file.extend(file)

    for file in file_list:
        if file_list.get(file):
            csv_file = pd.DataFrame({file: file_list.get(file)})
        else:
            pass
        if mode == 'CSV':
                csv_file.to_csv(f'D:\\Downloads\\{file}.csv', index_label='Index')
        elif mode == 'XLSX':
                csv_file.to_excel(f'D:\\Downloads\\{file}.xlsx', sheet_name='Sheet1', index_label='Index')




