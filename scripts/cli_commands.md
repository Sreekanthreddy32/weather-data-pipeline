# Create bucket
aws s3 mb s3://bhadri-weather-pipeline

# Create folder structure
aws s3api put-object --bucket bhadri-weather-pipeline --key raw/
aws s3api put-object --bucket bhadri-weather-pipeline --key processed/
aws s3api put-object --bucket bhadri-weather-pipeline --key query-results/

# Upload sample data
aws s3 cp weather_sample.csv s3://bhadri-weather-pipeline/raw/

