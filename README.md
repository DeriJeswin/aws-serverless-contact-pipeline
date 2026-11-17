# ☁️ AWS Serverless Contact Form Pipeline

A full-stack, event-driven serverless web application built on **Amazon Web Services (AWS)**. This project eliminates 24/7 server management by using **Amazon S3**, **API Gateway**, **AWS Lambda**, and **DynamoDB** to capture, validate, and store user inquiries securely at zero idle cost.

## 🌐 Live Demo
Test the live serverless contact form here:  
👉 **[Live AWS S3 Contact Form](https://amazonaws.com)**

---

## 🏗️ Architecture Flow

```text
[User Browser] ──▶ [Amazon S3 (HTTPS Static Frontend)]
                           │  HTTPS POST (JSON)
                           ▼
                 [Amazon API Gateway] ──(CORS Validation)──▶ [AWS Lambda (Python 3.12)]
                                                                    │
                                              ┌─────────────────────┴─────────────────────┐
                                              ▼ (Least-Privilege IAM)                     ▼
                                     [Amazon DynamoDB]                          [Amazon CloudWatch]
                                    (ContactSubmission)                          (Execution Logs)
```

---

## 🛠️ AWS Services & Technologies Used

* **Frontend Hosting**: Amazon S3 (Static HTTPS hosting), HTML5, CSS3, JavaScript (`Fetch API`)
* **API Management**: Amazon API Gateway (HTTP API, CORS configuration, `$default` auto-deploy stage)
* **Serverless Compute**: AWS Lambda (Python 3.12, `boto3` SDK, `uuid`, `datetime`)
* **NoSQL Database**: Amazon DynamoDB (`ContactSubmission` table, Partition Key: `SubmissionID`)
* **Security & Identity**: AWS IAM (Custom execution role following the Principle of Least Privilege)
* **Monitoring**: Amazon CloudWatch Logs

---

## 📸 Project Proof & Screenshots

### 1. Live Form Submission
![Form Success](success%20ss.png)

### 2. Stored Record in DynamoDB
![DynamoDB Records](Serverless%20Form%20Datas.png)

---

## 🧠 Troubleshooting & Lessons Learned

* **CORS & Origin Security**: Hosted the frontend over HTTPS on Amazon S3 rather than local `file://` paths to ensure valid web origins and properly configured `OPTIONS`/`POST` preflight headers in API Gateway.
* **Route & Resource Alignment**: Verified exact API Gateway route paths (`/contact`) and DynamoDB table naming (`ContactSubmission`) across frontend JavaScript and backend Python `boto3` handlers.

---

## 👤 Author

**Deri Jeswin**  
* Aspiring Cloud & Network Engineer | CCNA & AWS Enthusiast  
* Email: derisunil@gmail.com
