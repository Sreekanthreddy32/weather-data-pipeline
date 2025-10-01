# 🧩 AWS Glue Jobs & Crawler

1. **Glue Crawler**
   - Crawled `s3://bhadri-weather-pipeline/raw/`.
   - Created database `weather_rt_db`.
   - Generated table `weather_json_raw`.

2. **Glue Transform Job (Optional)**
   - Convert JSON to Parquet for optimized Athena queries.
   - Write to `s3://bhadri-weather-pipeline/processed/`.

3. **Output**
   - Use `weather_rt_view` for querying in Athena.

