import pandas as pd
import requests
import numpy as np

'''
Updates: 
- 2021-02-04: Created the TestSample.csv file in the new data folder and added the path to it here . This way you don't have to create it yourself
Notes:
- If you run into a json-body not found error, than you forgot to configure the application/json mapping template in the method
- Some students had the problem: They get 200 here but the ClodWatch log of the Lambda says KeyError: 'context'  -- I can only force this when I dont't send in a payload to the API. Make sure you send data
- If you get 403 error: Make sure to add the resource name you created in API gateway to the URL . In my case "hello". If you just copy out your URL from the "stage" in the UI then this is missing. 
'''

# URL of your endpoint
URL = "https://ia4n6jlhbf.execute-api.us-east-1.amazonaws.com/ecommerce_prod/"


#read the testfile
data = pd.read_csv(r'D:\Kurse-Tutorials\AWS\data\testdata.csv', sep = ',')
print(data)
print('Count dataframe rows:' + str(len(data)))


# cleaning the dataset and remove rows where one or more of the values are missing: invoiceno, stockcode, quantity, customerid
data_new = data.dropna(subset=['InvoiceNo', 'StockCode', 'Quantity', 'CustomerID'])
print(data_new)
print('Count dataframe rows:' + str(len(data)))


# splitting the dataframe in multiple



# simulate streaming = random amount between 100 and 500 rows sended in a random time between 3 and 20 secondes



# write all the rows from the subset to the api as put request
# for i in data.index:
#     try:
#         # convert the row to json
#         export = data.loc[i].to_json()

#         #send it to the api
#         response = requests.post(URL, data = export)

#         # print the returncode
#         print(export)
#         print(response)
#     except:
#         print(data.loc[i])