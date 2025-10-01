# 🏗 Architecture

1. **AWS CLI**
   - Created S3 buckets for raw, processed, and query-results.
   - Uploaded initial sample weather data.

2. **AWS Lambda + EventBridge**
   - Lambda pulls real-time weather data from OpenWeather API.
   - EventBridge schedules Lambda every 5 minutes.

3. **Amazon S3**
   - Raw → JSON data from Lambda.
   - Processed → Cleaned data for queries.
   - Query-results → Athena query outputs.

4. **AWS Glue**
   - Glue crawler builds schema from JSON.
   - Creates `weather_json_raw` table & `weather_rt_view` view.

5. **Amazon Athena**
   - Queries weather data stored in S3.
   - Exposes SQL-based access to raw & processed weather data.

6. **Power BI**
   - Connected via Athena ODBC Driver.
   - Built dashboards for **Temperature Trends** & **Wind Speed Trends**.

