# 📦 Serverless Log Processing Pipeline (AWS White Belt Project)

## 🔧 Use Case
A cloud-native solution to process application logs via two input methods:
- 📁 File uploads to an S3 bucket (batch ingestion)
- 🌐 HTTP API for real-time log ingestion

All logs are automatically processed by AWS Lambda and stored in DynamoDB for fast access, metadata search, and reporting.

---

## 🗺️ Architecture Diagram

  ![image](https://github.com/user-attachments/assets/5a98b49b-38d8-4dfa-ac1c-397f6a1f280b)


**Flow:**

1. Client uploads a `.log` file to S3 → S3 event triggers Lambda → Lambda writes metadata to DynamoDB.
2. External apps POST to API Gateway → Triggers Lambda → Metadata stored in DynamoDB.

---

## ☁️ AWS Services Used
- S3
- API Gateway
- Lambda
- DynamoDB
- IAM
- CloudWatch

---

## 🧱 Step-by-Step Instructions

### 1. Create the S3 Bucket
 ![image](https://github.com/user-attachments/assets/bd26ae91-2576-4e80-b705-854eafe41044)


- Region: `us-east-1`
- Block all public access (enabled)
- Enable versioning (optional)

---

### 2. Create the DynamoDB Table
  ![image](https://github.com/user-attachments/assets/e7b9a660-f6d2-48ad-83f9-d7ebe26fdf60)
  ![image](https://github.com/user-attachments/assets/2d713aa6-87c2-428b-ae43-54c61b4fee20)
  ![image](https://github.com/user-attachments/assets/2ffd3fe2-476b-46da-8df3-3217887d2fd9)

  
- Name: `LogMetadataTable`
- Partition Key: `log_id` (String)

---

### 3. Write and Deploy Lambda Function for S3 Events
  ![image](https://github.com/user-attachments/assets/fc49ad78-d58a-4ebd-81d6-b194776079a6)
  ![image](https://github.com/user-attachments/assets/326eeb91-a307-49da-81e4-bf19792827a1)
  ![image](https://github.com/user-attachments/assets/c5ed1eb0-d057-417d-9555-cdeea464295b)

- Language: Python 3.9
- File: `log_processor.py`
- Handler: `log_processor.lambda_handler`
- Permissions: `AmazonDynamoDBFullAccess`

---

### 4. Add S3 Trigger to Lambda
  ![image](https://github.com/user-attachments/assets/70aa8667-18d5-4893-a790-0d28ae8aa07e)
  ![image](https://github.com/user-attachments/assets/94910e12-f5bc-4cf8-8617-b8b0fcdd2795)

- Event type: `PUT`
- Bucket: `jm-serverless-logs-bucket`

---

### 5. Create Lambda for API Ingestion
  ![image](https://github.com/user-attachments/assets/62a17fe3-8006-41ac-9cf3-f0762e25fa77)
  ![image](https://github.com/user-attachments/assets/81260be7-9cfc-4840-ba19-60c304a2b683)
  ![image](https://github.com/user-attachments/assets/06370d3b-a003-450e-b556-10660fe12b49)
  ![image](https://github.com/user-attachments/assets/18437509-4093-40ad-aa25-75868ac4e824)

- File: `api_log_ingestor.py`
- Parses POST request and stores metadata in DynamoDB

---

### 6. Set Up API Gateway
 ![image](https://github.com/user-attachments/assets/dbcd1cbf-362a-4bad-962c-9d42a9a886ab)
 ![image](https://github.com/user-attachments/assets/d1cb47b2-f874-4c38-a992-f08733fbec26)
 ![image](https://github.com/user-attachments/assets/2b6dd95a-ba28-4950-8331-d30b818f2179)
  
- Route: `/logs`
- Method: POST
- Connected to `apiLogIngestorLambda`

---

### 7. Test the Workflow
  ![image](https://github.com/user-attachments/assets/8c946120-80ab-4c87-ad89-3dbb9eb2db13)
  ![image](https://github.com/user-attachments/assets/b8b14c5b-3a75-4936-ad66-fa7979b51a05)
  ![image](https://github.com/user-attachments/assets/8fe9cee7-3b04-4bda-9d98-4a54f3e74819)
  ![image](https://github.com/user-attachments/assets/bb98d732-6905-419f-addc-b56e03d384d4)
  ![image](https://github.com/user-attachments/assets/9578b115-2b4b-4d05-bf13-6047f9c32a85)
  ![image](https://github.com/user-attachments/assets/9d45a99c-acf0-439f-b66a-0d95a3a4279e)
  ![image](https://github.com/user-attachments/assets/c9dd5acd-d3eb-456f-9dcd-2f727897a9c9)
    
- Upload `.log` file to S3
- Send POST via curl/Postman to API Gateway
- Check DynamoDB for new records

---

## 📈 Outcome

✅ Built a scalable, serverless pipeline with real-world application  
✅ Gained hands-on experience with event-driven architecture  
✅ Used industry tooling and permissions properly  
✅ Ready to speak to this project in interviews

---

## 📌 Project Author

**Jason Mallard**  
AWS Certified Solutions Architect – Associate 
Cloud | DevOps | Infrastructure as Code  

> 🚫 **Read-Only Repository**
>
> This project has been **archived intentionally** as a showcase for recruiters, classmates, and interviewers.  
> Feel free to **clone or fork** the code for reference, but no changes will be made to this repository.
>
> 📁 **Status**: `Archived` | 🔐 **Mode**: `Read-Only` | 💼 **Purpose**: `Interview & Portfolio Demo`


