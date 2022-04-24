import pandas as pd
import requests as r
import json

base_url = ''

df = pd.read_csv('test.csv', index_col=0, nrows=1)
X_test = df.drop(columns=['Loan_ID', 'Loan_Status'])
X_test = json.loads(X_test.to_json(orient='records'))

response = r.post(base_url + '/predict', json=X_test)

if response.status_code == 200:
    print('...')
    print('request succesful')
    print('...')
    print(response.json())
    
else:
    print(f'request failed: {response.status_code}')