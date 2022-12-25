import random
import pandas as pd
import requests
import time


# URL of your endpoint
URL = "https://ia4n6jlhbf.execute-api.us-east-1.amazonaws.com/ecommerce_prod/"


#read the testfile
data = pd.read_csv(r'D:\Kurse-Tutorials\AWS\data\testdata.csv', sep = ',')
print(data)
print('Count dataframe rows:' + str(len(data)))


# cleaning the dataset and remove rows where one or more of the values are missing: invoiceno, stockcode, quantity, customerid
data_new = data.dropna(subset=['InvoiceNo', 'StockCode', 'Quantity', 'CustomerID'])
print(data_new)
print('Count dataframe rows:' + str(len(data_new)))


# simulate streaming, sleep random amount between 0,2 and 3 seconds per row
# write all the rows from the subset to the api as put request
for i in data_new.index:
    try:
        # convert the row to json
        export = data_new.loc[i].to_json()

        #send it to the api
        response = requests.post(URL, data = export)

        # print the returncode
        print(f'{response} - {export}') 
        sleeptime = random.uniform(0.2, 3)
        print(f'Sleep: {sleeptime}')
        time.sleep(sleeptime)

    except:
        print(data_new.loc[i])