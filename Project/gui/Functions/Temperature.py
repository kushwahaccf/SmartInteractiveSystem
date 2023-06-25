import requests

def fetch_temperature():
    # Replace 'YOUR_API_KEY' with your actual API key
    api_key = 'cc7ee320fb1029be564636a4dde43306'
    city = 'Hamirpur'  # Replace with the desired city

    # Make an API request to fetch the temperature data
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()

    # Extract the temperature from the response data
    temperature = data['main']['temp']
    temperature = temperature - 273.15  # Convert from Kelvin to Celsius
    temperature = round(temperature, 2)

    # Update the temperature label
    return temperature

