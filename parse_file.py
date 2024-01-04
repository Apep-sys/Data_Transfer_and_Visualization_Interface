import pandas as pd

#TODO To make a function for both reading and saving as CSV or XLSX
df = pd.read_csv('D:\\Downloads\\Date_CSV.csv')
col_names = df.columns.tolist()
csv_names = ['Temp', 'Umiditate', 'Prezenta', 'Viteza', 'Pozitie']
temp_file = []
umid_file = []
prezenta_file = []
viteza_file = []
pozitie_file = []
file_list = {'Temp': temp_file, 'Umiditate': umid_file, 'Prezenta': prezenta_file, 'Pozitie': pozitie_file,
             'Viteza': viteza_file}

for index, name in enumerate(col_names):
    file = pd.read_csv('D:\\Downloads\\Date_CSV.csv', header=0, usecols=[index])
    if 'Temp' in name:
        temp_file.append(file)
    elif 'Umiditate' in name:
        umid_file.append(file)
    elif 'Prezenta' in name:
        prezenta_file.append(file)
    elif 'Pozitie' in name:
        pozitie_file.append(file)
    elif 'Viteza' in name:
        viteza_file.append(file)


for file in file_list:
    if file_list.get(file):
        print(file_list.get(file))
        csv_file = pd.DataFrame(file_list.get(file))
        csv_file.to_csv(f'D:\\Downloads\\{file}.csv')
