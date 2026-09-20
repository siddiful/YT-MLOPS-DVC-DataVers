import pandas as pd
import os

data = {
    'Name' : ['Sid', 'Dhan', 'Ashok'],
    'Age' : [30, 32, 62],
    'City' : ['Bangalore', 'Navi Mumbai', 'Dibiyapur']
}

df = pd.DataFrame(data)

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'sample_data.csv')

df.to_csv(file_path, index=False)

print(f'CSV created at path: {file_path}')