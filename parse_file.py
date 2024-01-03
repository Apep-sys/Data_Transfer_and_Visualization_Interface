import pandas as pd

df = pd.read_csv('D:\\Downloads\\Date_CSV.csv')
col_length = df.shape[1]
col_names = df.columns.tolist()
for index, name in enumerate(col_names):
    if 'Temp' in name:
        col_names[index] = 'Temp'
    elif 'Umiditate' in name:
        col_names[index] = 'Umiditate'
    elif 'Prezenta' in name:
        col_names[index] = 'Prezenta'
    elif 'Viteza' in name:
        col_names[index] = 'Viteza'
print(col_names)
for column in range(1, col_length):
    df = pd.read_csv('D:\\Downloads\\Date_CSV.csv', header=0,
                     usecols=[column])
#TODO To eliminate the repeating names of the columns in the list and make a file with each parameter



