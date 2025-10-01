import json, boto3, requests, datetime

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    city = "London"
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeather API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url).json()
    data = {
        "obs_time": str(datetime.datetime.utcnow()),
        "city": city,
        "temp_c": response['main']['temp'],
        "wind_ms": response['wind']['speed']
    }
    
    file_name = f"raw/{city}_{datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S')}.json"
    s3.put_object(Bucket="bhadri-weather-pipeline", Key=file_name, Body=json.dumps(data))
    
    return {"status": "success", "file": file_name}

