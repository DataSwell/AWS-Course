# AWS Data Engineering course

link to repository,
link to kaggle dataset 

## Use Case

1. **Streaming** <br/>
2. **Bulk import** <br/>

## AWS dataplattform

### Streaming
- **API Gateway** <br/>
To receive the streaming data we need to configure a REST API with GET and POST methods.
Stage ... Contains the URL which is needed for the Python streaming script.

- **Identity and Access Management** (IAM) <br/>
Roles
Policies

- **S3** <br/>
AWS Simple Storage Service (Amazon S3) is an key-value object storage service that offers scalability, data availability, security, and performance. 
We use S3 for creating a buckets to store the raw streamed data. 

- **Kinesis** <br/>

- **Kinesis Firehose** <br/>
The Firehose Delivery Stream connects with the Kinesis Data Stream and writes the data into a S3 Bucket. 
After that it copies the data from S3 into the referenced Redshift table.

- **Redshift** <br/>

- **CloudWatch** <br/>


### Bulk import
- **IAM**  <br/>

- **S3** <br/>

- **Glue** <br/>
Crawler: 
<br/>
Connections: 
<br/>
Data Catalog:
<br/>
Jobs:

- **Redshift** <br/>
