# 📑 Athena Queries (Used in Project)

## 1️⃣ Test Query (Check data from view)
```sql
SELECT *
FROM weather_rt_db.weather_rt_view
LIMIT 10;
```

## 2️⃣ Create Table from JSON in S3
```sql
CREATE EXTERNAL TABLE weather_json_raw (
  obs_time string,
  city string,
  temp_c double,
  wind_ms double
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://bhadri-weather-pipeline/raw/';
```

## 3️⃣ Create View for Clean Data
```sql
CREATE OR REPLACE VIEW weather_rt_view AS
SELECT obs_time, city, temp_c, wind_ms
FROM weather_json_raw
WHERE temp_c IS NOT NULL;
```
