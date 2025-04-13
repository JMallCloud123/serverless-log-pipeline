# Serverless Log Pipeline Progress Log

## 🔰 White Belt Phase

### ✅ Setup Phase (Complete)
- [x] Created professional GitHub account
- [x] Installed Git and AWS CLI
- [x] Cloned and pushed first repo
- [x] Configured Git with correct credentials
- [x] Initialized Terraform

### ✅ AWS Resource Phase (Complete)
- [x] Created S3 bucket `jm-serverless-logs-bucket`
- [x] Created DynamoDB table `LogMetadataTable`

### ✅ Lambda Phase (Complete)
- [x] Wrote log processing function in Python
- [x] Packaged and deployed to Lambda
- [x] Set up S3 event trigger
- [x] Granted IAM permissions
- [x] Verified log insertions in DynamoDB

### ✅ API Gateway Phase (Complete)
- [x] Created API Lambda (`apiLogIngestorLambda`)
- [x] Wrote ingestion logic for POST request
- [x] Deployed HTTP API using API Gateway
- [x] Tested using curl and Postman
- [x] Verified entry in DynamoDB from HTTP request

### 🧠 Notes / Observations
- Learned how to configure IAM roles
- Realized the importance of regional consistency
- First time using Terraform to plan future automation
- Observed the benefits of a Lambda function
- Learned to troubleshoot a few common errors with Lambda functions
- Learned to create an API Gateway to allow external log ingestion

---


I just officially completed my White Belt AWS Dojo Project:

✅ Built a serverless, event-driven architecture using S3, Lambda, DynamoDB
✅ Integrated API Gateway to allow external log ingestion
✅ Secured it with IAM
✅ Deployed, tested, debugged, and committed everything like a real Cloud Engineer
