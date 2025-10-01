# 🌦 Weather Data Analytics Pipeline (AWS + Athena + Glue + Power BI)

[![AWS](https://img.shields.io/badge/AWS-Cloud-orange?logo=amazonaws)]()
[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)]()
[![Power BI](https://img.shields.io/badge/Power%20BI-Dashboards-yellow?logo=powerbi)]()
[![Athena](https://img.shields.io/badge/AWS-Athena-green?logo=amazonaws)]()

🚀 A **real-time weather data pipeline** built with **AWS serverless tools** (S3, Lambda, EventBridge, Glue, Athena) and **Power BI** for visualization.  

It demonstrates how to **ingest, store, query, and visualize** weather data end-to-end in the cloud.

---
## 🏗️ Architecture Overview
💻 **AWS CLI** → Create S3 buckets & upload initial files  
🌍 **OpenWeather API** → Weather data source  
⚡ **AWS Lambda + EventBridge** → Automate real-time ingestion into S3  
☁️ **Amazon S3** → Data lake (raw + processed + query results)  
🛠 **AWS Glue Crawler** → Auto-detect schema & create tables  
📚 **Glue Data Catalog** → Metadata storage  
🗂 **Amazon Athena** → Query datasets using SQL  
🔌 **Athena ODBC Driver** → Bridge to Power BI  
📊 **Power BI** → Interactive dashboards  

---

## 🔄 Project Workflow

### 1️⃣ Data Ingestion
- Used **AWS CLI** to create S3 bucket and folder structure (`raw`, `processed`, `query-results`).  
- Uploaded sample weather data files to **S3/raw/**.  
- Automated **real-time ingestion** using **AWS Lambda** triggered by **EventBridge** (every 5 mins).  

### 2️⃣ Data Cataloging
- Ran an **AWS Glue Crawler** on the raw S3 bucket.  
- Created a new database `weather_rt_db` with two tables:  
  - `weather_json_raw` (raw JSON)  
  - `weather_rt_view` (cleaned view)  

### 3️⃣ Querying
- Used **Amazon Athena** to query weather data directly from S3.  
- Created SQL views to filter & clean the raw data.  
- Stored Athena query results back into `query-results/`.  

### 4️⃣ Visualization
- Installed **Athena ODBC Driver** and configured a System DSN.  
- Connected Power BI to Athena via ODBC.  
- Built dashboards with:  
  - 📈 Temperature trends over time  
  - 🌬 Wind speed trends over time  

---

## 📊 Example Dashboards

📈 **Temperature Trends (London)**  
🌬 **Wind Speed Trends (London)**  

*(Screenshots are saved in `/images/` folder)*



## ✅ Key Learnings
✔️ Built a **serverless AWS pipeline** using S3, Lambda, EventBridge, Glue & Athena  
✔️ Automated ingestion of **real-time weather data**  
✔️ Connected **Athena → Power BI** via ODBC  
✔️ Designed **interactive dashboards** for insights  

---

👨‍💻 **Author**: Sreekanth Reddy  
🔗 [GitHub Profile](https://github.com/Sreekanthreddy32)

