import pandas as pd
import os

def load_csv_files(folder_path):
    files = []
    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith('.csv'):
            filepath = os.path.join(folder_path, filename)
            df = pd.read_csv(filepath)
            files.append({'name': filename, 'data': df})
    return files

