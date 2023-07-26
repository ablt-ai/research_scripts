import pandas as pd
import re


def convert_to_csv(filename):
    with open(filename, 'r') as file:
        content = file.read()
        table = re.findall(r'benchmark:.*?OPS(.*?)\n\n', content, re.DOTALL)[0]
        lines = table.split('\n')[1:-1]
        data = [re.split(r'\s{2,}', line) for line in lines]
        df = pd.DataFrame(data)
        df.columns = ['Name (time in ms)', 'Min', 'Max', 'Mean', 'StdDev', 'Median', 'IQR', 'Outliers', 'OPS', 'Rounds', 'Iterations']  # добавляем заголовки
        df = df.replace(r' \(\d+\.?\d*\)', '', regex=True)
        df = df.replace(r'\.', '', regex=True)
        df = df.replace(r',', '.', regex=True)
        for col in df.columns[1:8]:
            df[col] = df[col].apply(lambda x: '0' if x is None or not any(c in x for c in ['.', ',']) else x)
        df.to_csv('output.csv', index=False)
        print("output saved to output.csv")


convert_to_csv('message.txt')